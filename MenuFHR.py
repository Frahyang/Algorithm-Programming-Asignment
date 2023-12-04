class Menu:
#The initialiser
    def __init__(self, foodName, foodAmount):
        self.__foodName = foodName
        self.__foodAmount = foodAmount
        self.__standardPrice = self.__PriceList()
        self.totalPrice = self.calculatePriceFHR()

#The private method to store the list of items
    def __PriceList(self):
        if self.__foodName == "Dry Cured Iberian Ham":
            self.__standardPrice = 177.80
        elif self.__foodName == "Wagyu Steak":
            self.__standardPrice = 450.00
        elif self.__foodName == "Matsutake Mushrooms":
            self.__standardPrice = 272.00
        elif self.__foodName == "Kopi Luwak Coffe":
            self.__standardPrice = 306.50
        elif self.__foodName == "Moose Cheese":
            self.__standardPrice = 487.20
        elif self.__foodName == "White Truffles":
            self.__standardPrice = 3600.00
        elif self.__foodName == "Blue Fin Tuna":
            self.__standardPrice = 3603.00
        elif self.__foodName == "Le Bonnotte Potatoes":
            self.__standardPrice = 270.81
        else:
            self.__standardPrice = 0.00

#Public method to calculate the price
    def calculatePriceFHR(self):
        return self.__foodAmount * self.__standardPrice
    
    def __str__(self):
        print(self.totalPrice)

Menu("Dry Cured Iberian Ham", 1)