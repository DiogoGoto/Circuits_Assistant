import basic_functions as bf

def parallel_resistance():
    resistances = bf.input_list("resistances")
    if 0 in resistances:
        print("0 is not a valid resistance")
        return
    if resistances == True:
        return
    print(sum([1/resistor for resistor in resistances])**(-1))

def series_resistance():
    resitances = bf.input_list("Resistances")
    if resitances == True:
        return
    print(sum([resistor for resistor in resitances]))


