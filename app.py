import math
import tkinter
from tkinter import ttk
import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.ticker import ScalarFormatter


#################################### Default Values #####################################


units_NMI   = ["NMI", "mi", "m", "ft"]
units_dBW   = ["dBW", "dBm", "W", "mW"]
units_rcs  = ["m\u00B2"]
units_GHz  = ["GHz", "MHz", "Hz", "kHz"]


##################################### Calculations ######################################
"""
        Pt * Gt * Gr * λ^2 * σ
Pr = ---------------------------
            (4π)^3 * R^4

pwr_r      = Power Received (dBW)
pwr_t      = Power Transmitted (dBW)
gain_t     = Gain Transmitted
gain_r     = Gain Received
wavelength = Wavelength (NMI)
rcs        = Radar Cross-Section (NMI^2)
range      = Range (NMI)

"""

def radar_range_equation(pwr_t, gain_t, gain_r, freq, rcs, range):
    wavelength = convert_to_wavelength(freq, freq_unit)
    numer = pwr_t * gain_t * gain_r * math.pow(wavelength, 2) * rcs
    denom = math.pow(4 * np.pi, 3) * math.pow(range, 4)
    return numer / denom

def convert_to_NMI(value, unit):
    if  unit == "mi"  : return value * 0.868976242
    elif unit == "m"  : return value / 1852
    elif unit == "ft" : return value * (1.64578834 * 10e-4)
    else              : return value # Passthrough

def convert_to_mi(value, unit):
    if   unit == "NMI" : return value * 1.15078
    elif unit == "m"   : return value * 6.21e-4
    elif unit == "ft"  : return value / 5280
    else               : return value # Passthrough

def convert_to_m(value, unit):
    if   unit == "NMI"  : return value * 1852
    elif unit == "mi" : return value * 1609.344
    elif unit == "ft" : return value * 0.3048
    else              : return value # Passthrough

def convert_to_ft(value, unit):
    if   unit == "NMI" : return value * 6076.12
    elif unit == "mi"  : return value * 5280 
    elif unit == "m"   : return value * 3.28084
    else               : return value # Passthrough

def convert_to_dBW(value, unit):
    if   unit == "dBm" : return value - 30.0
    elif unit == "W"   : return 10 * math.log10(value)
    elif unit == "mW"  : return 10 * math.log10(value / 1000)
    else               : return value # Passthrough

def convert_to_dBm(value, unit):
    if   unit == "dBW" : return value + 30.0
    elif unit == "W"   : return 10 * math.log10(value * 1000)
    elif unit == "mW"  : return 10 * math.log10(value / 1000)
    else               : return value # Passthrough

def convert_to_W(value, unit):
    if   unit == "dBW" : return math.pow(10, value / 10)
    elif unit == "dBm" : return math.pow(10, value / 10) / 1000
    elif unit == "mW"  : return float(value / 1000)
    else               : return float(value)  # Passthrough, ensure it's a float

def convert_to_mW(value, unit):
    if unit != "mW" : return convert_to_W(value, unit) * 1000
    else            : return float(value)  # Passthrough, ensure it's a float

def convert_to_Hz(value, unit):
    if   unit == "GHz" : return float(value * 1e9)
    elif unit == "MHz" : return float(value * 1e6)
    elif unit == "kHz" : return float(value * 1e3)
    else               : return float(value) # Passthrough

def convert_to_wavelength(freq, unit):
    c = 299792458.0   # Speed of light (m/s)
    freq = convert_to_Hz(freq, unit)
    return c / freq

def validate_entry(entry):
    value = entry.get()
    if not value or float(value) == 0:
        entry.delete(0, tkinter.END)
        entry.insert(0, "invalid input")
        entry.config(fg="red")
        return False
    entry.config(fg="black")
    return True

def reset_entry(event, entry):
    if entry.get() == "invalid input" or float(entry.get()) == 1:
        entry.delete(0, tkinter.END)
        entry.config(fg="black")
    return

