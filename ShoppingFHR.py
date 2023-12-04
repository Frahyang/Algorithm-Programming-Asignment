from MenuFHR import Menu

#Function to create a list of objects
def createListFHR():
    listOfItems = []
    while True:
        numberOfItems = int(input("How many items will you order today? "))
        if numberOfItems > 0:
            for itemNumber in range(numberOfItems):
                print("Item #" + str(itemNumber + 1))
                food = input("Enter food: ")
                foodAmount = float(input("Enter amount of pounds: "))
                object = Menu(food, foodAmount)
                listOfItems.append(object)
        else:
            print("Number of items must be at least 1")
            continue
        return listOfItems

#Function to display the contents of the list
def displayListFHR(listOfFood):
    for food in listOfFood:
        print("Item: " + food.foodName)
        print("Amount: " + str(food.foodAmount))
        print("Price per pound: " + str(food.standardPrice))
        print("Price of order: " + str(food.totalPrice))

#Function to calculate the total cost of all items
def totalCostFHR(foodPrice):
    listOfFood = []
    for price in foodPrice:
        listOfFood.append(price.totalPrice)
    return sum(listOfFood)

#The main function
def groceriesFHR():
    listOfFood = createListFHR()
    displayListFHR(listOfFood)
    print("Total cost: " + str(totalCostFHR(listOfFood)))

groceriesFHR()
