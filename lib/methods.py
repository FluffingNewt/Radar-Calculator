import tkinter
from tkinter import ttk

default_font = ('Arial', 12)
bold_font    = ("Arial", 12, "bold")

def validate_entries(tab, column, rowStart, rowStop, type):
            blank_entries = []
            error_found = False

            alpha_chars = "abcdfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            special_chars = "[$&,:;=?@#|'\"<>_^*()%!]"

            for child in tab.winfo_children():

                if isinstance(child, tkinter.Entry):

                    info = child.grid_info()

                    if info['column'] == column and info['row'] >= rowStart and info['row'] <= rowStop:
                        value = child.get()

                        if any(char in value for char in alpha_chars) or \
                           any(char in value for char in special_chars) or \
                           value in ["0", "0.0"]:
                                
                            print(f"Error: Invalid input '{value}' in row {info['row']}")
                            child.delete(0, tkinter.END)
                            child.insert(0, "invalid input")
                            child.config(fg="red")
                            error_found = True

                        elif value == "":
                            blank_entries.append(child)
            
            if type == "unam_r"      and len(blank_entries) == 2 or \
               type == "doppler"     and len(blank_entries) == 4 or \
               type in ["pr", "log"] and len(blank_entries) == 7 or \
               type in ["nj", "rj"]  and len(blank_entries) == 9:
                
                error_found = True

            elif len(blank_entries) > 1:
                for entry in blank_entries:
                    entry.delete(0, tkinter.END)
                    entry.insert(0, "invalid input")
                    entry.config(fg="red")
                    
                error_found = True
                print('Error: Blank lines detected')

            return error_found

def reset_entry(event, entry):
    if entry.get() in ["invalid input", "error"]:
        entry.delete(0, tkinter.END)
        entry.config(fg="black")

def create_entry(self, row, column, padx=0 , pady=10):
            entry = tkinter.Entry(self)
            entry.grid(row=row, column=column, padx=padx, pady=pady, sticky="ew")
            entry.bind("<FocusIn>", lambda event: reset_entry(event, entry))
            return entry

def create_label(self, text, row, column, padx=10, pady=5, sticky="w", columnspan=1):
    label = tkinter.Label(self, text=text, font=bold_font)
    label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return label

def create_combobox(self, textvariable, values, row, column, width=6, pady=10, sticky=""):
    combobox = ttk.Combobox(self, textvariable=textvariable, values=values, font=default_font, state="readonly", width=width)
    combobox.grid(row=row, column=column, pady=pady, sticky=sticky)
    return combobox

def create_separator(self, orient, row, column, padx=0, pady=0, rowspan=1, columnspan=1):
    separator = ttk.Separator(self, orient=orient)
    if orient == "horizontal" : separator.grid(row=row, column=column, rowspan=rowspan ,columnspan=columnspan , sticky="ew", padx=padx, pady=pady)
    else                      : separator.grid(row=row, column=column, rowspan=rowspan ,columnspan=columnspan , sticky="nsw", padx=padx, pady=pady)
    
