import lib.formulas as f
import lib.methods  as m
import tkinter


class Tab4(tkinter.Frame):

    default_font = ('Arial', 12)
    bold_font    = ("Arial", 12, "bold")

    def __init__(self, parent):
        super().__init__(parent)



        def calc_unam_rPRF():
            if m.validate_entries(self, 1, 1, 2, "unam_r"): return

            if prf_entry.get() == "":
                r = f.convert_to_m(r_prf_entry.get(), r_prf_entry.get())
                prf = f.unam_range_prf(r)

                if   prf_unit.get() == "GHz" : prf = f.convert_to_GHz(prf, "Hz")
                elif prf_unit.get() == "MHz" : prf = f.convert_to_MHz(prf, "Hz")
                elif prf_unit.get() == "kHz" : prf = f.convert_to_kHz(prf, "Hz")

                prf_entry.insert(0, f"{prf:.4}")

            else:
                if r_prf_entry.get() != "": r_prf_entry.delete(0, tkinter.END)
                prf = f.convert_to_Hz(prf_entry.get(), prf_unit.get())
                r = f.unam_range_rPRF(prf)

                if   r_prf_unit.get() == "NMI" : r = f.convert_to_NMI(r, "m")
                elif r_prf_unit.get() == "mi"  : r = f.convert_to_mi(r, "m")
                elif r_prf_unit.get() == "ft"  : r = f.convert_to_ft(r, "m")

                r_prf_entry.insert(0, f"{r:.4}")

                

        
        def calc_unam_rPRI():
            if m.validate_entries(self, 1, 5, 6, "unam_r"): return

            if pri_entry.get() == "":

                r = f.convert_to_m(r_pri_entry.get(), r_pri_unit.get())
                pri = f.unam_range_pri(r)

                if   pri_unit.get() == "ms"  : pri = f.convert_to_ms(pri, "s")
                elif pri_unit.get() == "min" : pri = f.convert_to_min(pri, "s")
                elif pri_unit.get() == "hr"  : pri = f.convert_to_hr(pri, "s")

                pri_entry.insert(0, f"{pri:.4}")
                
            else:
                if r_pri_entry.get() != "": r_pri_entry.delete(0, tkinter.END)
                pri = f.convert_to_s(pri_entry.get(), pri_unit.get())
                r = f.unam_range_rPRI(pri)

                if   r_pri_unit.get() == "NMI" : r = f.convert_to_NMI(r, "m")
                elif r_pri_unit.get() == "mi"  : r = f.convert_to_mi(r, "m")
                elif r_pri_unit.get() == "ft"  : r = f.convert_to_ft(r, "m")

                r_pri_entry.insert(0, f"{r:.4}")


        row = 0
        col = 0
        m.create_label(self, "Max Unambiguous Range (PRF)", row, col)

        row = 1
        m.create_label(self, "Pf : PRF", row, col)
        prf_entry = m.create_entry(self, row, col+1, 10)
        prf_unit = tkinter.StringVar(value="Hz")
        m.create_combobox(self, prf_unit, f.units_freq, row, col+2)

        row = 2
        m.create_label(self, "R : Unambiguous Range", row, col)
        r_prf_entry = m.create_entry(self, row, col+1, 10)
        r_prf_unit = tkinter.StringVar(value="m")
        m.create_combobox(self, r_prf_unit, f.units_range, row, col+2)
        doppler_btn = tkinter.Button(self, text="Calculate", command=calc_unam_rPRF, font=m.default_font)
        doppler_btn.grid(row=row, column=col+3, padx=5, sticky="")


        row = 4
        m.create_separator(self, "horizontal", row-1, col, 0, 10, columnspan=10)
        m.create_label(self, "Max Unambiguous Range (PRI)", row, col)

        row = 5
        m.create_label(self, "Pi : PRI", row, col)
        pri_entry = m.create_entry(self, row, col+1, 10)
        pri_unit = tkinter.StringVar(value="s")
        m.create_combobox(self, pri_unit, f.units_time, row, col+2)


        row = 6
        m.create_label(self, "R : Unambiguous Range", row, col)
        r_pri_entry = m.create_entry(self, row, col+1, 10)
        r_pri_unit = tkinter.StringVar(value="m")
        m.create_combobox(self, r_pri_unit, f.units_range, row, col+2)
        doppler_btn = tkinter.Button(self, text="Calculate", command=calc_unam_rPRI, font=m.default_font)
        doppler_btn.grid(row=row, column=col+3, padx=5, sticky="")
        