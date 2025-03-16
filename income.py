import tkinter as tk
from tkinter import messagebox

class IncomeWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Додавання доходу")
        self.configure(bg="#000000")

        label = tk.Label(self, text="Введіть суму доходу:", bg="#000000", fg="#FFFFFF")
        label.pack(pady=10)
        
        amount_entry = tk.Entry(self)
        amount_entry.pack(pady=5)
        
        confirm_button = tk.Button(
            self, text="Додати", 
            command=lambda: master.record_income(amount_entry.get(), self), 
            bg="#9400D3", fg="#FFFFFF", font=("Helvetica", 12, "bold")
        )
        confirm_button.pack(pady=10)
