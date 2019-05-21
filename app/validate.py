# Lev Klochkov
# 22/05/2019
# qa-unit-intern-task
# Run from run.py

import jsonschema

logs = "logs"
time = "time"
test = "test"
output = "output"
name = "name"
errors = "errors"
cases = "cases"
result = "result"
tests = "tests"
captures = "captures"
expected = "expected"
actual = "actual"

fail = 'fail'

schema_input = [{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        logs: {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        time: {
                            "type": "string"
                        },
                        test: {
                            "type": "string"
                        },
                        output: {
                            "type": "string"
                        }
                    },
                    "required": [
                        time,
                        test,
                        output
                    ]
                }
            ]
        }
    },
    "required": [
        logs
    ]
}, {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "suites": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        name: {
                            "type": "string"
                        },
                        tests: {
                            "type": "integer"
                        },
                        cases: {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        name: {
                                            "type": "string"
                                        },
                                        errors: {
                                            "type": "integer"
                                        },
                                        time: {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        name,
                                        errors,
                                        time]
                                }
                            ]
                        }
                    },
                    "required": [
                        name,
                        tests,
                        cases
                    ]
                }
            ]
        }
    },
    "required": [
        "suites"
    ]
}, {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        captures: {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        expected: {
                            "type": "string"
                        },
                        actual: {
                            "type": "string"
                        },
                        time: {
                            "type": "string"
                        }
                    },
                    "required": [
                        expected,
                        actual,
                        time
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        expected: {
                            "type": "string"
                        },
                        actual: {
                            "type": "string"
                        },
                        time: {
                            "type": "string"
                        }
                    },
                    "required": [
                        expected,
                        actual,
                        time
                    ]
                }
            ]
        }
    },
    "required": [
        captures
    ]
}]

schema_output = {
    "type": "object",
    "required": [logs],
    "properties": {
        logs: {
            "type": "array",
            "items": {
                "type": "object",
                "required": [time, name, result, expected, actual],
                "properties": {
                    time: {
                        "type": "string"
                    },
                    name: {
                        "type": "string"
                    },
                    result: {
                        "type": "boolean"
                    },
                    expected: {
                        "type": "string"
                    },
                    actual: {
                        "type": "string"
                    }
                }
            }
        }
    }
}


def validate(obj: dict, schema: dict) -> bool:
    """
    Validate a json object according to a schema
    :param obj: Json object as dictionary
    :param schema: Json schema
    :return: True if object is validated
    """
    try:
        jsonschema.validate(obj, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
