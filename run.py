# Lev Klochkov
# 22/05/2019
# qa-unit-intern-task
# Run with following arguments: first file path, second file path, third file path, result file path

import sys

from app import TestRunsAnalyzer

if __name__ == '__main__':
    TestRunsAnalyzer(sys.argv[1], sys.argv[2], sys.argv[3]).write_output(sys.argv[4])
