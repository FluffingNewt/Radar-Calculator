import formulas as f

import numpy
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import ScalarFormatter


##################################### Calculations ######################################

units_NMI  = ["NMI", "mi", "m", "ft"]
units_dBW  = ["dBW", "dBm", "W", "mW"]
units_rcs  = ["m\u00B2"]
units_GHz  = ["GHz", "MHz", "Hz", "kHz"]

def calculate_and_plot():
    # Check if all text fields have valid inputs
    error = False
    for entry in root.winfo_children():
        if isinstance(entry, tkinter.Entry) and not isinstance(entry, ttk.Combobox):
            if entry.grid_info()["row"] == 7 and entry.grid_info()["column"] == 1:
                continue
            elif not validate_entry(entry):
                error = True
    
    if error:
        print('input error at "invalid input" values')
        return

    root.focus_set()

    # Variable setup
    pwr_t  = f.convert_to_W(pwr_t_entry.get(), pwr_t_unit.get())
    gain_t = float(gain_t_entry.get())
    gain_r = float(gain_r_entry.get())
    freq   = f.convert_to_Hz(freq_entry.get(), freq_unit.get())
    rcs    = float(rcs_entry.get())
    pwr_r_values = []

    # Convert range to expected x-unit
    if   plot_x_unit.get() == "NMI":
        range  = f.convert_to_NMI(range_entry.get(), range_unit.get())
        r_unit = "NMI"
    elif plot_x_unit.get() == "mi":
        range  = f.convert_to_mi(range_entry.get(), range_unit.get())
        r_unit = "mi"
    elif plot_x_unit.get() == "ft":
        range  = f.convert_to_ft(range_entry.get(), range_unit.get())
        r_unit = "ft"
    else:
        range  = f.convert_to_m(range_entry.get(), range_unit.get())
        r_unit = "m"

    range_values = numpy.linspace(1, range, 400)

    # Calculate [range, pwr_r] pairs
    for r in range_values:
        pwr_r = f.rre_pr(pwr_t, gain_t, gain_r, freq, rcs, f.convert_to_m(r, r_unit))

        if plot_y_unit.get() == "dBW":
            pwr_r  = f.convert_to_dBW(pwr_r, "W")
        elif plot_y_unit.get() == "dBm":
            pwr_r  = f.convert_to_dBm(pwr_r, "W")
        elif plot_y_unit.get() == "mW":
            pwr_r  = f.convert_to_mW(pwr_r,  "W")
        
        pwr_r_values.append(pwr_r)

    # Log output calculation
    print(f"\nPr = {pwr_r_values[len(pwr_r_values) - 1]} {plot_y_unit.get()}")

    # Clear, initialize, and plot graph
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(range_values, pwr_r_values, label="Received Power")
    # ax.plot(range, 10 * numpy.log10(pwr_n), label="Noise Jammer")
    # ax.plot(range, 10 * numpy.log10(P_range_j), label="Repeater Jammer")
    ax.set_xlabel(f"Range ({plot_x_unit.get()})")
    ax.set_ylabel(f"Received Power {plot_y_unit.get()}")
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.legend(loc="upper right")
    pwr_r_entry.delete(0, tkinter.END)
    pwr_r_entry.insert(0, f"{pwr_r_values[len(pwr_r_values) - 1]:.4f}")
    canvas.draw()


###################################### GUI Setup ########################################

def validate_entry(entry):
    value = entry.get()
    if not value or \
        value == "0" or \
        value == "0.0" or \
        any(char.isalpha() for char in value) or \
        any(char in value for char in "[$&+,:;=?@#|'\"<>-_^*()%!]") or \
        ("." in value and value == "."):
            entry.delete(0, tkinter.END)
            entry.insert(0, "invalid input")
            entry.config(fg="red")
            return False
    
    entry.config(fg="black")
    return True

