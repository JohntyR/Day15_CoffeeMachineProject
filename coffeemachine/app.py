resourceManager = {
    "Water": [1000, "ml"],
    "Milk": [500, "ml"],
    "Coffee": [76, "g"],
    "Money": [2.5, "$"],
}

drinkResources = {
    "espresso": {"Water": 60, "Coffee": 16},
    "latte": {"Water": 60, "Milk": 200, "Coffee": 16},
    "cappuccino": {"Water": 20, "Milk": 125, "Coffee": 14},
}


def report(resourceDict):
    returnString = ""
    for key, value in resourceDict.items():
        if key == "Money":
            returnString += f"{key}:\t{value[1]}{value[0]}\n"
        else:
            returnString += f"{key}:\t{value[0]}{value[1]}\n"
    return returnString


def check_resources(drinkDict, resourceDict):
    returnString = ""
    for key, value in drinkDict.items():
        if resourceDict[key][0] < value:
            returnString += f"Sorry not enough {key}"
            return returnString
    returnString = "thank you"
    return returnString


def run_coffee_machine():

    while True:
        print("Hi, what would you like? (espresso/latte/cappuccino)")
        userInput = input()
        print(userInput)
        if userInput == "off":
            break
        elif userInput == "report":
            print(report(resourceManager))
        elif userInput in ["espresso", "latte", "cappuccino"]:
            print(drinkResources[userInput])
            print(check_resources(drinkResources[userInput], resourceManager))


if __name__ == "__main__":
    run_coffee_machine()