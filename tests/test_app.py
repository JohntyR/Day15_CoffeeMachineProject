import unittest
from unittest.mock import patch

from coffeemachine import app  # pylint: disable=import-error


class BasicTestCase(unittest.TestCase):
    def test_report(self):
        resourceDict = {"Water": [100, "ml"]}
        reportResults = app.report(resourceDict)
        self.assertEqual(reportResults, "Water:\t100ml\n")

    def test_report_key_equals_money(self):
        resourceDict = {"Money": [100, "$"]}
        reportResults = app.report(resourceDict)
        self.assertEqual(reportResults, "Money:\t$100\n")

    def test_report_multiple_keys(self):
        resourceDict = {"Money": [100, "$"], "Water": [100, "ml"]}
        reportResults = app.report(resourceDict)
        self.assertEqual(reportResults, "Money:\t$100\nWater:\t100ml\n")


if __name__ == "__main__":
    unittest.main()