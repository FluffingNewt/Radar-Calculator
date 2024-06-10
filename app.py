import formulas as f

import numpy
import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#! Incomplete
class Graph:

    graph_types = ["pr", "nj", "rj"]
    x_values    = []
    y_values    = []

    def __init__(self, graph_type, invalid,pwr_r, pwr_r_u, pwr_t, pwr_t_u, gain_t, gain_r, freq, freq_u, rcs, rcs_u, r, r_u):
        if invalid: return

        self.graph_type = graph_type

        if pwr_t.get() == "":
            self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
            self.gain_t = float(gain_t.get())
            self.gain_r = float(gain_r.get())
            self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
            self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
            self.r      = f.convert_to_m(r.get(), r_u.get())
            
            self.pwr_t = f.rre_pt(self.pwr_r, self.gain_t, self.gain_r, self.freq, self.rcs, self.r)

            if   pwr_t_u.get() == "dBW" : self.pwr_t = f.convert_to_dBW(self.pwr_t, "W")
            elif pwr_t_u.get() == "dBm" : self.pwr_t = f.convert_to_dBm(self.pwr_t, "W")
            elif pwr_t_u.get() == "W"   : self.pwr_t = f.convert_to_W(self.pwr_t, "W")
            elif pwr_t_u.get() == "mW"  : self.pwr_t = f.convert_to_mW(self.pwr_t, "W")

            pt_entries[self.graph_type].insert(0, f"{self.pwr_t}")

        elif gain_t.get() == "":
            self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
            self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
            self.gain_r = float(gain_r.get())
            self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
            self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
            self.r      = f.convert_to_m(r.get(), r_u.get())

            self.gain_t = f.rre_gt(self.pwr_r, self.pwr_t, self.gain_r, self.freq, self.rcs, self.r)

            gt_entries[self.graph_type].insert(0, f"{self.gain_t}")

        elif gain_r.get() == "":
            self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
            self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
            self.gain_t = float(gain_t.get())
            self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
            self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
            self.r      = f.convert_to_m(r.get(), r_u.get())

            self.gain_r = f.rre_gr(self.pwr_r, self.pwr_t, self.gain_t, self.freq, self.rcs, self.r)

            gr_entries[self.graph_type].insert(0, f"{self.gain_r}")
        
        elif freq.get() == "":
            self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
            self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
            self.gain_t = float(gain_t.get())
            self.gain_r = float(gain_r.get())
            self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
            self.r      = f.convert_to_m(r.get(), r_u.get())

            self.freq = f.rre_f(self.pwr_r, self.pwr_t, self.gain_t, self.gain_r, self.rcs, self.r)

            if   freq_u.get() == "GHz" : self.freq = f.convert_to_GHz(self.freq, "Hz")
            elif freq_u.get() == "MHz" : self.freq = f.convert_to_MHz(self.freq, "Hz")
            elif freq_u.get() == "kHz" : self.freq = f.convert_to_kHz(self.freq, "Hz")
            elif freq_u.get() == "Hz"  : self.freq = f.convert_to_Hz(self.freq, "Hz")

            f_entries[self.graph_type].insert(0, f"{self.freq}")
        
        elif rcs.get() == "":
            self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
            self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
            self.gain_t = float(gain_t.get())
            self.gain_r = float(gain_r.get())
            self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
            self.r      = f.convert_to_m(r.get(), r_u.get())

            self.rcs = f.rre_rcs(self.pwr_r, self.pwr_t, self.gain_t, self.gain_r, self.freq, self.r)

            if   rcs_u.get() == "m\u00B2"  : rcs = f.convert_to_m2(self.rcs, "m\u00B2")
            elif rcs_u.get() == "ft\u00B2" : rcs = f.convert_to_ft2(self.rcs, "m\u00B2")

            rcs_entries[self.graph_type].insert(0, f"{rcs}")
        
        elif r.get() == "":
            self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
            self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
            self.gain_t = float(gain_t.get())
            self.gain_r = float(gain_r.get())
            self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
            self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())

            self.r = f.rre_r(self.pwr_r, self.pwr_t, self.gain_t, self.gain_r, self.freq, self.rcs)

            if   r_u.get() == "NMI" : r = f.convert_to_NMI(self.r, "m")
            elif r_u.get() == "mi"  : r = f.convert_to_mi(self.r, "m")
            elif r_u.get() == "m"   : r = f.convert_to_m(self.r, "m")
            elif r_u.get() == "ft"  : r = f.convert_to_ft(self.r, "m")

            r_entries[self.graph_type].insert(0, f"{r}")
        
        else: # if pwr_r == "" or calculate like normal
            if pwr_r.get() != "": pr_entries[self.graph_type].delete(0, tkinter.END)

            self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
            self.gain_t = float(gain_t.get())
            self.gain_r = float(gain_r.get())
            self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
            self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
            self.r      = f.convert_to_m(r.get(), r_u.get())

            self.pwr_r = f.rre_pr(self.pwr_t, self.gain_t, self.gain_r, self.freq, self.rcs, self.r)

            if   pwr_r_u.get() == "dBW" : pwr_r = f.convert_to_dBW(self.pwr_r, "W")
            elif pwr_r_u.get() == "dBm" : pwr_r = f.convert_to_dBm(self.pwr_r, "W")
            elif pwr_r_u.get() == "W"   : pwr_r = f.convert_to_W(self.pwr_r, "W")
            elif pwr_r_u.get() == "mW"  : pwr_r = f.convert_to_mW(self.pwr_r, "W")

            pr_entries[self.graph_type].insert(0, f"{pwr_r}")

            # Log output calculation
            print(f"\nPr = {self.y_values[len(self.y_values) - 1]} {plot_y_unit.get()}")
        
        # Calculate pwr_t values for the selected graph_type
        #! Will probably need to update this to new 1 way jamming formulas, shouldnt affect much
        if   self.graph_type == "rj" : pwr_t_values = numpy.linspace(1, self.pwr_t, 400)
        else                         : pwr_t_values = numpy.linspace(self.pwr_t, self.pwr_t, 400)
        
        # init x and y value arrays
        self.x_values = numpy.linspace(1, self.r, 400)
        self.y_values = []

        # generate x and y values
        i = 0
        for range in self.x_values:
            pr = f.rre_pr(pwr_t_values[i], self.gain_t, self.gain_r, self.freq, self.rcs, range)   
            self.y_values.append(pr)
            i += 1

        self.convert_x_values(plot_x_unit.get())
        self.convert_y_values(plot_y_unit.get())

        
    def convert_x_values(self, unit):
        if unit == "m": return

        new_x_values = []
        for val in self.x_values:

            if   unit == "NMI" : val = f.convert_to_NMI(val, "m")
            elif unit == "mi"  : val = f.convert_to_mi(val, "m")
            elif unit == "ft"  : val = f.convert_to_ft(val, "m")

            new_x_values.append(val)
        
        self.x_values = new_x_values


    def convert_y_values(self, unit):
        new_y_values = []

        for val in self.y_values:

            if   unit == "dBW" : val = f.convert_to_dBW(val, "W")
            elif unit == "dBm" : val = f.convert_to_dBm(val, "W")
            elif unit == "mW"  : val = f.convert_to_mW(val, "W")

            new_y_values.append(val)
        
        self.y_values = new_y_values

