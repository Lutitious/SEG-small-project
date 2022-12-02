class CalculatePrice:

    costPerFifteenMin = 8.75
    permanentDiscount = 1.0
    rentedInstrumentCost = 2

    def __init__(self, Fifteen, rentedInstrument, groupLesson):
        self.Fifteen = Fifteen
        self.rentedInstrument = rentedInstrument
        self.groupLesson = groupLesson

    def calculatePrice(self):
        rentedInstrumentSum = 0
        if self.rentedInstrument:
            rentedInstrumentSum += self.Fifteen * self.rentedInstrumentCost
        groupLessonDiscount = 1
        if self.groupLesson:
            groupLessonDiscount = 0.7
        return (self.costPerFifteenMin * self.Fifteen * groupLessonDiscount) + rentedInstrumentSum

    @staticmethod
    def setCostPerFifteenMin(costPerFifteenMin):
        CalculatePrice.costPerFifteenMin = costPerFifteenMin

    @staticmethod
    def setPermanentDiscount(permanentDiscount):
        CalculatePrice.permanentDiscount = permanentDiscount

    @staticmethod
    def setRentedInstrumentCost(rentedInstrumentCost):
        CalculatePrice.rentedInstrumentCost = rentedInstrumentCost
