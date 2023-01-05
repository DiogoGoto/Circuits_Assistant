import basic_functions as bf
import math

w = 0

def update_omega():
    global w
    w = bf.input_float("\u03C9")

def parallel_impedance():
    impedances = bf.input_list_complex("impedance")
    if 0 in impedances:
        print("0 is not a valid impedance")
        return
    if impedances == True:
        return
    print(sum([1/impedance for impedance in impedances])**(-1))

def series_impedance():
    impedances = bf.input_list_complex("impedance")
    if impedances == True:
        return
    print(sum([impedance for impedance in impedances]))

def impedace_capacitor():
    global w
    print(f"Current \u03C9: {w}")
    c = bf.input_float("capacitance")
    if c == 0:
        print('0 is not a valid capacitance')
        return
    print()    
    print(f"Zc = {1/(w*c*1j)}\u03A9")

def impedance_inductor():
    global w
    print(f"Current \u03C9: {w}")
    L = bf.input_float("inductance")
    if L == 0:
        print('0 is not a valid inductance')
        return
    print()        
    print(f"ZL = {w * L * 1j}\u03A9")

def frequency_to_omega():
    f = bf.input_float()
    print(2 * math.pi * f)

def omega_to_frequency():
    global w
    print(w / (2 * math.pi))

if __name__ == "__main__":
    parallel_impedance()
    update_omega()
    impedace_capacitor()
    impedance_inductor()