##################################### Calculations ######################################

def calculate_and_plot():
    pr_error = False
    nj_error = False
    rj_error = False

    # Check if all text fields have valid inputs
    for i in range(1, 6, 2):
        if   i == 1: pr_error = validate_entries(i)
        elif i == 3: nj_error = validate_entries(i)
        elif i == 5: rj_error = validate_entries(i)

    root.focus_set()

    graph_pr = Graph("pr", pr_error,
                     pr_entries ["pr"] , pr_units  ["pr"],
                     pt_entries ["pr"] , pt_units  ["pr"],
                     gt_entries ["pr"] , gr_entries["pr"],
                     f_entries  ["pr"] , f_units   ["pr"],
                     rcs_entries["pr"] , rcs_units ["pr"],
                     r_entries  ["pr"] , r_units   ["pr"])
    
    # graph_nj = Graph("nj", nj_error, 
    #                  pr_entries ["nj"] , pr_units  ["nj"],
    #                  pt_entries ["nj"] , pt_units  ["nj"],
    #                  gt_entries ["nj"] , gr_entries["nj"],
    #                  f_entries  ["nj"] , f_units   ["nj"],
    #                  rcs_entries["nj"] , rcs_units ["nj"],
    #                  r_entries  ["nj"] , r_units   ["nj"])
    
    # graph_rj = Graph("rj", rj_error, 
    #                  pr_entries ["rj"] , pr_units  ["rj"],
    #                  pt_entries ["rj"] , pt_units  ["rj"],
    #                  gt_entries ["rj"] , gr_entries["rj"],
    #                  f_entries  ["rj"] , f_units   ["rj"],
    #                  rcs_entries["rj"] , rcs_units ["rj"],
    #                  r_entries  ["rj"] , r_units   ["rj"])

    # Clear, initialize, and plot graph
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(graph_pr.x_values, graph_pr.y_values, label="Received Power")
    # ax.plot(graph_nj.x_values, graph_nj.y_values, label="Noise Jammer")
    # ax.plot(graph_rj.x_values, graph_rj.y_values, label="Repeater Jammer")
    ax.set_xlabel(f"Range ({plot_x_unit.get()})")
    ax.set_ylabel(f"Received Power {plot_y_unit.get()}")
    ax.legend(loc="upper right")
    canvas.draw()

