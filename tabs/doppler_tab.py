import lib.formulas as formulas
import lib.methods  as methods
import tkinter


class Tab3(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        def calc_doppler():
            if methods.validate_entries(self, 1, 1, 4, "doppler"): return

            if   vs_entry.get() == "":
                vt = formulas.convert_to_ms(vt_entry.get(), vt_unit.get())
                ft = formulas.convert_to_Hz(ft_entry.get(), ft_unit.get())
                fd = formulas.convert_to_Hz(fd_entry.get(), fd_unit.get())
                vs = formulas.doppler_vs(fd, ft, vt)

                if   vs_unit.get() == "km/h"  : vs = formulas.convert_to_kmh(vs, "m/s")
                elif vs_unit.get() == "mi/h"  : vs = formulas.convert_to_mih(vs, "m/s")
                elif vs_unit.get() == "knots" : vs = formulas.convert_to_knots(vs, "m/s")

                vs_entry.insert(0, f"{vs}")

            elif vt_entry.get() == "":
                vs = formulas.convert_to_ms(vs_entry.get(), vs_unit.get())
                ft = formulas.convert_to_Hz(ft_entry.get(), ft_unit.get())
                fd = formulas.convert_to_Hz(fd_entry.get(), fd_unit.get())
                vt = formulas.doppler_vt(fd, ft, vs)

                if   vt_unit.get() == "km/h"  : vt = formulas.convert_to_kmh(vt, "m/s")
                elif vt_unit.get() == "mi/h"  : vt = formulas.convert_to_mih(vt, "m/s")
                elif vt_unit.get() == "knots" : vt = formulas.convert_to_knots(vt, "m/s")

                vt_entry.insert(0, f"{vt}")

            elif ft_entry.get() == "":
                vt = formulas.convert_to_ms(vt_entry.get(), vt_unit.get())
                vs = formulas.convert_to_ms(vs_entry.get(), vs_unit.get())
                fd = formulas.convert_to_Hz(fd_entry.get(), fd_unit.get())
                ft = formulas.doppler_ft(fd, vs, vt)

                if   ft_unit.get() == "GHz" : ft = formulas.convert_to_GHz(ft, "Hz")
                elif ft_unit.get() == "MHz" : ft = formulas.convert_to_MHz(ft, "Hz")
                elif ft_unit.get() == "kHz" : ft = formulas.convert_to_kHz(ft, "Hz")
                elif ft_unit.get() == "Hz"  : ft = formulas.convert_to_Hz(ft, "Hz")

                ft_entry.insert(0, f"{ft}")

            else:
                if fd_entry.get() != "": fd_entry.delete(0, tkinter.END)
                vt = formulas.convert_to_ms(vt_entry.get(), vt_unit.get())
                vs = formulas.convert_to_ms(vs_entry.get(), vs_unit.get())
                ft = formulas.convert_to_Hz(ft_entry.get(), ft_unit.get())
                fd = formulas.doppler_fd(vs, vt, ft)

                if   fd_unit.get() == "GHz" : fd = formulas.convert_to_GHz(fd, "Hz")
                elif fd_unit.get() == "MHz" : fd = formulas.convert_to_MHz(fd, "Hz")
                elif fd_unit.get() == "kHz" : fd = formulas.convert_to_kHz(fd, "Hz")
                elif fd_unit.get() == "Hz"  : fd = formulas.convert_to_Hz(fd, "Hz")

                fd_entry.insert(0, f"{fd}")
        
        row = 0
        col = 0
        methods.create_label(self, "Shooter-Target Velocity", row, col)

        row = 1
        methods.create_separator(self, "vertical", row, col+1, 5, rowspan=4)
        methods.create_label(self, "Vs : Shooter Velocity", row, col)
        vs_entry = methods.create_entry(self, row, col+1, 10)
        vs_unit = tkinter.StringVar(value="knots")
        methods.create_combobox(self, vs_unit, formulas.units_vel, row, col+2)

        row = 2
        methods.create_label(self, "Vt : Target Velocity", row, col)
        vt_entry = methods.create_entry(self, row, col+1, 10)
        vt_unit = tkinter.StringVar(value="knots")
        methods.create_combobox(self, vt_unit, formulas.units_vel, row, col+2)

        row = 3
        methods.create_label(self, "ft : Transmit Frequency", row, col)
        ft_entry = methods.create_entry(self, row, col+1, 10)
        ft_unit = tkinter.StringVar(value="GHz")
        methods.create_combobox(self, ft_unit, formulas.units_freq, row, col+2)

        row = 4
        methods.create_label(self, "fd : Doppler Frequency", row, col)
        fd_entry = methods.create_entry(self, row, col+1, 10)
        fd_unit = tkinter.StringVar(value="GHz")
        methods.create_combobox(self, fd_unit, formulas.units_freq, row, col+2)
        doppler_btn = tkinter.Button(self, text="Calculate", command=calc_doppler, font=methods.default_font)
        doppler_btn.grid(row=row, column=col+3, padx=5, sticky="")

        row = 6
        methods.create_separator(self, "horizontal", row-1, col, 0, 10, columnspan=10)
        methods.create_label(self, "Unambiguous Closing Velocity (Doppler)", row, col)