# Lev Klochkov
# 22/05/2019
# qa-unit-intern-task
# Run from run.py

import datetime
import json

from app.validate import *


def read_file(path) -> dict:
    """
    Returns json file as dictionary
    :param path: Path to file
    :return: Json object as dictionary
    """
    with open(path, 'r') as file:
        return json.loads(file.read())


def parse_time(time_str: str, time_format: str) -> datetime:
    return datetime.datetime.strptime(time_str, time_format)


class TestRunsAnalyzer:
    """
    Main class
    """
    test_runs = dict()

    def __init__(self, path1, path2, path3):
        inputs = [read_file(path1), read_file(path2), read_file(path3)]
        # validating input according to schemas
        for i in range(0, len(inputs)):
            if not validate(inputs[i], schema_input[i]):
                print('Invalid input schema')
                return
        if inputs is not None:
            self.parse_first_file(inputs[0])
            self.parse_second_file(inputs[1])
            self.parse_third_file(inputs[2])

    def parse_first_file(self, obj: dict):
        """
        Parsing first file to dictionary of dictionaries stored by timestamps
        If there would be two logs for one time, that will be a problem
        :param obj:  First file json object
        """
        logs_dict = obj[logs]
        for entry in logs_dict:
            timestamp = str(
                datetime.datetime.utcfromtimestamp(int(entry[time])).replace(tzinfo=datetime.timezone.utc))
            self.test_runs[timestamp] = {time: timestamp, name: entry[test], result: entry[output] != fail}

    def parse_second_file(self, obj: dict):
        """
        Parsing second file to dictionary of dictionaries stored by timestamps
        If there would be two logs for one time, that will be a problem
        :param obj: Second file json object
        :return:
        """
        suites = obj['suites']
        for suit in suites:
            cases_dict = suit[cases]
            for case in cases_dict:
                timestamp = str(
                    parse_time(case[time], '%A, %d-%b-%y %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc))
                self.test_runs[timestamp] = {time: timestamp, name: case[name], result: case[errors] == 0}

    def parse_third_file(self, obj: dict):
        """
        Adding expected and actual values to parsed logs from first and second files finding objects by timestamps
        :param obj: Third file json object
        """
        captures_dict = obj[captures]
        for capture in captures_dict:
            timestamp = str(parse_time(capture[time], '%Y-%m-%dT%H:%M:%S%z'))
            if timestamp in self.test_runs:
                self.test_runs[timestamp].update({expected: capture[expected], actual: capture[actual]})

    def write_output(self, path: str):
        """
        Validate output  to output object schema and write it to file
        :param path: Path to file
        """
        if len(self.test_runs) == 0:
            print('Empty input')
            return
        with open(path, 'w') as file:
            output_str = {logs: list(self.test_runs.values())}
            if not validate(output_str, schema_output):
                print('Invalid output schema!')
                return
            file.write(json.dumps(output_str))