###################################### GUI Setup ########################################

def validate_entries(column):
    blank_entries = []
    error_found = False

    # Loop through all children of the root window
    for child in root.winfo_children():
        if isinstance(child, tkinter.Entry):
            info = child.grid_info()
            if info['column'] == column and info['row'] <= 7:
                value = child.get()

                if any(char.isalpha() for char in value) or \
                   any(char in value for char in "[$&+,:;=?@#|'\"<>-_^*()%!]") or \
                   value in ["0", "0.0"]:
                    print(f"Error: Invalid input '{value}' in row {info['row']}")
                    child.delete(0, tkinter.END)
                    child.insert(0, "invalid input")
                    child.config(fg="red")
                    error_found = True
                elif value == "":
                    blank_entries.append(child)

    # Handle multiple blank entries
    if len(blank_entries) > 1:
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


def create_label(root, text, row, column, padx=10, pady=5, sticky="w", columnspan=1):
    label = tkinter.Label(root, text=text, font=default_font)
    label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return label


def create_entry(root, row, column, padx=0 , pady=10):
    entry = tkinter.Entry(root)
    entry.grid(row=row, column=column, padx=padx, pady=pady, sticky="w")
    entry.bind("<FocusIn>", lambda event: reset_entry(event, entry))
    return entry


def create_combobox(root, textvariable, values, row, column, width=6, pady=10, sticky=""):
    combobox = ttk.Combobox(root, textvariable=textvariable, values=values, font=default_font, state="readonly", width=width)
    combobox.grid(row=row, column=column, pady=pady, sticky=sticky)
    return combobox


def create_separator(root, orient, row, column, rowspan, columnspan, sticky, padx=0, pady=0):
    separator = ttk.Separator(root, orient=orient)
    separator.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=sticky, padx=padx, pady=pady)


# Root
root = tkinter.Tk()
root.geometry("870x870")
root.title("Radar Range Equation Calculator")
default_font = ('Product Sans', 13)


create_label(root, "Received Power", 0, 0, 10, 5, "ew", 3)
create_label(root, "Noise Jammer", 0, 3, 10, 5, "ew", 2)
create_label(root, "Repeater Jammer", 0, 5, 10, 5, "ew", 2)

