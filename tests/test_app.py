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

    def test_check_resources_enough(self):
        drinkDict = {"Water": 60, "Coffee": 16}
        resourceList = {
            "Water": [1000, "ml"],
            "Milk": [500, "ml"],
            "Coffee": [76, "g"],
            "Money": [2.5, "$"],
        }
        checkResults = app.check_resources(drinkDict, resourceList)
        self.assertEqual(checkResults, "thank you")

    def test_check_resources_insufficient_water(self):
        drinkDict = {"Water": 6000, "Coffee": 16}
        resourceList = {
            "Water": [1000, "ml"],
            "Milk": [500, "ml"],
            "Coffee": [76, "g"],
            "Money": [2.5, "$"],
        }
        checkResults = app.check_resources(drinkDict, resourceList)
        self.assertEqual(checkResults, "Sorry not enough Water")

    def test_check_resources_insufficient_coffee(self):
        drinkDict = {"Water": 60, "Coffee": 1600}
        resourceList = {
            "Water": [1000, "ml"],
            "Milk": [500, "ml"],
            "Coffee": [76, "g"],
            "Money": [2.5, "$"],
        }
        checkResults = app.check_resources(drinkDict, resourceList)
        self.assertEqual(checkResults, "Sorry not enough Coffee")


if __name__ == "__main__":
    unittest.main()