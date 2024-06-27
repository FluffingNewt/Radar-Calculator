import math

units_range  = ["NMI", "mi", "m", "ft"]
units_pwr  = ["dBW", "dBm", "W"]
units_freq  = ["GHz", "MHz", "Hz", "kHz"]
units_area  = ["m\u00B2", "ft\u00B2"]
units_vel  = ["m/s", "km/h", "mi/h", "knots"]
units_time = ["ms", "s", "min", "hr"]

c = 299792458.0

#!###### Unit Conversions #####!#

# Range
def convert_to_NMI(value, unit):
    if value == "": return ""

    value = float(value)
    if   unit == "mi" : return value / 1.15078
    elif unit == "m"  : return value / 1852.0
    elif unit == "ft" : return value / 6076.11549
    else              : return value # Passthrough


def convert_to_mi(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "NMI" : return value * 1.15078
    elif unit == "m"   : return value / 1609.344
    elif unit == "ft"  : return value / 5280.0
    else               : return value # Passthrough


def convert_to_m(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "NMI" : return value * 1852.0
    elif unit == "mi"  : return value * 1609.344
    elif unit == "ft"  : return value * 0.3048
    else               : return value # Passthrough


def convert_to_ft(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "NMI" : return value * 6076.11549
    elif unit == "mi"  : return value * 5280.0
    elif unit == "m"   : return value / 0.3048
    else               : return value # Passthrough

# Power
def convert_to_dBW(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "dBm" : return value - 30.0
    elif unit == "W"   : return 10 * math.log10(value)
    else               : return value # Passthrough


def convert_to_dBm(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "dBW" : return value + 30.0
    elif unit == "W"   : return 10 * math.log10(value * 1000.0)
    else               : return value # Passthrough


def convert_to_W(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "dBW" : return math.pow(10, value / 10.0)
    elif unit == "dBm" : return math.pow(10, value / 10.0) / 1000.0
    else               : return value  # Passthrough

# Frequency
def convert_to_GHz(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "MHz" : return value / 1.0e3
    elif unit == "kHz" : return value / 1.0e6
    elif unit == "Hz"  : return value / 1.0e9
    else               : return value # Passthrough


def convert_to_MHz(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "GHz" : return value * 1.0e3
    elif unit == "kHz" : return value / 1.0e3
    elif unit == "Hz"  : return value / 1.0e6
    else               : return value # Passthrough


def convert_to_kHz(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "GHz" : return value * 1.0e6
    elif unit == "MHz" : return value * 1.0e3
    elif unit == "Hz"  : return value / 1.0e3
    else               : return value # Passthrough


def convert_to_Hz(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "GHz" : return value * 1.0e9
    elif unit == "MHz" : return value * 1.0e6
    elif unit == "kHz" : return value * 1.0e3
    else               : return value # Passthrough

# RCS
def convert_to_m2(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "ft\u00B2" : return value / 10.7639
    else                    : return value # Passthrough


def convert_to_ft2(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "m\u00B2" : return value * 10.7639
    else                   : return value # Passthrough

# Velocity
def convert_to_ms(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "km/h"  : return value / 3.6
    elif unit == "mi/h"  : return value * 0.44704
    elif unit == "knots" : return value / 1.944
    else                 : return value  # Passthrough


def convert_to_kmh(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "m/s"   : return value * 3.6
    elif unit == "mi/h"  : return value * 1.60934
    elif unit == "knots" : return value * 1.852
    else                 : return value  # Passthrough


def convert_to_mih(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "m/s"   : return value * 2.23694
    elif unit == "km/h"  : return value / 1.60934
    elif unit == "knots" : return value * 1.151
    else                 : return value  # Passthrough


def convert_to_knots(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "m/s"   : return value * 1.944
    elif unit == "km/h"  : return value / 1.852
    elif unit == "mi/h"  : return value / 1.151
    else                 : return value  # Passthrough

# Time
def convert_to_ms(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "s"   : return value * 1000
    elif unit == "min" : return value * 60000
    elif unit == "hr"  : return value * 3600000
    else               : return value  # Passthrough

def convert_to_s(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "ms"  : return value / 1000
    elif unit == "min" : return value * 60
    elif unit == "hr"  : return value * 3600
    else               : return value  # Passthrough

def convert_to_min(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "ms" : return value / 60000
    elif unit == "s"  : return value / 60
    elif unit == "hr" : return value * 60
    else              : return value  # Passthrough

def convert_to_hr(value, unit):
    if value == "": return ""
    
    value = float(value)
    if   unit == "ms"  : return value / 3600000
    elif unit == "s"   : return value / 3600
    elif unit == "min" : return value / 60
    else               : return value  # Passthrough

def convert_to_log(value):
    return 10 * math.log10(value)

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

# def rre_log_j_pr(pt, gt, gr, f, r, lt, la, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(lt) - 10 * math.log10(la) - 10 * math.log10(lr)

# def rre_log_j_pt(pr, gt, gr, f, r, lt, la, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) - 10 * math.log10(gt) - 10 * math.log10(gr) - 2 * wavelength + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr)

# def rre_log_j_gt(pr, pt, gr, f, r, lt, la, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) - 10 * math.log10(pt) - 10 * math.log10(gr) - 2 * wavelength + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr)

# def rre_log_j_gr(pr, pt, gt, f, r, lt, la, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) - 10 * math.log10(pt) - 10 * math.log10(gt) - 2 * wavelength + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr)

# def rre_log_j_f(pr, pt, gt, gr, r, lt, la, lr):
#     wavelength = 10 * math.log10(pr) + 20 * math.log10(4 * math.pi) + 20 * math.log10(r) + 10 * math.log10(lt) + 10 * math.log10(la) + 10 * math.log10(lr) - 10 * math.log10(pt) - 10 * math.log10(gt) + 10 * math.log10(gr)
#     return 10 * math.log10(c) - 0.5 * wavelength

# def rre_log_j_r(pr, pt, gt, gr, f, lt, la, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 0.5 * (10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 10 * math.log10(lt) - 10 * math.log10(la) - 10 * math.log10(lr))

# def rre_log_j_lt(pr, pt, gt, gr, f, r, la, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(la) - 10 * math.log10(lr)

# def rre_log_j_la(pr, pt, gt, gr, f, r, lt, lr):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(lt) - 10 * math.log10(lr)

# def rre_log_j_lr(pr, pt, gt, gr, f, r, lt, la):
#     wavelength = 10 * math.log10(c) - 10 * math.log10(f)
#     return 10 * math.log10(pt) + 10 * math.log10(gt) + 10 * math.log10(gr) + 2 * wavelength - 10 * math.log10(pr) - 20 * math.log10(4 * math.pi) - 20 * math.log10(r) - 10 * math.log10(lt) - 10 * math.log10(la)

#!###### Doppler Formulas ######!#

def doppler_vs(fd, ft, vt):
    fd = float(fd)
    ft = float(ft)
    vt = float(vt)

    return (fd * c) / (2 * ft) - vt

def doppler_vt(fd, ft, vs):
    fd = float(fd)
    ft = float(ft)
    vs = float(vs)
    
    return (fd * c) / (2 * ft) - vs

def doppler_ft(fd, vs, vt):
    fd = float(fd)
    vs = float(vs)
    vt = float(vt)
    
    return (fd * c) / (2 * (vs + vt))

def doppler_fd(vs, vt, ft):
    vs = float(vs)
    vt = float(vt)
    ft = float(ft)

    return (2 * (vs + vt) * ft) / c

#!###### Unambiguous Range Formulas ######!#

def unam_range_prf(r):
    r = float(r)

    return c / (2 * r)

def unam_range_pri(r):
    r = float(r)
    
    return (2 * r) / c

def unam_range_rPRF(prf):
    prf = float(prf)
    
    return c / (2 * prf)

def unam_range_rPRI(pri):
    pri = float(pri)
    
    return (c * pri) / 2