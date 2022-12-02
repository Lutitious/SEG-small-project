from django.test import TestCase
from lessons.price_calculator import CalculatePrice

class priceTest(TestCase):

    def setUp(self):
        CalculatePrice.setCostPerHour(35)
        CalculatePrice.setPermanentDiscount(1)
        CalculatePrice.setRentedInstrumentCost(2)

    def test_1_hour_lesson(self):
        cost = CalculatePrice(1, False, False).calculatePrice()
        self.assertEqual(cost, 35)

    def test_1_hour_lesson_with_rented_instrument(self):
        cost = CalculatePrice(1, True, False).calculatePrice()
        self.assertEqual(cost, 37)

    def test_1_hour_group_lesson_with_rented_instrument(self):
        cost = CalculatePrice(1, True, True).calculatePrice()
        self.assertEqual(cost, 26.5)

    def test_half_hour_group_lesson(self):
        cost = CalculatePrice(0.5, False, True).calculatePrice()
        self.assertEqual(cost, 12.25)

    def test_half_hour_group_lesson_cost_30(self):
        CalculatePrice.setCostPerHour(30)
        cost = CalculatePrice(0.5, False, True).calculatePrice()
        self.assertEqual(cost, 10.5)

    def test_half_hour_group_lesson_with_rented_instrument(self):
        cost = CalculatePrice(0.5, True, True).calculatePrice()
        self.assertEqual(cost, 13.25)