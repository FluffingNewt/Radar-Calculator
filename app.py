import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


#################################### Default Values #####################################


units_NMI   = ["NMI", "m", "mi", "ft"]
units_dBW   = ["dBW", "dBm", "W", "mW"]
units_rcs  = ["NMI\u00B2", "m\u00B2", "mi\u00B2", "ft\u00B2"]
units_GHz  = ["GHz", "MHz", "kHz", "Hz"]


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
    wavelength = convert_to_NMI(convert_to_wavelength(freq, freq_unit), "m")
    numer = pwr_t * gain_t * gain_r * math.pow(wavelength, 2) * rcs
    denom = math.pow(4 * np.pi, 3) * math.pow(range, 4)
    return numer / denom

def convert_to_NMI(value, unit):
    if   unit == "m"  : return value / 1852
    elif unit == "mi" : return value * 0.868976242
    elif unit == "ft" : return value * (1.64578834 * math.pow(10, -4))
    else              : return value # Passthrough

def convert_to_NMI2(value, unit):
    if   unit == "m\u00B2"  : return value * (2.915533496 * math.pow(10, -7))
    elif unit == "mi\u00B2" : return value * 1.3242933
    elif unit == "ft\u00B2" : return value * (2.70861925 * math.pow(10, -8))
    else                    : return value # Passthrough

def convert_to_dBW(value, unit):
    if   unit == "dBm" : return value - 30.0
    elif unit == "W"   : return 10 * math.log10(value)
    elif unit == "mW"  : return 10 * math.log10(value / 1000)
    else               : return value # Passthrough

def convert_to_Hz(value, unit):
    if   unit == "GHz" : return value * math.pow(10, 9)
    elif unit == "MHz" : return value * math.pow(10, 6)
    elif unit == "kHz" : return value * 1000
    else               : return value # Passthrough

def convert_to_wavelength(freq, unit):
    c = 299792458   # Speed of light (m/s)
    freq = convert_to_Hz(freq, unit)
    return c / freq

def calculate_and_plot():
    print("\n*** Power Received Calculation ***\n")
    print("BEFORE:")
    print("------")
    print(f"pwr_t    :  {float(pwr_t_entry.get())}   {pwr_t_unit.get()}")
    print(f"gain_t   :  {float(gain_t_entry.get())}")
    print(f"gain_r   :  {float(gain_r_entry.get())}")
    print(f"freq     :  {float(freq_entry.get())}    {freq_unit.get()}")
    print(f"rcs      :  {float(rcs_entry.get())}     {rcs_unit.get()}")
    print(f"range    :  {float(range_entry.get())}   {range_unit.get()}")
    print("\n------------------------------\n")

    pwr_t = convert_to_dBW(float(pwr_t_entry.get()), pwr_t_unit.get())
    gain_t = float(gain_t_entry.get())
    gain_r = float(gain_r_entry.get())
    freq  = convert_to_Hz(float(freq_entry.get()), freq_unit.get())
    rcs    = convert_to_NMI2(float(rcs_entry.get()), rcs_unit.get())
    range  = convert_to_NMI(float(range_entry.get()), range_unit.get())
    pwr_r = radar_range_equation(pwr_t, gain_t, gain_r, freq, rcs, range)

    print("AFTER:")
    print("------")
    print(f"pwr_t    :  {pwr_t}")
    print(f"gain_t   :  {gain_t}")
    print(f"gain_r   :  {gain_r}")
    print(f"wave     :  {convert_to_NMI(convert_to_wavelength(freq, freq_unit), "m")}")
    print(f"rcs      :  {rcs}")
    print(f"range    :  {range}")
    print("------------------------------")
    print(f"pwr_r      :  {pwr_r}")
    
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(range, 10 * np.log10(pwr_r), label="Received Power")
    # ax.plot(range, 10 * np.log10(pwr_n), label="Noise Jammer")
    # ax.plot(range, 10 * np.log10(P_range_j), label="Repeater Jammer")
    ax.set_xlabel(f"Range ({range_unit.get()})")
    ax.set_ylabel('Received Power (dBW)')
    ax.legend()
    canvas.draw()


###################################### GUI Setup ########################################


root = tk.Tk()
root.title("Radar Range Equation Calculator")
default_font = ('Product Sans', 13)


# Power Transmitted
tk.Label(root,
         text="Pt : Power Transmitted",
         font=default_font
        ).grid(row=0, column=0)
pwr_t_entry = tk.Entry(root)
pwr_t_entry.grid(row=0, column=1)
pwr_t_unit = tk.StringVar()
pwr_t_unit.set("dBW")
pwr_t_unit_menu = ttk.Combobox(root,
                               textvariable=pwr_t_unit,
                               values=units_dBW,
                               font=default_font,
                               state="readonly",
                               width=6
                               )
pwr_t_unit_menu.grid(row=0, column=2)

###############################################

# Gain Transmitted
tk.Label(root,
         text="Gt : Gain Transmitted",
         font=default_font
        ).grid(row=1, column=0)
gain_t_entry = tk.Entry(root)
gain_t_entry.grid(row=1, column=1)

###############################################

# Gain Received
tk.Label(root,
         text="Gr : Gain Received",
         font=default_font
        ).grid(row=2, column=0)
gain_r_entry = tk.Entry(root)
gain_r_entry.grid(row=2, column=1)

###############################################

# Frequency
tk.Label(root,
         text="\u03BB : Frequency",
         font=default_font
        ).grid(row=3, column=0)
freq_entry = tk.Entry(root)
freq_entry.grid(row=3, column=1)
freq_unit = tk.StringVar()
freq_unit.set("GHz")
freq_unit_menu = ttk.Combobox(root,
                              textvariable=freq_unit,
                              values=units_GHz,
                              font=default_font,
                              state="readonly",
                              width=6
                              )
freq_unit_menu.grid(row=3, column=2)

###############################################

# RCS
tk.Label(root,
         text="\u03C3 : Radar Cross Secion",
         font=default_font
        ).grid(row=4, column=0)
rcs_entry = tk.Entry(root)
rcs_entry.grid(row=4, column=1)
rcs_unit = tk.StringVar()
rcs_unit.set("m\u00B2")
rcs_unit_menu = ttk.Combobox(root,
                             textvariable=rcs_unit,
                             values=units_rcs,
                             font=default_font,
                             state="readonly",
                             width=6
                             )
rcs_unit_menu.grid(row=4, column=2)

###############################################

# Range
tk.Label(root,
         text="R : Range",
         font=default_font
        ).grid(row=5, column=0)
range_entry = tk.Entry(root)
range_entry.grid(row=5, column=1)
range_unit = tk.StringVar()
range_unit.set("NMI")
range_unit_menu = ttk.Combobox(root,
                               textvariable=range_unit,
                               values=units_NMI,
                               font=default_font,
                               state="readonly",
                               width=6)
range_unit_menu.grid(row=5, column=2)

# Plot button
btn_plot = tk.Button(root, text="Plot", command=calculate_and_plot, font=default_font)
btn_plot.grid(row=9, columnspan=2)

# Matplotlib figure setup
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=10, columnspan=5)

root.mainloop()









