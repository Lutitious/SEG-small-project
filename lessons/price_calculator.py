class CalculatePrice:

    def __init__(self, hours, rentedInstrument, groupLesson):
        self.costPerHour = 35.0
        self.hours = hours
        self.rentedInstrument = rentedInstrument
        self.groupLesson = groupLesson

    def calculatePrice(self):
        rentedInstrumentCost = 0
        if self.rentedInstrument:
            rentedInstrumentCost += self.hours * 2
        groupLessonDiscount = 1
        if self.groupLesson:
            groupLessonDiscount = 0.7
        return (self.costPerHour * self.hours * groupLessonDiscount) + rentedInstrumentCost


