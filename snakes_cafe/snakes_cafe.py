x = "*"
y = x*50
print(y)
print("**", "  ", "Welcome to the Snakes Cafe!", "  ", "**") 
print("**", "  ", "Please see our menu below.", "  ", "**")
print("**")
print("**", "  ", "To quit anytime, type 'quit'", "  ", "**")
print(y)
print()
print("Appetizers")
print("----------")
myapps = ["Wings", "Cookies", "Spring Rolls"]
print(*myapps, sep="\n")
print()
print("Entrees")
print("----------")
myentree = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
print(*myentree, sep="\n")
print()
print("Desserts")
print("----------")
myDessert = ["Ice Cream", "Cake", "Pie"]
print(*myDessert, sep="\n")
print()
print("Drinks")
print("----------")
myDrinks = ["Coffee", "Tea", "Unicorn Tears"]
print(*myDrinks, sep="\n")
print()
print(y)
print("**", "What would you like to order?", "**")
print(y)
print()
item = []
menu = []
while True:
    menuChoice = input(">")


    if menuChoice in myapps:
        # print("Appetizers: ", menuChoice
        menu.append(menuChoice)

    if menuChoice in myentree:

        menu.append(menuChoice)

    if menuChoice in myDessert:
        menu.append(menuChoice)

    if menuChoice in myDrinks:
        menu.append(menuChoice)

        # menu.insert(menuChoice, menuChoice1)
    if menuChoice == "quit":
        break

    if menuChoice not in menu:
        print("Sorry, not on the menu!")

    # for menuChoice in menu:
    #     :
    #         item.append(menuChoice)
  
    # menu.append(menuChoice) #appends user menu to menu array
    print("%s orders of %s have been added to your meal." % (item, menuChoice))
