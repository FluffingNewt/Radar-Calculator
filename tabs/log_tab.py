import lib.formulas as f
import lib.methods as m
import numpy
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#* Notes
#* - Converts the input values into 10*log_10 values and calculates Pr
#* - If a value is empty, it will fill the box with the normal base10 version of the value.

#! To-Do
#!

class Tab2(tkinter.Frame):
    
    graph_types  = ["pr", "nj", "rj"]


    def __init__(self, parent):
        super().__init__(parent)

        ##################################### Graph Classes #####################################

        class Graph:

            def __init__(self, invalid, pwr_r, pwr_r_u, pwr_t, pwr_t_u, gain_t, gain_r, freq, freq_u, rcs, rcs_u, r, r_u):
                if invalid: return

                if pwr_t.get() == "":
                    self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
                    self.gain_t = float(gain_t.get())
                    self.gain_r = float(gain_r.get())
                    self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
                    self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
                    self.r      = f.convert_to_m(r.get(), r_u.get())
                    
                    log_pwr_t = f.rre_log_pt(self.pwr_r, self.gain_t, self.gain_r, self.freq, self.rcs, self.r)
                    self.pwr_t = 10 ** (log_pwr_t / 10)

                    if   pwr_t_u.get() == "dBW" : pwr_t = f.convert_to_dBW(self.pwr_t, "W")
                    elif pwr_t_u.get() == "dBm" : pwr_t = f.convert_to_dBm(self.pwr_t, "W")
                    elif pwr_t_u.get() == "W"   : pwr_t = f.convert_to_W(self.pwr_t, "W")
                    elif pwr_t_u.get() == "mW"  : pwr_t = f.convert_to_mW(self.pwr_t, "W")

                    pt_entries["pr"].insert(0, f"{self.pwr_t}")

                    print(f"\nGraph type - Pr:  Pt = {self.pwr_t} {pwr_t_u.get()}")

                elif gain_t.get() == "":
                    self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
                    self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
                    self.gain_r = float(gain_r.get())
                    self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
                    self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
                    self.r      = f.convert_to_m(r.get(), r_u.get())

                    log_gain_t = f.rre_log_gt(self.pwr_r, self.pwr_t, self.gain_r, self.freq, self.rcs, self.r)
                    self.gain_t = 10 ** (log_gain_t / 10)

                    gt_entries["pr"].insert(0, f"{self.gain_t}")

                    print(f"\nGraph type - Pr:  Gt = {self.gain_t}")

                elif gain_r.get() == "":
                    self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
                    self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
                    self.gain_t = float(gain_t.get())
                    self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
                    self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
                    self.r      = f.convert_to_m(r.get(), r_u.get())

                    log_gain_r = f.rre_log_gr(self.pwr_r, self.pwr_t, self.gain_t, self.freq, self.rcs, self.r)
                    self.gain_r = 10 ** (log_gain_r / 10)

                    gr_entries["pr"].insert(0, f"{self.gain_r}")
                    
                    print(f"\nGraph type - Pr:  Gr = {self.gain_r}")
                
                elif freq.get() == "":
                    self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
                    self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
                    self.gain_t = float(gain_t.get())
                    self.gain_r = float(gain_r.get())
                    self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
                    self.r      = f.convert_to_m(r.get(), r_u.get())

                    log_freq = f.rre_log_f(self.pwr_r, self.pwr_t, self.gain_t, self.gain_r, self.rcs, self.r)
                    self.freq = 10 ** (log_freq / 10)

                    if   freq_u.get() == "GHz" : freq = f.convert_to_GHz(self.freq, "Hz")
                    elif freq_u.get() == "MHz" : freq = f.convert_to_MHz(self.freq, "Hz")
                    elif freq_u.get() == "kHz" : freq = f.convert_to_kHz(self.freq, "Hz")
                    elif freq_u.get() == "Hz"  : freq = f.convert_to_Hz(self.freq, "Hz")

                    f_entries["pr"].insert(0, f"{freq}")

                    print(f"\nGraph type - Pr:  freq = {freq} {freq_u.get()}")
                
                elif rcs.get() == "":
                    self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
                    self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
                    self.gain_t = float(gain_t.get())
                    self.gain_r = float(gain_r.get())
                    self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
                    self.r      = f.convert_to_m(r.get(), r_u.get())

                    log_rcs = f.rre_log_rcs(self.pwr_r, self.pwr_t, self.gain_t, self.gain_r, self.freq, self.r)
                    self.rcs = 10 ** (log_rcs / 10)

                    if   rcs_u.get() == "m\u00B2"  : rcs = f.convert_to_m2(self.rcs, "m\u00B2")
                    elif rcs_u.get() == "ft\u00B2" : rcs = f.convert_to_ft2(self.rcs, "m\u00B2")

                    rcs_entries["pr"].insert(0, f"{rcs}")

                    print(f"\nGraph type - Pr:  rcs = {rcs} {rcs_u.get()}")
                
                elif r.get() == "":
                    self.pwr_r  = f.convert_to_W(pwr_r.get(), pwr_r_u.get())
                    self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
                    self.gain_t = float(gain_t.get())
                    self.gain_r = float(gain_r.get())
                    self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
                    self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())

                    log_r = f.rre_log_r(self.pwr_r, self.pwr_t, self.gain_t, self.gain_r, self.freq, self.rcs)
                    self.r = 10 ** (log_r / 10)

                    if   r_u.get() == "NMI" : r = f.convert_to_NMI(self.r, "m")
                    elif r_u.get() == "mi"  : r = f.convert_to_mi(self.r, "m")
                    elif r_u.get() == "m"   : r = f.convert_to_m(self.r, "m")
                    elif r_u.get() == "ft"  : r = f.convert_to_ft(self.r, "m")

                    r_entries["pr"].insert(0, f"{r}")

                    print(f"\nGraph type - Pr:  R = {r} {r_u.get()}")
                
                else: # if pwr_r == "" or calculate like normal
                    if pwr_r.get() != "": pr_entries["pr"].delete(0, tkinter.END)

                    self.pwr_t  = f.convert_to_W(pwr_t.get(), pwr_t_u.get())
                    self.gain_t = float(gain_t.get())
                    self.gain_r = float(gain_r.get())
                    self.freq   = f.convert_to_Hz(freq.get(), freq_u.get())
                    self.rcs    = f.convert_to_m2(rcs.get(), rcs_u.get())
                    self.r      = f.convert_to_m(r.get(), r_u.get())

                    log_pwr_r = f.rre_log_pr(self.pwr_t, self.gain_t, self.gain_r, self.freq, self.rcs, self.r)
                    self.pwr_r = 10 ** (log_pwr_r / 10)

                    if   pwr_r_u.get() == "dBW" : pwr_r = f.convert_to_dBW(self.pwr_r, "W")
                    elif pwr_r_u.get() == "dBm" : pwr_r = f.convert_to_dBm(self.pwr_r, "W")
                    elif pwr_r_u.get() == "W"   : pwr_r = f.convert_to_W(self.pwr_r, "W")
                    elif pwr_r_u.get() == "mW"  : pwr_r = f.convert_to_mW(self.pwr_r, "W")

                    pr_entries["pr"].insert(0, f"{pwr_r}")

                    print(f"\nGraph type - Pr:  Pr = {pwr_r} {pwr_r_u.get()}")
                    print(f"               10log = {log_pwr_r} {pwr_r_u.get()}")

                # generate x and y values
                self.x_values = numpy.linspace(1, self.r, 100)
                self.y_values = []

                for range in self.x_values:
                    pr = f.rre_log_pr(self.pwr_t, self.gain_t, self.gain_r, self.freq, self.rcs, range)
                    self.y_values.append(pr)
                

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


        ##################################### Methods ######################################

        def calculate_and_plot():
            pr_error = False

            # Check if all text fields have valid inputs
            pr_error = m.validate_entries(self, 1, 10)

            self.focus_set()

            graph_pr = Graph(pr_error,
                            pr_entries ["pr"] , pr_units  ["pr"],
                            pt_entries ["pr"] , pt_units  ["pr"],
                            gt_entries ["pr"] , gr_entries["pr"],
                            f_entries  ["pr"] , f_units   ["pr"],
                            rcs_entries["pr"] , rcs_units ["pr"],
                            r_entries  ["pr"] , r_units   ["pr"])
            

            # Clear, initialize, and plot graph
            if not pr_error:
                fig.clear()
                ax = fig.add_subplot(111)
                ax.plot(graph_pr.x_values, graph_pr.y_values, label="Received Power")
                ax.set_xlabel(f"Range ({plot_x_unit.get()})")
                ax.set_ylabel(f"Received Power {plot_y_unit.get()}")
                ax.legend(loc="upper right")
                canvas.draw()


        ###################################### GUI Setup ########################################

        # Header Labels
        m.create_label(self, "Received Power" , 0, 1, 10, 5, "ew", 2)

        row = 2
        col = 0
        # Power Transmitted
        pt_entries = {}
        pt_units = {}
        m.create_label(self, "Pt : Power Transmitted", row, col)
        pt_entries["pr"] = m.create_entry(self, row, col+1, 10)
        pt_units["pr"] = tkinter.StringVar(value="dBW")
        m.create_combobox(self, pt_units["pr"], f.units_dBW, row, col+2)

        row = 3
        col = 0
        # Gain Transmitted
        gt_entries = {}
        m.create_label(self, "Gt : Gain Transmitted", row, col)
        gt_entries["pr"] = m.create_entry(self, row, col+1, 10)

        row = 4
        col = 0
        # Gain Received
        gr_entries = {}
        m.create_label(self, "Gr : Gain Received", row, col)
        gr_entries["pr"] = m.create_entry(self, row, col+1, 10)

        row = 5
        col = 0
        # Frequency
        f_entries = {}
        f_units = {}
        m.create_label(self, "\u03BD : Frequency", row, col)
        f_entries["pr"] = m.create_entry(self, row, col+1, 10)
        f_units["pr"] = tkinter.StringVar(value="GHz")
        m.create_combobox(self, f_units["pr"], f.units_GHz, row, col+2)

        row = 6 
        col = 0
        # RCS
        rcs_entries = {}
        rcs_units = {}
        m.create_label(self, "\u03C3 : Radar Cross Section", row, col)
        rcs_entries["pr"] = m.create_entry(self, row, col+1, 10)
        rcs_units["pr"] = tkinter.StringVar(value="m\u00B2")
        m.create_combobox(self, rcs_units["pr"], f.units_rcs, row, col+2)

        row = 7
        col = 0
        # Range
        r_entries = {}
        r_units = {}
        m.create_label(self, "R : Range", row, col)
        r_entries["pr"] = m.create_entry(self, row, col+1, 10)
        r_units["pr"] = tkinter.StringVar(value="NMI")
        m.create_combobox(self, r_units["pr"], f.units_NMI, row, col+2)

        row = 9
        col = 0
        # Power Received
        pr_entries = {}
        pr_units = {}
        m.create_label(self, "Pr : Power Received", row, col, 10, 10)
        pr_entries["pr"] = m.create_entry(self, row, col+1, 10)
        pr_units["pr"] = tkinter.StringVar(value="dBW")
        m.create_combobox(self, pr_units["pr"], f.units_dBW, row, col+2)

        row = 11
        col = 0
        # Graph Units Frame
        frame = tkinter.Frame(self)
        frame.grid(row=row, column=col, columnspan=1, rowspan=1, sticky="n")

        row = 0
        col = 0
        ## x Unit
        plot_x_unit = tkinter.StringVar(value="NMI")
        m.create_label(frame, "x Unit", row, col)
        m.create_combobox(frame, plot_x_unit, f.units_NMI, row, col+1)

        ## y Unit
        plot_y_unit = tkinter.StringVar(value="dBW")
        m.create_label(frame, "y Unit", row+1, col)
        m.create_combobox(frame, plot_y_unit, f.units_dBW, row+1, col+1)

        ## Plot Button
        btn_plot = tkinter.Button(frame, text="Plot", command=calculate_and_plot, font=m.default_font)
        btn_plot.grid(row=row+2, column=col, columnspan=2, sticky="s")

        # Separators
        m.create_separator(self, "horizontal", 1, 0)
        m.create_separator(self, "horizontal", 8, 0)
        m.create_separator(self, "horizontal", 10, 0)

        row = 11
        col = 1
        # Graph
        fig = Figure(layout="tight")
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=row, column=col, columnspan=6, sticky="ew")

        ax = fig.add_subplot(111)
        ax.plot(1, 1, label="Received Power")
        ax.legend(loc="upper right")
        canvas.draw()

        ax.set_xlabel(f"Range ({plot_x_unit.get()})")
        ax.set_ylabel(f"Received Power (10log {plot_y_unit.get()})")