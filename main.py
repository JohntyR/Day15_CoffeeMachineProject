resourceManager = {
    "Water": [100, "ml"],
    "Milk": [50, "ml"],
    "Coffee": [76, "g"],
    "Money": [2.5, "$"],
}


while True:
    print("Hi, what would you like? (espresso/latte/cappuccino)")
    userInput = input()
    print(userInput)
    if userInput == "off":
        break
    elif userInput == "report":
        for key, value in resourceManager.items():
            if key == "Money":
                print(f"{key}:\t{value[1]}{value[0]}")
            else:
                print(f"{key}:\t{value[0]}{value[1]}")