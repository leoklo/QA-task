# Lev Klochkov
# 22/05/2019
# qa-unit-intern-task
# Test file

from unittest import TestCase

from app.main import *
from app.validate import *


class TestTestRunsAnalyzer(TestCase):
    output_path = 'result.json'
    input_path = '1.json', '2.json', '3.json'

    def test_parse(self):
        analyzer = TestRunsAnalyzer(self.input_path[0], self.input_path[1], self.input_path[2])
        test_logs = analyzer.test_runs
        self.assertEqual(len(test_logs), 2)
        self.assertTrue(validate({logs: list(test_logs.values())}, schema_output))

    def test_write(self):
        analyzer = TestRunsAnalyzer(self.input_path[0], self.input_path[1], self.input_path[2])
        analyzer.write_output(self.output_path)
        test_logs = read_file(self.output_path)
        self.assertEqual(len(test_logs[logs]), 2)
        validate(test_logs, schema_output)
