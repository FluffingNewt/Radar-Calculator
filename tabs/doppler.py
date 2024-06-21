import formulas as f
import numpy
import tkinter
from tkinter import ttk


class Tab3(tkinter.Frame):

    default_font = ('Arial', 12)
    bold_font    = ("Arial", 12, "bold")


    def __init__(self, parent):
        super().__init__(parent)

        def validate_entries(column):
            blank_entries = []
            error_found = False

            special_chars = "[$&+,:;=?@#|'\"<>_^*()%!]"

            # Loop through all children of the self window
            for child in self.winfo_children():
                if isinstance(child, tkinter.Entry):
                    info = child.grid_info()
                    if info['column'] == column and info['row'] <= 12:
                        value = child.get()

                        if any(char.isalpha() for char in value) or \
                        any(char in value for char in special_chars) or \
                        value in ["0", "0.0"]:
                            print(f"Error: Invalid input '{value}' in row {info['row']}")
                            child.delete(0, tkinter.END)
                            child.insert(0, "invalid input")
                            child.config(fg="red")
                            error_found = True
                        elif value == "":
                            blank_entries.append(child)

            
            if (column == 1 and len(blank_entries) == 7) or (column in [3, 5] and len(blank_entries) == 9):
                error_found = True
            elif len(blank_entries) > 1:
                for entry in blank_entries:
                    entry.delete(0, tkinter.END)
                    entry.insert(0, "invalid input")
                    entry.config(fg="red")
                error_found = True

            return error_found


        def reset_entry(event, entry):
            if entry.get() == "invalid input":
                entry.delete(0, tkinter.END)
                entry.config(fg="black")


        def create_label(self, text, row, column, padx=10, pady=5, sticky="w", columnspan=1):
            label = tkinter.Label(self, text=text, font=Tab4.bold_font)
            label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
            return label


        def create_entry(self, row, column, padx=0 , pady=10):
            entry = tkinter.Entry(self)
            entry.grid(row=row, column=column, padx=padx, pady=pady, sticky="w")
            entry.bind("<FocusIn>", lambda event: reset_entry(event, entry))
            return entry

        def create_combobox(self, textvariable, values, row, column, width=6, pady=10, sticky=""):
            combobox = ttk.Combobox(self, textvariable=textvariable, values=values, font=Tab4.default_font, state="readonly", width=width)
            combobox.grid(row=row, column=column, pady=pady, sticky=sticky)
            return combobox

        def create_separator(self, orient, row, column, padx=0, pady=0):
            separator = ttk.Separator(self, orient=orient)
            if orient == "horizontal" : separator.grid(row=row, column=column, rowspan=1 ,columnspan=10 , sticky="ew", padx=padx, pady=pady)
            else                      : separator.grid(row=row, column=column, rowspan=14 ,columnspan=1 , sticky="nsw", padx=padx, pady=pady)
            
        
        row = 0
        col = 0
        create_label(self, "Doppler Theorem", row, col)

        row = 1
        col = 0
        create_separator(self, "horizontal", row, col, 0)

        row = 2
        col = 0
        create_label(self, "V : Shooter-Target Closing Velocity", row, col)
        v_entry = create_entry(self, row, col+1, 10)
        v_unit = tkinter.StringVar(value="m/s")
        create_combobox(self, v_unit, f.units_vel, row, col+2)

        row = 3
        col = 0
        create_label(self, "ft : Transmit Frequency", row, col)
        ft_entry = create_entry(self, row, col+1, 10)
        ft_unit = tkinter.StringVar(value="GHz")
        create_combobox(self, ft_unit, f.units_GHz, row, col+2)
