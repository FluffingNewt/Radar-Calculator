import lib.formulas as f
import lib.methods  as m
import tkinter


class Tab3(tkinter.Frame):

    default_font = ('Arial', 12)
    bold_font    = ("Arial", 12, "bold")


    def __init__(self, parent):
        super().__init__(parent)

        def calc_doppler():

            # if not m.validate_entries(self, 1, 3): return

            if   v_entry.get() == "":
                ft = f.convert_to_Hz(ft_entry.get(), ft_unit.get())
                fd = f.convert_to_Hz(fd_entry.get(), fd_unit.get())
                v = f.doppler_v(ft, fd)

                if   v_unit.get() == "km/h" : v = f.convert_to_kmh(v, "m/s")
                elif v_unit.get() == "mi/h" : v = f.convert_to_mih(v, "m/s")

                v_entry.insert(0, f"{v}")

            elif ft_entry.get() == "":
                v  = f.convert_to_ms(v_entry.get(), v_unit.get())
                fd = f.convert_to_Hz(fd_entry.get(), fd_unit.get())
                ft = f.doppler_f(v, fd)

                if   ft_unit.get() == "GHz" : ft = f.convert_to_GHz(ft, "Hz")
                elif ft_unit.get() == "MHz" : ft = f.convert_to_MHz(ft, "Hz")
                elif ft_unit.get() == "kHz" : ft = f.convert_to_kHz(ft, "Hz")
                elif ft_unit.get() == "Hz"  : ft = f.convert_to_Hz(ft, "Hz")

                ft_entry.insert(0, f"{ft}")

            else:
                v  = f.convert_to_ms(v_entry.get(), v_unit.get())
                ft = f.convert_to_Hz(ft_entry.get(), ft_unit.get())
                fd = f.doppler_fd(v, ft)

                if   fd_unit.get() == "GHz" : fd = f.convert_to_GHz(fd, "Hz")
                elif fd_unit.get() == "MHz" : fd = f.convert_to_MHz(fd, "Hz")
                elif fd_unit.get() == "kHz" : fd = f.convert_to_kHz(fd, "Hz")
                elif fd_unit.get() == "Hz"  : fd = f.convert_to_Hz(fd, "Hz")

                fd_entry.insert(0, f"{fd}")
        
        row = 0
        col = 0
        m.create_label(self, "Doppler Theorem", row, col)

        row = 1
        col = 0
        m.create_separator(self, "horizontal", row, col, 0)

        row = 2
        col = 0
        m.create_label(self, "V : Shooter-Target Closing Velocity", row, col)
        v_entry = m.create_entry(self, row, col+1, 10)
        v_unit = tkinter.StringVar(value="m/s")
        m.create_combobox(self, v_unit, f.units_vel, row, col+2)

        row = 3
        col = 0
        m.create_label(self, "ft : Transmit Frequency", row, col)
        ft_entry = m.create_entry(self, row, col+1, 10)
        ft_unit = tkinter.StringVar(value="GHz")
        m.create_combobox(self, ft_unit, f.units_GHz, row, col+2)

        row = 4
        col = 0
        m.create_separator(self, "horizontal", row, col, 0)

        row = 5
        col = 0
        m.create_label(self, "fd : Doppler Frequency", row, col)
        fd_entry = m.create_entry(self, row, col+1, 10)
        fd_unit = tkinter.StringVar(value="GHz")
        m.create_combobox(self, fd_unit, f.units_GHz, row, col+2)

        row = 6
        col = 0
        btn_plot = tkinter.Button(self, text="Calculate", command=calc_doppler, font=m.default_font)
        btn_plot.grid(row=row+2, column=col, columnspan=2, sticky="s")