# Power Transmitted
row = 2
col = 0
pt_entries = {}
pt_units = {}
col_count = 1
i = 0
create_label(root, "Pt : Power Transmitted", row, col)
for type in Graph.graph_types:
    pt_entries[type] = create_entry(root, row, col+1, 10)
    pt_units[type] = tkinter.StringVar(value="dBW")
    create_combobox(root, pt_units[type], f.units_dBW, row, col+2)
    
    if i != len(Graph.graph_types) - 1:
        create_separator(root, "vertical", 0, col+3, 11, 1, "nsw", 5)
    i += 1
    col += 2
    col_count += 3

# Gain Transmitted
row = 3
col = 0
gt_entries = {}
create_label(root, "Gt : Gain Transmitted", row, col)
for type in Graph.graph_types:
    gt_entries[type] = create_entry(root, row, col+1, 10)
    col += 2

# Gain Received
row = 4
col = 0
gr_entries = {}
create_label(root, "Gr : Gain Received", row, col)
for type in Graph.graph_types:
    gr_entries[type] = create_entry(root, row, col+1, 10)
    col += 2
    col_count += 1

# Frequency
row = 5
col = 0
f_entries = {}
f_units = {}
create_label(root, "\u03BD : Frequency", row, col)
for type in Graph.graph_types:
    f_entries[type] = create_entry(root, row, col+1, 10)
    f_units[type] = tkinter.StringVar(value="GHz")
    create_combobox(root, f_units[type], f.units_GHz, row, col+2)
    col += 2

# RCS
row = 6 
col = 0
rcs_entries = {}
rcs_units = {}
create_label(root, "\u03C3 : Radar Cross Section", row, col)
for type in Graph.graph_types:
    rcs_entries[type] = create_entry(root, row, col+1, 10)
    rcs_units[type] = tkinter.StringVar(value="m\u00B2")
    create_combobox(root, rcs_units[type], f.units_rcs, row, col+2)
    col += 2

# Range
row = 7
col = 0
r_entries = {}
r_units = {}
create_label(root, "R : Range", row, col)
for type in Graph.graph_types:
    r_entries[type] = create_entry(root, row, col+1, 10)
    r_units[type] = tkinter.StringVar(value="NMI")
    create_combobox(root, r_units[type], f.units_NMI, row, col+2)
    col += 2

# Power Received
row = 9
col = 0
pr_entries = {}
pr_units = {}
create_label(root, "Pr : Power Received", row, col, 10, 10)
for type in Graph.graph_types:
    pr_entries[type] = create_entry(root, row, col+1, 10)
    pr_units[type] = tkinter.StringVar(value="dBW")
    create_combobox(root, pr_units[type], f.units_dBW, row, col+2)
    col += 2

# x Unit
row = 11
col = 0
frame = tkinter.Frame(root)
frame.grid(row=row, column=col, columnspan=1, rowspan=1, sticky="n")
plot_x_unit = tkinter.StringVar(value="NMI")
row = 0
col = 0
create_label(frame, "x Unit", row, col)
create_combobox(frame, plot_x_unit, f.units_NMI, row, col+1)

# y Unit
plot_y_unit = tkinter.StringVar(value="dBW")
create_label(frame, "y Unit", row+1, col)
create_combobox(frame, plot_y_unit, f.units_dBW, row+1, col+1)

# Plot Button
btn_plot = tkinter.Button(frame, text="Plot", command=calculate_and_plot, font=default_font)
btn_plot.grid(row=row+2, column=col, columnspan=2, sticky="s")

# Separator
create_label(root, "", 10, 0, 10, 10, "")
create_separator(root, "horizontal", 1, 0, 1, col_count+3, "ew")
create_separator(root, "horizontal", 8, 0, 1, col_count+3, "ew", 0, 0)

# Matplotlib figure setup
row = 11
col = 1
fig = Figure(layout="tight")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=11, column=col, columnspan=6, sticky="ew")

ax = fig.add_subplot(111)
ax.plot(1, 1, label="Received Power")
ax.plot(0, 0, label="Noise Jammer")
ax.plot(0, 0, label="Repeater Jammer")
ax.legend(loc="upper right")
canvas.draw()

ax.set_xlabel(f"Range ({plot_x_unit.get()})")
ax.set_ylabel(f"Received Power {plot_y_unit.get()}")

root.mainloop()