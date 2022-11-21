from django.test import TestCase
from lessons.price_calculator import CalculatePrice

class priceTest(TestCase):

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
        cost = CalculatePrice(1, False, True).calculatePrice()
        self.assertEqual(cost, 12.25)