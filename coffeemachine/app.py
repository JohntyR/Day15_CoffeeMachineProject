resourceManager = {
    "Water": [100, "ml"],
    "Milk": [50, "ml"],
    "Coffee": [76, "g"],
    "Money": [2.5, "$"],
}


def report(resourceDict):
    returnString = ""
    for key, value in resourceDict.items():
        if key == "Money":
            returnString += f"{key}:\t{value[1]}{value[0]}\n"
        else:
            returnString += f"{key}:\t{value[0]}{value[1]}\n"
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


if __name__ == "__main__":
    run_coffee_machine()