def calculate_and_plot():
    ### Calculations ###
    print("\n*** LOGGED CALCULATION: ***\n")

    ### Unfocus text boxes after calculations ###
    root.focus_set()
    error = False
    for entry in root.winfo_children():
        if isinstance(entry, tkinter.Entry) and not isinstance(entry, ttk.Combobox):
            if not validate_entry(entry):
                error = True
    
    if error:
        print("input error at \"invalid input\" values")
        return

    # if not (validate_entry(pwr_t_entry)  and
    #         validate_entry(gain_t_entry) and
    #         validate_entry(gain_r_entry) and
    #         validate_entry(freq_entry)   and
    #         validate_entry(rcs_entry)    and
    #         validate_entry(range_entry)):
    #     print("input error")
    #     return

    print(f"       {float(pwr_t_entry.get())} {pwr_t_unit.get()} * {float(gain_t_entry.get())} * {float(gain_r_entry.get())} * (c / {float(freq_entry.get())} {freq_unit.get()})^2 * {float(rcs_entry.get())} {rcs_unit.get()}")
    print(f"Pr = ---------------------------------------------")
    print(f"              (4pi)^3 * ({float(range_entry.get())} {range_unit.get()})^4")


    pwr_t  = convert_to_W(float(pwr_t_entry.get()), pwr_t_unit.get())
    pwr_t_unit.set("W")
    gain_t = float(gain_t_entry.get())
    gain_r = float(gain_r_entry.get())
    freq   = convert_to_Hz(float(freq_entry.get()), freq_unit.get())
    freq_unit.set("Hz")
    rcs    = float(rcs_entry.get())


    if plot_x_unit.get() == "NMI":
        range  = convert_to_NMI(float(range_entry.get()), range_unit.get())
        r_unit = "NMI"
    elif plot_x_unit.get() == "mi":
        range  = convert_to_mi(float(range_entry.get()), range_unit.get())
        r_unit = "mi"
    elif plot_x_unit.get() == "ft":
        range  = convert_to_ft(float(range_entry.get()), range_unit.get())
        r_unit = "ft"
    else:
        range  = convert_to_m(float(range_entry.get()), range_unit.get())
        r_unit = "m"

    range_values = np.linspace(1, range, 100)
    pwr_r_values = []

    for r in range_values:
        pwr_r = radar_range_equation(pwr_t, gain_t, gain_r, freq, rcs, convert_to_m(r, r_unit))

        if plot_y_unit.get() == "dBW":
            pwr_r  = convert_to_dBW(pwr_r, "W")
        elif plot_y_unit.get() == "dBm":
            pwr_r  = convert_to_dBm(pwr_r, "W")
        elif plot_y_unit.get() == "mW":
            pwr_r  = convert_to_mW(pwr_r,  "W")
        
        pwr_r_values.append(pwr_r)

    print(f"\n   = {pwr_r_values[len(pwr_r_values) - 1]} {plot_y_unit.get()}")

    print(f"\n----------------------------------------------------------------")

    ### Plot ###
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(range_values, pwr_r_values, label="Received Power")
    # ax.plot(range, 10 * np.log10(pwr_n), label="Noise Jammer")
    # ax.plot(range, 10 * np.log10(P_range_j), label="Repeater Jammer")
    ax.set_xlabel(f"Range ({plot_x_unit.get()})")
    ax.set_ylabel(f"Received Power {plot_y_unit.get()}")
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.legend()
    canvas.draw()

###################################### GUI Setup ########################################


root = tkinter.Tk()
root.title("Radar Range Equation Calculator")
default_font = ('Product Sans', 13)

# Power Transmitted
tkinter.Label(root,
         text="Pt : Power Transmitted",
         font=default_font
        ).grid(row=0, column=0, sticky="w", padx=10, pady=10)
pwr_t_entry = tkinter.Entry(root)
pwr_t_entry.grid(row=0, column=1, pady=10)
pwr_t_entry.insert(0, 1)
pwr_t_entry.bind("<FocusIn>", lambda event: reset_entry(event, pwr_t_entry))

pwr_t_unit = tkinter.StringVar()
pwr_t_unit.set("dBW")
pwr_t_unit_menu = ttk.Combobox(root,
                               textvariable=pwr_t_unit,
                               values=units_dBW,
                               font=default_font,
                               state="readonly",
                               width=6
                               )
pwr_t_unit_menu.grid(row=0, column=2, pady=10)

###############################################

# Gain Transmitted
tkinter.Label(root,
         text="Gt : Gain Transmitted",
         font=default_font
        ).grid(row=1, column=0, sticky="w", padx=10, pady=10)
gain_t_entry = tkinter.Entry(root)
gain_t_entry.grid(row=1, column=1, pady=10)
gain_t_entry.insert(0, 1)
gain_t_entry.bind("<FocusIn>", lambda event: reset_entry(event, gain_t_entry))

###############################################

