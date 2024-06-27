import lib.formulas as formulas
import lib.methods as m
import numpy
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#* Notes
#* - Converts the input values into 10*log_10 values and calculates Pr
#* - If a value is empty, it will fill the box with the normal base10 version of the value.
#* - As the formulas output the 10*log_10 values, it plots the log scaled x and y axis to the graph

class Tab2(tkinter.Frame):
    
    graph_types  = ["pr", "nj", "rj"]

    def __init__(self, parent):
        super().__init__(parent)

        ##################################### Graph Classes #####################################

        class Graph:

            def __init__(self, invalid, pr, pr_u, pt, pt_u, gt, gr, f, f_u, rcs, rcs_u, r, r_u):
                if invalid: return

                self.pr  , self.pr_unit  = formulas.convert_to_dBW(pr.get() , pr_u.get())  , pr_u.get()
                self.pt  , self.pt_unit  = formulas.convert_to_dBW(pt.get() , pt_u.get())  , pt_u.get()
                self.f   , self.f_unit   = formulas.convert_to_Hz(f.get()   , f_u.get())   , f_u.get()
                self.rcs , self.rcs_unit = formulas.convert_to_m2(rcs.get() , rcs_u.get()) , rcs_u.get()
                self.r   , self.r_unit   = formulas.convert_to_m(r.get()    , r_u.get())   , r_u.get()
                self.gt                  = float(gt.get()) if gt.get() != "" else ""
                self.gr                  = float(gr.get()) if gr.get() != "" else ""

                self.x_values = []
                self.y_values = []

                self.error_report = False
            
            
            def calc_missing(self):
                if   self.pt  == "":
                    log_pt = formulas.rre_log_pt(self.pr, self.gt, self.gr, self.f, self.rcs, self.r)
                    self.pt = 10 ** (log_pt / 10)

                    try:
                        if self.pt_unit == "dBm" : pt = formulas.convert_to_dBm(self.pt, "dBW")
                        elif self.pt_unit == "W" : pt = formulas.convert_to_W(self.pt, "dBW")
                        else                     : pt = self.pt

                        pt_entries["pr"].insert(0, f"{pt:.4e}")

                    except:
                        r_entries["pr"].insert(0, "error")
                        r_entries["pr"].config(fg="red")

                elif self.gt  == "":
                    log_gt = formulas.rre_log_gt(self.pr, self.pt, self.gr, self.f, self.rcs, self.r)
                    self.gt = 10 ** (log_gt / 10)
                    gt_entries["pr"].insert(0, f"{self.gt:.4e}")

                elif self.gr  == "":
                    log_gr = formulas.rre_log_gt(self.pr, self.pt, self.gt, self.f, self.rcs, self.r)
                    self.gr = 10 ** (log_gr / 10)
                    gr_entries["pr"].insert(0, f"{self.gr:.4e}")

                elif self.f   == "":
                    log_f = formulas.rre_log_f(self.pr, self.pt, self.gt, self.gr, self.rcs, self.r)
                    self.f = 10 ** (log_f / 10)

                    try:
                        if   self.f_unit == "GHz" : f = formulas.convert_to_GHz(self.f, "Hz")
                        elif self.f_unit == "MHz" : f = formulas.convert_to_MHz(self.f, "Hz")
                        elif self.f_unit == "kHz" : f = formulas.convert_to_kHz(self.f, "Hz")
                        else                      : f = self.f

                        f_entries["pr"].insert(0, f"{f:.4e}")

                    except:
                        r_entries["pr"].insert(0, "error")
                        r_entries["pr"].config(fg="red")

                elif self.rcs == "":
                    log_rcs = formulas.rre_log_rcs(self.pr, self.pt, self.gt, self.gr, self.f, self.r)
                    self.rcs = 10 ** (log_rcs / 10)
                    
                    try:
                        if self.rcs_unit == "ft\u00B2" : rcs = formulas.convert_to_ft2(self.rcs, "m\u00B2")
                        else                           : rcs = self.rcs

                        rcs_entries["pr"].insert(0, f"{rcs:.4e}")

                    except:
                        r_entries["pr"].insert(0, "error")
                        r_entries["pr"].config(fg="red")

                elif self.r   == "":
                    log_r = formulas.rre_log_r(self.pr, self.pt, self.gt, self.gr, self.f, self.rcs)
                    self.r = 10 ** (log_r / 10)

                    try:
                        if   self.r_unit == "NMI" : r = formulas.convert_to_NMI(self.r, "m")
                        elif self.r_unit == "mi"  : r = formulas.convert_to_mi(self.r, "m")
                        elif self.r_unit == "ft"  : r = formulas.convert_to_ft(self.r, "m")
                        else                      : r = self.r

                        r_entries["pr"].insert(0, f"{r:.4e}")

                    except:
                        r_entries["pr"].insert(0, "error")
                        r_entries["pr"].config(fg="red")

                else:
                    if self.pr != "": pr_entries["pr"].delete(0, tkinter.END)

                    log_pr = formulas.rre_log_pr(self.pt, self.gt, self.gr, self.f, self.rcs, self.r)
                    self.pr = 10 ** (log_pr / 10)

                    try:
                        if   self.pr_unit == "dBm" : pr = formulas.convert_to_dBm(self.pr, "dBW")
                        elif self.pr_unit == "W"   : pr = formulas.convert_to_W(self.pr, "dBW")
                        else                       : pr = self.pr

                        pr_entries["pr"].insert(0, f"{pr:.4e}")

                    except:
                        pr_entries["pr"].insert(0, "error")
                        pr_entries["pr"].config(fg="red")
                
            
            def gen_graph(self):
                self.x_values = numpy.linspace(1, self.r, 10)

                for r in self.x_values:
                    pr = formulas.rre_log_pr(self.pt, self.gt, self.gr, self.f, self.rcs, r)
                    self.y_values.append(pr)
                
                self.convert_x_values(plot_x_unit.get())
                self.convert_y_values(plot_y_unit.get())
            
            
            def convert_x_values(self, unit):
                new_x_values = []
                for val in self.x_values:

                    if   unit == "NMI" : val = formulas.convert_to_NMI(val, "m")
                    elif unit == "mi"  : val = formulas.convert_to_mi(val, "m")
                    elif unit == "ft"  : val = formulas.convert_to_ft(val, "m")

                    new_x_values.append(formulas.convert_to_log(val))
                
                self.x_values = new_x_values


            def convert_y_values(self, unit):
                if unit == "dBW": return

                new_y_values = []
                for val in self.y_values:
                    
                    val = 10 ** (val / 10)
                    if   unit == "dBm" : val = formulas.convert_to_dBm(val, "dBW")
                    elif unit == "W"   : val = formulas.convert_to_W(val, "dBW")

                    new_y_values.append(formulas.convert_to_log(val))
                
                self.y_values = new_y_values


        ##################################### Methods ######################################

        def calculate_and_plot():
            pr_error = False

            # Check if all text fields have valid inputs
            pr_error = m.validate_entries(self, 1, 2, 9, "log")

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
                graph_pr.calc_missing()
                graph_pr.gen_graph()

                fig.clear()
                ax = fig.add_subplot(111)
                ax.plot(graph_pr.x_values, graph_pr.y_values, label="Received Power")
                ax.set_xlabel(f"Range (10log {plot_x_unit.get()})")
                ax.set_ylabel(f"Received Power (10log {plot_y_unit.get()})")
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
        m.create_combobox(self, pt_units["pr"], formulas.units_pwr, row, col+2)

        row = 3
        # Gain Transmitted
        gt_entries = {}
        m.create_label(self, "Gt : Gain Transmitted", row, col)
        gt_entries["pr"] = m.create_entry(self, row, col+1, 10)

        row = 4
        # Gain Received
        gr_entries = {}
        m.create_label(self, "Gr : Gain Received", row, col)
        gr_entries["pr"] = m.create_entry(self, row, col+1, 10)

        row = 5
        # Frequency
        f_entries = {}
        f_units = {}
        m.create_label(self, "\u03BD : Frequency", row, col)
        f_entries["pr"] = m.create_entry(self, row, col+1, 10)
        f_units["pr"] = tkinter.StringVar(value="GHz")
        m.create_combobox(self, f_units["pr"], formulas.units_freq, row, col+2)

        row = 6
        # RCS
        rcs_entries = {}
        rcs_units = {}
        m.create_label(self, "\u03C3 : Radar Cross Section", row, col)
        rcs_entries["pr"] = m.create_entry(self, row, col+1, 10)
        rcs_units["pr"] = tkinter.StringVar(value="m\u00B2")
        m.create_combobox(self, rcs_units["pr"], formulas.units_area, row, col+2)

        row = 7
        # Range
        r_entries = {}
        r_units = {}
        m.create_label(self, "R : Range", row, col)
        r_entries["pr"] = m.create_entry(self, row, col+1, 10)
        r_units["pr"] = tkinter.StringVar(value="NMI")
        m.create_combobox(self, r_units["pr"], formulas.units_range, row, col+2)

        row = 9
        # Power Received
        pr_entries = {}
        pr_units = {}
        m.create_label(self, "Pr : Power Received", row, col, 10, 10)
        pr_entries["pr"] = m.create_entry(self, row, col+1, 10)
        pr_units["pr"] = tkinter.StringVar(value="dBW")
        m.create_combobox(self, pr_units["pr"], formulas.units_pwr, row, col+2)

        row = 11
        # Graph Units Frame
        frame = tkinter.Frame(self)
        frame.grid(row=row, column=col, columnspan=1, rowspan=1, sticky="n")

        row = 0
        ## x Unit
        plot_x_unit = tkinter.StringVar(value="NMI")
        m.create_label(frame, "x Unit", row, col)
        m.create_combobox(frame, plot_x_unit, formulas.units_range, row, col+1)

        ## y Unit
        plot_y_unit = tkinter.StringVar(value="dBW")
        m.create_label(frame, "y Unit", row+1, col)
        m.create_combobox(frame, plot_y_unit, formulas.units_pwr, row+1, col+1)

        ## Plot Button
        btn_plot = tkinter.Button(frame, text="Plot", command=calculate_and_plot, font=m.default_font)
        btn_plot.grid(row=row+2, column=col, columnspan=2, sticky="s")

        # Separators
        m.create_separator(self, "horizontal", 1, 0, columnspan=3)
        m.create_separator(self, "horizontal", 8, 0, columnspan=3)
        m.create_separator(self, "horizontal", 10, 0, columnspan=3)

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

        ax.set_xlabel(f"Range (10log {plot_x_unit.get()})")
        ax.set_ylabel(f"Received Power (10log {plot_y_unit.get()})")