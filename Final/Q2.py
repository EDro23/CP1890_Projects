import tkinter
from tkinter import messagebox
import csv


class PreferencesGUI:
    def __init__(self):
        """
        Initializes the GUI elements for the program
        """
        self.root = tkinter.Tk()
        self.root.title("Preferences")
        self.root.geometry("425x150")

        # GUI Elements
        self.name_label = tkinter.Label(self.root, text="Name:")
        self.name_required_label = tkinter.Label(self.root, text="Required.")
        self.name_required_label.grid(row=0, column=3, sticky=tkinter.W)
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tkinter.E)
        self.name_entry = tkinter.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tkinter.W)

        self.language_label = tkinter.Label(self.root, text="Language:")
        self.language_label.grid(row=1, column=0, padx=5, pady=5, sticky=tkinter.E)
        self.language_entry = tkinter.Entry(self.root)
        self.language_entry.grid(row=1, column=1, padx=5, pady=5)

        self.autosave_label = tkinter.Label(self.root, text="Auto Save Every X Minutes:")
        self.valid_int_label = tkinter.Label(self.root, text="Must be a valid integer.")
        self.valid_int_label.grid(row=2, column=3, padx=5, pady=5, sticky=tkinter.W)
        self.autosave_label.grid(row=2, column=0, padx=5, pady=5)
        self.autosave_entry = tkinter.Entry(self.root)
        self.autosave_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.save_button = tkinter.Button(self.root, text="Save", command=self.save_entry)
        self.save_button.grid(row=3, column=1, padx=5, pady=5, sticky="W")

        self.cancel_button = tkinter.Button(self.root, text="Cancel", command=self.root.destroy)
        self.cancel_button.grid(row=3, column=1, padx=5, pady=5, sticky="E")

    def save_entry(self):
        """
        Saves the entry to a CSV file when the user hits the save button.
        :return:
        """
        name = self.name_entry.get()
        language = self.language_entry.get()
        autosave = self.autosave_entry.get()

        # Check if any of the fields are empty
        if not all([name, language, autosave]):
            messagebox.showerror("Error", "All fields are required")
            return

        # Save entry to CSV
        with open('preferences.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, language, autosave])

        messagebox.showinfo("Success", "Entry saved to preferences.csv")


if __name__ == "__main__":
    """
    Main function of the program to run the GUI
    """
    preferences_gui = PreferencesGUI()
    preferences_gui.root.mainloop()
