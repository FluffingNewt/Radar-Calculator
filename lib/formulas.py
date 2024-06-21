import math

units_NMI  = ["NMI", "mi", "m", "ft"]
units_dBW  = ["dBW", "dBm", "W", "mW"]
units_GHz  = ["GHz", "MHz", "Hz", "kHz"]
units_rcs  = ["m\u00B2", "ft\u00B2"]
units_vel  = ["m/s"]


c = 299792458.0

#!###### Unit Conversions #####!#

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
    elif unit == "mW"  : return 10 * math.log10(value)
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
    elif unit == "Hz"  : return value / 1.0e3
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

#!###### Linear RRE Formulas ######!#

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

#!###### Linear RRE Jammer Formulas ######!#

def rre_j_pr(pt, gt, gr, f, r, lt, la, lr):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w**2)
    denom = (4 * math.pi)**2 * (r**2) * lt * la * lr
    return numer / denom


def rre_j_pt(pr, gt, gr, f, r, lt, la, lr):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**2 * (r**2) * lt * la * lr
    denom =  gt * gr * (w**2)
    return numer / denom


def rre_j_gt(pr, pt, gr, f, r, lt, la, lr):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**2 * (r**2) * lt * la * lr
    denom =  pt * gr * (w**2)
    return numer / denom


def rre_j_gr(pr, pt, gt, f, r, lt, la, lr):
    w = 299792458.0 / f
    numer = pr * (4 * math.pi)**2 * (r**2) * lt * la * lr
    denom =  pt * gt * (w**2)
    return numer / denom


def rre_j_f(pr, pt, gt, gr, r, lt, la, lr):
    numer = pr * (4 * math.pi)**2 * (r**2) * lt * la * lr
    denom =  pt * gt * gr
    return 299792458.0 / ((numer / denom)**0.5)


def rre_j_r(pr, pt, gt, gr, f, lt, la, lr):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w ** 2)
    denom =  pr * (4 * math.pi)**2 * lt * la * lr
    return (numer / denom)**0.5


def rre_j_lt(pr, pt, gt, gr, f, r, la, lr):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w**2)
    denom = pr * (4 * math.pi)**2 * (r**2) * la * lr
    return numer / denom


def rre_j_la(pr, pt, gt, gr, f, r, lt, lr):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w**2)
    denom = pr * (4 * math.pi)**2 * (r**2) * lt * lr
    return numer / denom


def rre_j_lr(pr, pt, gt, gr, f, r, lt, la):
    w = 299792458.0 / f
    numer = pt * gt * gr * (w**2)
    denom = pr * (4 * math.pi)**2 * (r**2) * lt * la
    return numer / denom

#!###### Logarithmic RRE Formulas ######!#

def rre_log_pr(pt, gt, gr, f, rcs, r):
    return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 20 * math.log10(c) + 10 * math.log10(rcs) - 30 * math.log10(4 * math.pi) - 20 * math.log10(f) - 40 * math.log10(r)

def rre_log_pt(pr, gt, gr, f, rcs, r):
    return 10 * math.log10(pr) - 10 * math.log10(gt) - 10 * math.log10(gr) - 20 * math.log10(c) - 10 * math.log10(rcs) + 30 * math.log10(4 * math.pi) + 20 * math.log10(f) + 40 * math.log10(r)

def rre_log_gt(pr, pt, gr, f, rcs, r):
    return 10 * math.log10(pr) - 10 * math.log10(pt) - 10 * math.log10(gr) - 20 * math.log10(c) - 10 * math.log10(rcs) + 30 * math.log10(4 * math.pi) + 20 * math.log10(f) + 40 * math.log10(r)

def rre_log_gr(pr, pt, gt, f, rcs, r):
    return 10 * math.log10(pr) - 10 * math.log10(pt) - 10 * math.log10(gt) - 20 * math.log10(c) - 10 * math.log10(rcs) + 30 * math.log10(4 * math.pi) + 20 * math.log10(f) + 40 * math.log10(r)

def rre_log_rcs(pr, pt, gt, gr, f, r):
    return 10 * math.log10(pr) - 10 * math.log10(pt) - 10 * math.log10(gt) - 10 * math.log10(gr) - 20 * math.log10(c) + 30 * math.log10(4 * math.pi) + 20 * math.log10(f) + 40 * math.log10(r)

def rre_log_f(pr, pt, gt, gr, rcs, r):
    freq = 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 20 * math.log10(c) + 10 * math.log10(rcs) - 10 * math.log10(pr) - 30 * math.log10(4 * math.pi) - 40 * math.log10(r)
    return freq / 2

def rre_log_r(pr, pt, gt, gr, f, rcs):
    r = 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 20 * math.log10(c) + 10 * math.log10(rcs) - 10 * math.log10(pr) - 30 * math.log10(4 * math.pi) - 20 * math.log10(f)
    return r / 4

#!###### Logarithmic RRE Jammer Formulas ######!#

def rre_log_j_pr(pt, gt, gr, f, r, lt, la, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(lt) - 10 * math.log10(la) - 10 * math.log10(lr)

def rre_log_j_pt(pr, gt, gr, f, r, lt, la, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) - 10 * math.log10(gt) - 10 * math.log10(gr) - 2 * wavelength + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr)

def rre_log_j_gt(pr, pt, gr, f, r, lt, la, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) - 10 * math.log10(pt) - 10 * math.log10(gr) - 2 * wavelength + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr)

def rre_log_j_gr(pr, pt, gt, f, r, lt, la, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) - 10 * math.log10(pt) - 10 * math.log10(gt) - 2 * wavelength + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr)

def rre_log_j_f(pr, pt, gt, gr, r, lt, la, lr):
    wavelength = 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr) - 10 * math.log10(pt) - 10 * math.log10(gt) + 10 * math.log10(gr)
    return 10 * math.log10(c) - 0.5 * wavelength

def rre_log_j_r(pr, pt, gt, gr, f, lt, la, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 0.5 * (10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 10 * math.log10(lt) - 10 * math.log10(la) - 10 * math.log10(lr))

def rre_log_j_lt(pr, pt, gt, gr, f, r, la, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(la) - 10 * math.log10(lr)

def rre_log_j_la(pr, pt, gt, gr, f, r, lt, lr):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(lt) - 10 * math.log10(lr)

def rre_log_j_lr(pr, pt, gt, gr, f, r, lt, la):
    wavelength = 10 * math.log10(c) - 10 * math.log10(f)
    return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(lt) - 10 * math.log10(la)

#! Doppler Equation

def doppler_v(fd, f):
    return (fd * c) / (2 * f)

def doppler_f(fd, v):
    return (fd * c) / (2 * v)

def doppler_fd(v, f):
    return (2 * v * f) / c