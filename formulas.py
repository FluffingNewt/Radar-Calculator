import math

units_NMI  = ["NMI", "mi", "m", "ft"]
units_dBW  = ["dBW", "dBm", "W", "mW"]
units_GHz  = ["GHz", "MHz", "Hz", "kHz"]
units_rcs  = ["m\u00B2", "ft\u00B2"]


###### Conversions ######

def convert_to_NMI(value, unit):
    value = float(value)
    if   unit == "mi" : return value / 1.15078
    elif unit == "m"  : return value / 1852.0
    elif unit == "ft" : return value / 6076.11549
    else              : return value # Passthrough


def convert_to_mi(value, unit):
    value = float(value)
    if   unit == "NMI" : return value * 1.15078
    elif unit == "m"   : return value / 1609.344
    elif unit == "ft"  : return value / 5280.0
    else               : return value # Passthrough


def convert_to_m(value, unit):
    value = float(value)
    if   unit == "NMI" : return value * 1852.0
    elif unit == "mi"  : return value * 1609.344
    elif unit == "ft"  : return value * 0.3048
    else               : return value # Passthrough


def convert_to_ft(value, unit):
    value = float(value)
    if   unit == "NMI" : return value * 6076.11549
    elif unit == "mi"  : return value * 5280.0
    elif unit == "m"   : return value / 0.3048
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


def convert_to_GHz(value, unit):
    value = float(value)
    if   unit == "MHz" : return value / 1.0e3
    elif unit == "kHz" : return value / 1.0e6
    elif unit == "Hz"  : return value / 1.0e9
    else               : return value # Passthrough


def convert_to_MHz(value, unit):
    value = float(value)
    if   unit == "GHz" : return value * 1.0e3
    elif unit == "kHz" : return value / 1.0e3
    elif unit == "Hz"  : return value / 1.0e6
    else               : return value # Passthrough


def convert_to_kHz(value, unit):
    value = float(value)
    if   unit == "GHz" : return value * 1.0e6
    elif unit == "MHz" : return value * 1.0e3
    elif unit == "Hz" : return value / 1.0e3
    else               : return value # Passthrough


def convert_to_Hz(value, unit):
    value = float(value)
    if   unit == "GHz" : return value * 1.0e9
    elif unit == "MHz" : return value * 1.0e6
    elif unit == "kHz" : return value * 1.0e3
    else               : return value # Passthrough


def convert_to_m2(value, unit):
    value = float(value)
    if   unit == "ft\u00B2" : return value / 10.7639
    else                    : return value # Passthrough


def convert_to_ft2(value, unit):
    value = float(value)
    if   unit == "m\u00B2" : return value * 10.7639
    else                   : return value # Passthrough

####### Formulas #######

def rre_pr(pt, gt, gr, f, rcs, r):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w**2) * rcs
    denom = (4 * math.pi)**3 * (r**4)
    return numer / denom


def rre_pt(pr, gt, gr, f, rcs, r):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**3 * (r**4)
    denom =  gt * gr * (w**2) * rcs
    return numer / denom


def rre_gt(pr, pt, gr, f, rcs, r):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**3 * (r**4)
    denom =  pt * gr * (w**2) * rcs
    return numer / denom


def rre_gr(pr, pt, gt, f, rcs, r):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**3 * (r**4)
    denom =  pt * gt * (w**2) * rcs
    return numer / denom


def rre_f(pr, pt, gt, gr, rcs, r):
    numer = pr * (4 * math.pi)**3 * (r**4)
    denom =  pt * gt * gr * rcs
    return 299792458.0 / ((numer / denom)**0.5)


def rre_rcs(pr, pt, gt, gr, f, r):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**3 * (r**4)
    denom =  pt * gt * gr * (w**2)
    return numer / denom


def rre_r(pr, pt, gt, gr, f, rcs):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w ** 2) * rcs
    denom =  pr * (4 * math.pi)**3
    return (numer / denom)**0.25