def reset_entry(event, entry):
    if (entry.get() == "invalid input") or (entry.get() == "1"):
        entry.delete(0, tkinter.END)
        entry.config(fg="black")

def create_label(root, text, row, column, font, padx=10, pady=10, sticky="w"):
    label = tkinter.Label(root, text=text, font=font)
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return label

def create_entry(root, row, column, default_value=1, pady=10):
    entry = tkinter.Entry(root)
    entry.grid(row=row, column=column, pady=pady)
    entry.insert(0, default_value)
    entry.bind("<FocusIn>", lambda event: reset_entry(event, entry))
    return entry

def create_combobox(root, textvariable, values, row, column, font, width=6, pady=10):
    combobox = ttk.Combobox(root, textvariable=textvariable, values=values, font=font, state="readonly", width=width)
    combobox.grid(row=row, column=column, pady=pady)
    return combobox

# Root
root = tkinter.Tk()
root.title("Radar Range Equation Calculator")
default_font = ('Product Sans', 13)

# Power Transmitted
create_label(root, "Pt : Power Transmitted", 0, 0, default_font)
pwr_t_entry = create_entry(root, 0, 1)
pwr_t_unit = tkinter.StringVar(value="dBW")
create_combobox(root, pwr_t_unit, units_dBW, 0, 2, default_font)

# Gain Transmitted
create_label(root, "Gt : Gain Transmitted", 1, 0, default_font)
gain_t_entry = create_entry(root, 1, 1)

# Gain Received
create_label(root, "Gr : Gain Received", 2, 0, default_font)
gain_r_entry = create_entry(root, 2, 1)

# Frequency
create_label(root, "\u03BD : Frequency", 3, 0, default_font)
freq_entry = create_entry(root, 3, 1)
freq_unit = tkinter.StringVar(value="GHz")
create_combobox(root, freq_unit, units_GHz, 3, 2, default_font)

# RCS
create_label(root, "\u03C3 : Radar Cross Section", 4, 0, default_font)
rcs_entry = create_entry(root, 4, 1)
rcs_unit = tkinter.StringVar(value="m\u00B2")
create_combobox(root, rcs_unit, units_rcs, 4, 2, default_font)

# Range
create_label(root, "R : Range", 5, 0, default_font)
range_entry = create_entry(root, 5, 1)
range_unit = tkinter.StringVar(value="NMI")
create_combobox(root, range_unit, units_NMI, 5, 2, default_font)

# Plot Button
btn_plot = tkinter.Button(root, text="Plot", command=calculate_and_plot, font=default_font)
btn_plot.grid(row=7, column=3, sticky="e")

# x Unit
plot_x_unit = tkinter.StringVar(value="NMI")
create_label(root, "x Unit", 4, 3, default_font, sticky="w")
create_combobox(root, plot_x_unit, units_NMI, 4, 4, default_font)

# y Unit
plot_y_unit = tkinter.StringVar(value="dBW")
create_label(root, "y Unit", 5, 3, default_font, sticky="w")
create_combobox(root, plot_y_unit, units_dBW, 5, 4, default_font)

# Power Received
create_label(root, "", 6, 0, default_font, 0, 0)
create_label(root, "Pr : Power Received", 7, 0, default_font, padx=10, pady=10)
pwr_r_entry = create_entry(root, 7, 1, "")
pwr_r_unit = tkinter.StringVar(value="")
create_combobox(root, pwr_r_unit, units_dBW, 7, 2, default_font)

# Matplotlib figure setup
fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=9, columnspan=5)

ax = fig.add_subplot(111)
ax.plot(1, 1, label="Received Power")
ax.plot(0, 0, label="Noise Jammer")
ax.plot(0, 0, label="Repeater Jammer")
ax.legend(loc="upper right")
canvas.draw()

ax.set_xlabel(f"Range ({plot_x_unit.get()})")
ax.set_ylabel(f"Received Power {plot_y_unit.get()}")

root.mainloop()