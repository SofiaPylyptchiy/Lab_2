import tkinter as tk

class ExpenseDetailsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Детальна інформація про витрати")
        self.configure(bg="#000000")

        for category, expenses in master.expense_details.items():
            text = f"{category}: {sum(expenses):.2f} {master.currency.get()}" if expenses else f"{category}: -"
            label = tk.Label(self, text=text, bg="#000000", fg="#FFFFFF", font=("Helvetica", 12))
            label.pack(pady=5)
