import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#################################### Default Values #####################################

units_NMI   = ["NMI", "m", "mi", "ft"]
units_dBw   = ["dBw", "dBm", "W", "mW"]
units_rcs  = ["m\u00B2"]
units_GHz  = ["GHz", "MHz", "kHz", "Hz"]

k = 1.380649 * math.pow(10, -23)    # Boltzmann constant (J/K)

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
pwr_t_unit.set("dBw")
pwr_t_unit_menu = ttk.Combobox(root,
                               textvariable=pwr_t_unit,
                               values=units_dBw,
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

# Wavelength
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


##################################### Calculations ######################################

#                pwr_t * gain_t * gain_r * wavelength^2 * rcs
#       pwr_r = ------------------------------------------------
#                             (4π)^3 * range^4

# pwr_r      = Power Received (Watts)
# pwr_t      = Power Transmitted
# gain_t     = Gain Transmitted
# gain_r     = Gain Received
# wavelength = Wavelength
# rcs        = Radar Cross-Section
# range      = Range

def radar_range_equation(pwr_t, gain_t, gain_r, freq, rcs, range):
    wavelength = convert_to_wavelength(freq)
    numer = pwr_t * gain_t * gain_r * math.pow(wavelength, 2) * rcs
    denom = math.pow(4 * np.pi, 3) * math.pow(range, 4)
    return numer / denom

def convert_to_NMI(value, unit):
    if   unit == "m"  : return value / 1852
    elif unit == "mi" : return value * 0.868976
    elif unit == "ft" : return value / 6076.12
    else              : return value # Passthrough

def convert_to_dBw(value, unit):
    if   unit == "dBm" : return value - 30.0
    elif unit == "W"   : return 10 * math.log10(value)
    elif unit == "mW"  : return 10 * math.log10(value / 1000)
    else               : return value # Passthrough

def convert_to_GHz(value, unit):
    if   unit == "MHz" : return value / 1000
    elif unit == "kHz" : return value / math.pow(10, 6)
    elif unit == "Hz"  : return value / math.pow(10, 9)
    else               : return value # Passthrough

def convert_to_wavelength(freq):
    c = 299792458   # Speed of light (m/s)
    return c / freq

def calculate_and_plot():
    # sel_pwr_r_unit = pwr_r_unit.get()
    sel_range_unit = range_unit.get()

    pwr_t = convert_to_dBw(float(pwr_t_entry.get()), pwr_t_unit.get())
    gain_t = float(gain_t_entry.get())
    gain_r = float(gain_r_entry.get())
    freq  = convert_to_GHz(float(freq_entry.get()), freq_unit.get())
    rcs    = float(rcs_entry.get())
    range  = convert_to_NMI(float(rcs_entry.get()), sel_range_unit)
    
    pwr_r = radar_range_equation(pwr_t, gain_t, gain_r, freq, rcs, range)
    print(pwr_r)
    
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(range, 10 * np.log10(pwr_r), label="Received Power")
    # ax.plot(range, 10 * np.log10(pwr_n), label="Noise Jammer")
    # ax.plot(range, 10 * np.log10(P_range_j), label="Repeater Jammer")
    ax.set_xlabel(f"Range ({sel_range_unit})")
    ax.set_ylabel('Received Power (dBw)')
    ax.legend()
    canvas.draw()

# Plot button
btn_plot = tk.Button(root, text="Plot", command=calculate_and_plot, font=default_font)
btn_plot.grid(row=9, columnspan=2)

# Matplotlib figure setup
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=10, columnspan=5)

root.mainloop()









