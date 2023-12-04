from MenuFHR import Menu

#Function to create a list of objects
def createListFHR():
    listOfItems = []
    numberOfItems = input("How many items will you order today? ")
    if numberOfItems > 0:
        for itemNumber in numberOfItems:
            print("Item #" + itemNumber)
            food = input("Enter food: ")
            foodInPounds = input("Enter amount of pounds: ")
            listOfItems.append(food, foodInPounds)
    else:
        print("Number of items must be at least 1")

#Function to display the contents of the list
def displayListFHR(listOfFood):
    for food in listOfFood:
        print("Item: " + food.foodName)
        print("Amount: " + food.foodAmount)
        print("Price per pound: " + food.standardPrice)
        print("Price of order: " + food.totalPrice)

#Function to calculate the total cost of all items
def totalCostFHR(listOfFood):
    foodPrice = ()
    for price in foodPrice:
        price.append(price.foodPrices)
    sum(foodPrice)

#The main function
def main():
    createListFHR()
    displayListFHR()
    totalCostFHR()

main()

