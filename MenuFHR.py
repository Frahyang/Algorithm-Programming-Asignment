class Menu:
#The initialiser
    def __init__(self, foodName, foodAmount):
        self.foodName = foodName
        self.foodAmount = foodAmount
        self.__PriceList()
        self.totalPrice = self.calculatePriceFHR()

#The private method to store the list of items
    def __PriceList(self):
        if self.foodName == "Dry Cured Iberian Ham":
            self.standardPrice = 177.80
        elif self.foodName == "Wagyu Steaks":
            self.standardPrice = 450.00
        elif self.foodName == "Matsutake Mushrooms":
            self.standardPrice = 272.00
        elif self.foodName == "Kopi Luwak Coffe":
            self.standardPrice = 306.50
        elif self.foodName == "Moose Cheese":
            self.standardPrice = 487.20
        elif self.foodName == "White Truffles":
            self.standardPrice = 3600.00
        elif self.foodName == "Blue Fin Tuna":
            self.standardPrice = 3603.00
        elif self.foodName == "Le Bonnotte Potatoes":
            self.standardPrice = 270.81
        else:
            self.standardPrice = 0.00

#Public method to calculate the price
    def calculatePriceFHR(self):
        return self.foodAmount * self.standardPrice
