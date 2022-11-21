class CalculatePrice:

    costPerHour = 35.0
    permanentDiscount = 1.0
    rentedInstrumentCost = 2

    def __init__(self, hours, rentedInstrument, groupLesson):
        self.hours = hours
        self.rentedInstrument = rentedInstrument
        self.groupLesson = groupLesson

    def calculatePrice(self):
        rentedInstrumentSum = 0
        if self.rentedInstrument:
            rentedInstrumentSum += self.hours * self.rentedInstrumentCost
        groupLessonDiscount = 1
        if self.groupLesson:
            groupLessonDiscount = 0.7
        return (self.costPerHour * self.hours * groupLessonDiscount) + rentedInstrumentSum

    @staticmethod
    def setCostPerHour(costPerHour):
        CalculatePrice.costPerHour = costPerHour

    @staticmethod
    def setPermanentDiscount(permanentDiscount):
        CalculatePrice.permanentDiscount = permanentDiscount

    @staticmethod
    def setRentedInstrumentCost(rentedInstrumentCost):
        CalculatePrice.rentedInstrumentCost = rentedInstrumentCost