# Gain Received
tkinter.Label(root,
         text="Gr : Gain Received",
         font=default_font
        ).grid(row=2, column=0, sticky="w", padx=10, pady=10)
gain_r_entry = tkinter.Entry(root)
gain_r_entry.grid(row=2, column=1, pady=10)
gain_r_entry.insert(0, 1)
gain_r_entry.bind("<FocusIn>", lambda event: reset_entry(event, gain_r_entry))

###############################################

# Frequency
tkinter.Label(root,
         text="\U0001D453 : Frequency",
         font=default_font
        ).grid(row=3, column=0, sticky="w", padx=10, pady=10)
freq_entry = tkinter.Entry(root)
freq_entry.grid(row=3, column=1, pady=10)
freq_entry.insert(0, 1)
freq_entry.bind("<FocusIn>", lambda event: reset_entry(event, freq_entry))
freq_unit = tkinter.StringVar()
freq_unit.set("GHz")
freq_unit_menu = ttk.Combobox(root,
                              textvariable=freq_unit,
                              values=units_GHz,
                              font=default_font,
                              state="readonly",
                              width=6)
freq_unit_menu.grid(row=3, column=2, pady=10)

###############################################

# RCS
tkinter.Label(root,
         text="\u03C3 : Radar Cross Secion",
         font=default_font
        ).grid(row=4, column=0, sticky="w", padx=10, pady=10)
rcs_entry = tkinter.Entry(root)
rcs_entry.grid(row=4, column=1, pady=10)
rcs_entry.insert(0, 1)
rcs_entry.bind("<FocusIn>", lambda event: reset_entry(event, rcs_entry))
rcs_unit = tkinter.StringVar()
rcs_unit.set("m\u00B2")
rcs_unit_menu = ttk.Combobox(root,
                             textvariable=rcs_unit,
                             values=units_rcs,
                             font=default_font,
                             state="readonly",
                             width=6
                             )
rcs_unit_menu.grid(row=4, column=2, pady=10)

###############################################

# Range
tkinter.Label(root,
         text="R : Range",
         font=default_font
        ).grid(row=5, column=0, sticky="w", padx=10, pady=10)
range_entry = tkinter.Entry(root)
range_entry.grid(row=5, column=1, pady=10)
range_entry.insert(0, 1)
range_entry.bind("<FocusIn>", lambda event: reset_entry(event, range_entry))
range_unit = tkinter.StringVar()
range_unit.set("NMI")
range_unit_menu = ttk.Combobox(root,
                               textvariable=range_unit,
                               values=units_NMI,
                               font=default_font,
                               state="readonly",
                               width=6
                              )
range_unit_menu.grid(row=5, column=2, pady=10)

tkinter.Label(root, text="").grid(row=6, columnspan=5)

###############################################

# Plot button
btn_plot = tkinter.Button(root, text="Plot", command=calculate_and_plot, font=default_font)
btn_plot.grid(row=5, column=4, sticky="w")

###############################################

# x Unit
plot_x_unit = tkinter.StringVar()
plot_x_unit.set("NMI")
tkinter.Label(root,
              text="   x Unit",
              font=default_font
              ).grid(row=3, column=3, sticky="w")

plot_x_unit_menu = ttk.Combobox(root,
                                textvariable=plot_x_unit,
                                values=units_NMI,
                                font=default_font,
                                state="readonly",
                                width=6)
plot_x_unit_menu.grid(row=3, column=4, sticky="w")

###############################################

# y Unit
plot_y_unit = tkinter.StringVar()
plot_y_unit.set("dBW")
tkinter.Label(root,
         text="   y Unit",
         font=default_font
        ).grid(row=4, column=3, sticky="w")

plot_y_unit_menu = ttk.Combobox(root,
                               textvariable=plot_y_unit,
                               values=units_dBW,
                               font=default_font,
                               state="readonly",
                               width=6)
plot_y_unit_menu.grid(row=4, column=4, sticky="w")

###############################################




###################################### App Loop ########################################

# Matplotlib figure setup
fig = pyplot.Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=8, columnspan=5)

ax = fig.add_subplot(111)
ax.plot(190, 1, label="Received Power")
ax.plot(190, 1, label="Noise Jammer")
ax.plot(190, 1, label="Repeater Jammer")
ax.legend()
canvas.draw()

ax.set_xlabel(f"Range ({plot_x_unit.get()})")
ax.set_ylabel(f"Received Power {plot_y_unit.get()}")

root.mainloop()