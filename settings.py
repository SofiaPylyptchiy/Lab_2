import tkinter as tk

class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Налаштування")
        self.configure(bg="#000000")

        label_currency = tk.Label(self, text="Виберіть валюту:", bg="#000000", fg="#FFFFFF")
        label_currency.pack(pady=5)

        currency_options = ["грн", "$", "€"]
        currency_menu = tk.OptionMenu(self, master.currency, *currency_options)
        currency_menu.configure(bg="#9400D3", fg="#FFFFFF", font=("Helvetica", 10))
        currency_menu.pack(pady=5)

        save_button = tk.Button(self, text="Зберегти", command=self.destroy, bg="#9400D3", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        save_button.pack(pady=10)
