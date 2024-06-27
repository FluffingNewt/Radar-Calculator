import lib.formulas as formulas
import lib.methods  as methods
import tkinter


class Tab4(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        def calc_unam_rPRF():
            if methods.validate_entries(self, 1, 1, 2, "unam_r"): return

            if prf_entry.get() == "":
                r = formulas.convert_to_m(r_prf_entry.get(), r_prf_entry.get())
                prf = formulas.unam_range_prf(r)

                if   prf_unit.get() == "GHz" : prf = formulas.convert_to_GHz(prf, "Hz")
                elif prf_unit.get() == "MHz" : prf = formulas.convert_to_MHz(prf, "Hz")
                elif prf_unit.get() == "kHz" : prf = formulas.convert_to_kHz(prf, "Hz")

                prf_entry.insert(0, f"{prf:.4}")

            else:
                if r_prf_entry.get() != "": r_prf_entry.delete(0, tkinter.END)
                prf = formulas.convert_to_Hz(prf_entry.get(), prf_unit.get())
                r = formulas.unam_range_rPRF(prf)

                if   r_prf_unit.get() == "NMI" : r = formulas.convert_to_NMI(r, "m")
                elif r_prf_unit.get() == "mi"  : r = formulas.convert_to_mi(r, "m")
                elif r_prf_unit.get() == "ft"  : r = formulas.convert_to_ft(r, "m")

                r_prf_entry.insert(0, f"{r:.4}")

                

        
        def calc_unam_rPRI():
            if methods.validate_entries(self, 1, 5, 6, "unam_r"): return

            if pri_entry.get() == "":

                r = formulas.convert_to_m(r_pri_entry.get(), r_pri_unit.get())
                pri = formulas.unam_range_pri(r)

                if   pri_unit.get() == "ms"  : pri = formulas.convert_to_ms(pri, "s")
                elif pri_unit.get() == "min" : pri = formulas.convert_to_min(pri, "s")
                elif pri_unit.get() == "hr"  : pri = formulas.convert_to_hr(pri, "s")

                pri_entry.insert(0, f"{pri:.4}")
                
            else:
                if r_pri_entry.get() != "": r_pri_entry.delete(0, tkinter.END)
                pri = formulas.convert_to_s(pri_entry.get(), pri_unit.get())
                r = formulas.unam_range_rPRI(pri)

                if   r_pri_unit.get() == "NMI" : r = formulas.convert_to_NMI(r, "m")
                elif r_pri_unit.get() == "mi"  : r = formulas.convert_to_mi(r, "m")
                elif r_pri_unit.get() == "ft"  : r = formulas.convert_to_ft(r, "m")

                r_pri_entry.insert(0, f"{r:.4}")


        row = 0
        col = 0
        methods.create_label(self, "Max Unambiguous Range (PRF)", row, col)

        row = 1
        methods.create_label(self, "Pf : PRF", row, col)
        prf_entry = methods.create_entry(self, row, col+1, 10)
        prf_unit = tkinter.StringVar(value="Hz")
        methods.create_combobox(self, prf_unit, formulas.units_freq, row, col+2)

        row = 2
        methods.create_label(self, "R : Unambiguous Range", row, col)
        r_prf_entry = methods.create_entry(self, row, col+1, 10)
        r_prf_unit = tkinter.StringVar(value="m")
        methods.create_combobox(self, r_prf_unit, formulas.units_range, row, col+2)
        doppler_btn = tkinter.Button(self, text="Calculate", command=calc_unam_rPRF, font=methods.default_font)
        doppler_btn.grid(row=row, column=col+3, padx=5, sticky="")


        row = 4
        methods.create_separator(self, "horizontal", row-1, col, 0, 10, columnspan=10)
        methods.create_label(self, "Max Unambiguous Range (PRI)", row, col)

        row = 5
        methods.create_label(self, "Pi : PRI", row, col)
        pri_entry = methods.create_entry(self, row, col+1, 10)
        pri_unit = tkinter.StringVar(value="s")
        methods.create_combobox(self, pri_unit, formulas.units_time, row, col+2)


        row = 6
        methods.create_label(self, "R : Unambiguous Range", row, col)
        r_pri_entry = methods.create_entry(self, row, col+1, 10)
        r_pri_unit = tkinter.StringVar(value="m")
        methods.create_combobox(self, r_pri_unit, formulas.units_range, row, col+2)
        doppler_btn = tkinter.Button(self, text="Calculate", command=calc_unam_rPRI, font=methods.default_font)
        doppler_btn.grid(row=row, column=col+3, padx=5, sticky="")
        