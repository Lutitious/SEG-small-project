from django.test import TestCase
from lessons.price_calculator import CalculatePrice

class priceTest(TestCase):

    def setUp(self):
        CalculatePrice.setCostPerHour(8.75)
        CalculatePrice.setPermanentDiscount(1)
        CalculatePrice.setRentedInstrumentCost(2)

    def test_fifteen_min_lesson(self):
        cost = CalculatePrice(1, False, False).calculatePrice()
        self.assertEqual(cost, 8.75)

    def test_fifteen_min_lesson_with_rented_instrument(self):
        cost = CalculatePrice(1, True, False).calculatePrice()
        self.assertEqual(cost, 10.75)

    def test_fifteen_min_group_lesson_with_rented_instrument(self):
        cost = CalculatePrice(1, True, True).calculatePrice()
        self.assertEqual(cost, 8.125)


    def test_half_hour_group_lesson(self):
        cost = CalculatePrice(2, False, True).calculatePrice()
        self.assertEqual(cost, 12.25)

    def test_half_hour_group_lesson_cost_30(self):
        CalculatePrice.setCostPerFifteenMin(30)
        cost = CalculatePrice(2, False, True).calculatePrice()
        self.assertEqual(cost, 10.5)

    def test_half_hour_group_lesson_with_rented_instrument(self):
        cost = CalculatePrice(2, True, True).calculatePrice()
        self.assertEqual(cost, 13.25)


    def test_forty_five_min_group_lesson(self):
        cost = CalculatePrice(3, False, True).calculatePrice()
        self.assertEqual(cost, 18.375)

    def test_forty_five_min_group_lesson_cost_7_and_a_half(self):
        CalculatePrice.setCostPerFifteenMin(7.5)
        cost = CalculatePrice(3, False, True).calculatePrice()
        self.assertEqual(cost, 15.75)

    def test_forty_five_min_group_lesson_with_rented_instrument(self):
        cost = CalculatePrice(3, True, True).calculatePrice()
        self.assertEqual(cost, 20.375)
        

    def test_one_hour_group_lesson(self):
        cost = CalculatePrice(4, False, True).calculatePrice()
        self.assertEqual(cost, 24.5)

    def test_one_hour_group_lesson_cost_7_and_a_half(self):
        CalculatePrice.setCostPerFifteenMin(7.5)
        cost = CalculatePrice(4, False, True).calculatePrice()
        self.assertEqual(cost, 21)

    def test_one_hour_group_lesson_with_rented_instrument(self):
        cost = CalculatePrice(4, True, True).calculatePrice()
        self.assertEqual(cost, 26.5)