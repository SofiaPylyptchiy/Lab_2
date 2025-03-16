import tkinter as tk

class SavingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Мета заощаджень")
        self.configure(bg="#000000")

        label = tk.Label(self, text="Введіть суму мети заощаджень:", bg="#000000", fg="#FFFFFF")
        label.pack(pady=10)

        savings_entry = tk.Entry(self)
        savings_entry.pack(pady=5)

        confirm_button = tk.Button(
            self, text="Підтвердити", 
            command=lambda: master.set_goal_amount(savings_entry.get(), self), 
            bg="#9400D3", fg="#FFFFFF", font=("Helvetica", 12, "bold")
        )
        confirm_button.pack(pady=10)
