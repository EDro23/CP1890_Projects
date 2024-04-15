# Triangle side calculator
from tkinter import ttk
import tkinter as tk
from dataclasses import dataclass


@dataclass
class TriangleGUI:
    """
    Triangle GUI for a triangle calculator program
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Right Triangle Calculator")
        self.root.geometry("300x125")

        # GUI Elements
        self.sideA_label = ttk.Label(root, text="Side A:")
        self.sideA_entry = ttk.Entry(root)
        self.sideB_label = ttk.Label(root, text="Side B:")
        self.sideB_entry = ttk.Entry(root, )
        self.sideC_label = ttk.Label(root, text="Side C:")
        self.sideC_entry = ttk.Entry(root, state="disabled")
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_triangle)
        self.exit_button = ttk.Button(root, text="Exit", command=root.quit)

        # GUI Grid
        self.sideA_label.grid(row=0, column=0, padx=5, pady=5)
        self.sideA_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=5, ipadx="50")
        self.sideB_label.grid(row=1, column=0, padx=5, pady=5)
        self.sideB_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=5, ipadx="50")
        self.sideC_label.grid(row=2, column=0, padx=5, pady=5)
        self.sideC_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=5, ipadx="50")
        self.calculate_button.grid(row=4, column=4, sticky=tk.W)
        self.exit_button.grid(row=4, column=5, sticky=tk.E)

    def calculate_triangle(self):
        """
        Method that calculates the triangle side A and side B and gets the result of side C
        :return: Side C in the field.
        """
        side_a = int(self.sideA_entry.get())
        side_b = int(self.sideB_entry.get())
        side_a_squared = side_a ** 2
        side_b_squared = side_b ** 2
        side_c_squared = side_a_squared + side_b_squared
        side_c = side_c_squared ** 0.5
        self.sideC_entry.config(state="normal")  # Enable entry field
        self.sideC_entry.delete(0, tk.END)  # Delete
        self.sideC_entry.insert(0, f"{side_c:.3f}")  # Insert
        self.sideC_entry.config(state="disabled")  # Disable entry field again


if __name__ == '__main__':
    root = tk.Tk()
    app = TriangleGUI(root)
    root.mainloop()
