import tkinter as tk
from tkinter import messagebox

class ExpensesWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Додавання витрат")
        self.configure(bg="#000000")

        label = tk.Label(self, text="Введіть суму витрат:", bg="#000000", fg="#FFFFFF")
        label.pack(pady=10)
        
        amount_entry = tk.Entry(self)
        amount_entry.pack(pady=5)
        
        category_label = tk.Label(self, text="Оберіть категорію:", bg="#000000", fg="#FFFFFF")
        category_label.pack(pady=5)
        
        category_var = tk.StringVar(self)
        category_var.set(master.expense_categories[0])
        category_menu = tk.OptionMenu(self, category_var, *master.expense_categories)
        category_menu.pack(pady=5)
        
        confirm_button = tk.Button(
            self, text="Додати", 
            command=lambda: master.record_expenses(amount_entry.get(), category_var.get(), self), 
            bg="#9400D3", fg="#FFFFFF", font=("Helvetica", 12, "bold")
        )
        confirm_button.pack(pady=10)
