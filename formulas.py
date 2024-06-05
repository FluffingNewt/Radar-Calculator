import math

units_NMI  = ["NMI", "mi", "m", "ft"]
units_dBW  = ["dBW", "dBm", "W", "mW"]
units_rcs  = ["m\u00B2"]
units_GHz  = ["GHz", "MHz", "Hz", "kHz"]


def convert_to_NMI(value, unit):
    value = float(value)
    if   unit == "mi" : return value * 0.868976242
    elif unit == "m"  : return value / 1852.0
    elif unit == "ft" : return value * (1.64578834 * 10.0e-4)
    else              : return value # Passthrough


def convert_to_mi(value, unit):
    value = float(value)
    if   unit == "NMI" : return value * 1.15078
    elif unit == "m"   : return value * 6.21e-4
    elif unit == "ft"  : return value / 5280
    else               : return value # Passthrough


def convert_to_m(value, unit):
    value = float(value)
    if   unit == "NMI" : return value * 1852
    elif unit == "mi"  : return value * 1609.344
    elif unit == "ft"  : return value * 0.3048
    else               : return value # Passthrough


def convert_to_ft(value, unit):
    value = float(value)
    if   unit == "NMI" : return value * 6076.12
    elif unit == "mi"  : return value * 5280 
    elif unit == "m"   : return value * 3.28084
    else               : return value # Passthrough


def convert_to_dBW(value, unit):
    value = float(value)
    if   unit == "dBm" : return value - 30.0
    elif unit == "W"   : return 10 * math.log10(value)
    elif unit == "mW"  : return 10 * math.log10(value / 1000.0)
    else               : return value # Passthrough


def convert_to_dBm(value, unit):
    value = float(value)
    if   unit == "dBW" : return value + 30.0
    elif unit == "W"   : return 10 * math.log10(value * 1000.0)
    elif unit == "mW"  : return 10 * math.log10(value / 1000.0)
    else               : return value # Passthrough


def convert_to_W(value, unit):
    value = float(value)
    if   unit == "dBW" : return math.pow(10, value / 10.0)
    elif unit == "dBm" : return math.pow(10, value / 10.0) / 1000.0
    elif unit == "mW"  : return value / 1000.0
    else               : return value  # Passthrough


def convert_to_mW(value, unit):
    value = float(value)
    if unit != "mW" : return convert_to_W(value, unit) * 1000.0
    else            : return value  # Passthrough


def convert_to_Hz(value, unit):
    value = float(value)
    if   unit == "GHz" : return value * 1.0e9
    elif unit == "MHz" : return value * 1.0e6
    elif unit == "kHz" : return value * 1.0e3
    else               : return value # Passthrough


def rre(pwr_t, gain_t, gain_r, freq, rcs, range):
    wavelength = 299792458.0 / freq
    numer = pwr_t * gain_t * gain_r * (wavelength ** 2) * rcs
    denom = (4 * math.pi) ** 3 * (range ** 4)
    return numer / denom

