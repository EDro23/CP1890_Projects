import tkinter as tk
from tkinter import ttk
import locale

locale.setlocale(locale.LC_ALL, '')

first_window = tk.Tk()
first_window.title("Future Value Calculator")
first_window.geometry("400x175")

frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack()

monthlyinvest_label = ttk.Label(frame, text="Monthly Investment:")
monthlyinvest_label.grid(row=0, column=0, sticky="e")
monthly_text = tk.StringVar()
monthly_entry = ttk.Entry(frame, width=25, textvariable=monthly_text)
monthly_entry.grid(row=0, column=1, sticky="w")

yearlyinvest_label = ttk.Label(frame, text="Yearly Interest Rate:")
yearlyinvest_label.grid(row=1, column=0, sticky="e")
yearly_text = tk.StringVar()
yearlyinvest_entry = ttk.Entry(frame, width=25, textvariable=yearly_text)
yearlyinvest_entry.grid(row=1, column=1, sticky="w")

years_label = ttk.Label(frame, text="Years:")
years_label.grid(row=2, column=0, sticky="e")
years_text = tk.StringVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(row=2, column=1, sticky="w")

future_v = ttk.Label(frame, text="Future Value:")
future_v.grid(row=3, column=0, sticky="e")
future_text = tk.StringVar()
future_entry = ttk.Entry(frame, width=25, textvariable=future_text, state="readonly")
future_entry.grid(row=3, column=1, sticky="w", columnspan=2)  # Set columnspan to span across both columns


def calculate_button():
    try:
        monthly_investment = float(monthly_text.get())
        yearly_interest_rate = float(yearly_text.get())
        years = int(years_text.get())

        future_value = 0
        for month in range(1, years * 12 + 1):
            future_value += monthly_investment
            future_value += ((future_value * (yearly_interest_rate / 12) / 100))

        formatted_future_value = locale.currency(future_value, grouping=True)  # Format with currency symbol and commas
        future_text.set(formatted_future_value)
    except ValueError:
        future_text.set("Invalid Input")


calcl_btn = ttk.Button(frame, text="Calculate", command=calculate_button)
calcl_btn.grid(row=4, column=0, sticky="e", padx=5, pady=5, columnspan=1)  # Set columnspan to span across both columns

button = ttk.Button(frame, text="Exit", command=first_window.destroy)
button.grid(row=4, column=0, sticky="e", padx=5, pady=5, columnspan=2)  # Set columnspan to span across both columns

first_window.mainloop()