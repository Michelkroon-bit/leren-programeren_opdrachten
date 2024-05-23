import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

#schrijf je test hier


if __name__ == "__main__":
    expected = 11
    result = JOURNEY_IN_DAYS
    test('dagen_test - test 1',expected, result)
    report()