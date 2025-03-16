import tkinter as tk
from datetime import datetime
from settings import SettingsWindow
from savings import SavingsWindow
from expenses import ExpensesWindow
from income import IncomeWindow
from expense_details import ExpenseDetailsWindow

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Фінансовий щоденник")
        self.geometry("800x600")
        self.configure(bg="#000000")
        self.create_main_menu()
        self.show_date()

        self.income = 0
        self.expenses = 0
        self.net_income = self.income - self.expenses
        self.savings_goal = 0
        self.savings_progress = 0
        self.expense_categories = ['FOOD', 'Transport', 'Apartment', 'Activity', 'Clother', 'Health', 'Other']
        self.expense_details = {category: [] for category in self.expense_categories}
        self.currency = tk.StringVar(value="грн")

    def create_main_menu(self):
        main_menu_frame = tk.Frame(self, bg="#000000")
        main_menu_frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(main_menu_frame, text="Твій фінансовий щоденник", font=("Helvetica", 24), bg="#000000", fg="#FFFFFF")
        label.pack(pady=20)

        buttons = [
            ("Налаштування", self.show_settings),
            ("Мета заощаджень", self.set_savings_goal),
            ("Витрати", self.show_expenses),
            ("Дохід", self.show_income),
            ("Переглянути детальніше", self.show_expense_details),
            ("Вихід", self.quit)
        ]

        for button_text, command in buttons:
            button = tk.Button(main_menu_frame, text=button_text, command=command, bg="#9400D3", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
            button.pack(pady=10)

    def show_date(self):
        current_date = datetime.now().strftime("%d.%m.%Y")
        date_label = tk.Label(self, text=f"Сьогоднішня дата: {current_date}", font=("Helvetica", 10), bg="#000000", fg="#FFFFFF")
        date_label.pack(side=tk.BOTTOM, pady=10, anchor="s")

    def show_settings(self):
        SettingsWindow(self)

    def set_savings_goal(self):
        SavingsWindow(self)

    def show_expenses(self):
        ExpensesWindow(self)

    def show_income(self):
        IncomeWindow(self)

    def show_expense_details(self):
        ExpenseDetailsWindow(self)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
