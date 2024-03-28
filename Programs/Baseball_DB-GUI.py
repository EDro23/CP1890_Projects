import tkinter as tk
from tkinter import ttk


class BaseballGui:
    def __init__(self):
        self.gui = tk.Tk()  # Instantiate a Tk object
        self.gui.title("Player")
        self.gui.geometry("450x425")
        self.gui.resizable(False, False)

        self.frame = ttk.Frame(self.gui, padding="10 10 10 10")
        self.frame.pack()

        # PlayerID field

        self.playerID_label = ttk.Label(self.frame, text="Player ID: ")
        self.playerID_label.grid(row=0, column=0, sticky="w")

        self.playerID_text = tk.StringVar()
        self.playerID_entry = ttk.Entry(self.frame, width=25, textvariable=self.playerID_text)
        self.playerID_entry.grid(row=0, column=1, sticky="w")

        # First name field

        self.firstName_label = ttk.Label(self.frame, text="First name: ")
        self.firstName_label.grid(row=1, column=0, sticky="w")

        self.firstName_text = tk.StringVar()
        self.firstName_entry = ttk.Entry(self.frame, width=25, textvariable=self.firstName_text)
        self.firstName_entry.grid(row=1, column=1, sticky="w")

        # Last name field

        self.lastName_label = ttk.Label(self.frame, text="Last name: ")
        self.lastName_label.grid(row=2, column=0, sticky="w")

        self.lastName_text = tk.StringVar()
        self.lastName_entry = ttk.Entry(self.frame, width=25, textvariable=self.lastName_text)
        self.lastName_entry.grid(row=2, column=1, sticky="w")

        # Position field

        self.position_label = ttk.Label(self.frame, text="Position: ")
        self.position_label.grid(row=3, column=0, sticky="w")

        self.position_text = tk.StringVar()
        self.position_entry = ttk.Entry(self.frame, width=25, textvariable=self.position_text)
        self.position_entry.grid(row=3, column=1, sticky="w")

        # At bats field

        self.atBats_label = ttk.Label(self.frame, text="At bats: ")
        self.atBats_label.grid(row=4, column=0, sticky="w")

        self.atBats_text = tk.StringVar()
        self.atBats_entry = ttk.Entry(self.frame, width=25, textvariable=self.atBats_text)
        self.atBats_entry.grid(row=4, column=1, sticky="w")

        # Hits field

        self.hits_label = ttk.Label(self.frame, text="Hits: ")
        self.hits_label.grid(row=5, column=0, sticky="w")

        self.hits_text = tk.StringVar()
        self.hits_entry = ttk.Entry(self.frame, width=25, textvariable=self.hits_text)
        self.hits_entry.grid(row=5, column=1, sticky="w")

        # Batting avg field (Read-only)

        self.battingAvg_label = ttk.Label(self.frame, text="Hits: ")
        self.battingAvg_label.grid(row=6, column=0, sticky="w")

        self.battingAvg_text = tk.StringVar()
        self.battingAvg_entry = ttk.Entry(self.frame, width=25, textvariable=self.hits_text)
        self.battingAvg_entry.grid(row=6, column=1, sticky="w")

        # Save changes button
        self.savechanges_button = ttk.Button(self.frame, text="Save Changes")
        self.savechanges_button.grid(row=7, column=1, pady=10, sticky="w")

        # Cancel button
        self.cancel_button = ttk.Button(self.frame, text="Cancel")
        self.cancel_button.grid(row=7, column=1, pady=10, sticky="e")

        # Get player button
        self.cancel_button = ttk.Button(self.frame, text="Get Player")
        self.cancel_button.grid(row=0, column=3, pady=10, sticky="w")


def main():
    root = BaseballGui()
    root.gui.mainloop()  # Start the tkinter loop


if __name__ == "__main__":
    main()
