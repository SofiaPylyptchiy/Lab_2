import sys
import os
import unittest
from main import MainApplication

# Додаємо кореневу папку до шляхів імпорту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestMainApplication(unittest.TestCase):
    def setUp(self):
        """ Ініціалізація перед кожним тестом """
        self.app = MainApplication()

    def test_initial_values(self):
        """ Перевіряємо, чи початкові значення правильні """
        self.assertEqual(self.app.income, 0)
        self.assertEqual(self.app.expenses, 0)
        self.assertEqual(self.app.net_income, 0)
        self.assertEqual(self.app.savings_goal, 0)
        self.assertEqual(self.app.savings_progress, 0)
        self.assertEqual(self.app.currency.get(), "грн")  # Переконуємося, що валюта - "грн"

    def test_update_income(self):
        """ Перевіряємо оновлення доходу """
        self.app.income = 5000
        self.assertEqual(self.app.income, 5000)

    def test_update_expenses(self):
        """ Перевіряємо оновлення витрат """
        self.app.expenses = 1500
        self.assertEqual(self.app.expenses, 1500)

    def test_net_income_calculation(self):
        """ Перевіряємо правильність підрахунку чистого доходу """
        self.app.income = 8000
        self.app.expenses = 3000
        self.app.net_income = self.app.income - self.app.expenses
        self.assertEqual(self.app.net_income, 5000)

    def test_expense_categories(self):
        """ Перевіряємо, чи всі категорії витрат коректні """
        expected_categories = ['FOOD', 'Transport', 'Apartment', 'Activity', 'Clother', 'Health', 'Other']
        self.assertEqual(self.app.expense_categories, expected_categories)

    def test_currency_change(self):
        """ Перевіряємо зміну валюти """
        self.app.currency.set("USD")
        self.assertEqual(self.app.currency.get(), "USD")

if __name__ == "__main__":
    unittest.main()

