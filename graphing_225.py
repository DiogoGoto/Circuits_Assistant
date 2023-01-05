import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import time
import basic_functions as bf

#2016 Capacitor - Current(type 2)
#x = [0,6  ,6   ,12,  12,13]
#y = [0,0.4,-0.5,-0.5,0, 0]

#2016 Inductor - Current(type 1)
# type: 2 L: 0.2, Initial current: 0
x = [0,4,12,13]
y = [0,20,-12,-12]


#x = [0,2,6,7]
#y = [0,-10,10,10]

#x = [0,8,12,13]
#y= [-40,24,-24,-24]
def find_b(slope,xy):
    """Finds the b values from a y = ax + b"""
    xcord, ycord = xy
    return ycord - (slope * xcord)


def capacitor():
    current = plt.subplot(2,2,1)
    current.axhline(0,color='black')
    current.grid()
    current.set_title("Current (A)")

    voltage = plt.subplot(2,2,2,sharex= current)
    voltage.axhline(0,color='black')
    voltage.grid()
    voltage.set_title("Voltage (V)")

    power = plt.subplot(2,2,3,sharex= current)
    power.axhline(0,color='black')
    power.grid()
    power.set_title("Power (w)")

    energy = plt.subplot(2,2,4,sharex= current)
    energy.axhline(0,color='black')
    energy.grid()
    energy.set_title("Energy (J)")

    mode = input("Are you going to input a voltage(1) or a current(2) graph?: ").strip()
    while mode not in '12':
        print(f"{mode} is not a valid type")
        mode = input("Are you going to input a voltage(1) or a current(2) graph?: ").strip()
    x = bf.input_list('x')
    if x == True :
            return
    y = bf.input_list('y')
    if y == True :
            return
    
    while len(x) != len(y):
        print()
        print("You should have the same amount of values for x and y")
        print("To make a vertical line you need to add the value for x twice where there are 2 values of y")
        correction = input("Which list of values you like to correct (x or y) or (q to quit)?: ").strip().lower()
        if correction == 'x':
            x = bf.input_list('x')
        if x == True :
            return
        elif correction == 'y':
            y = bf.input_list('y')
        if y == True :
            return
        elif correction == 'q':
            return

    print()
    print("you need to close the graph to continue the program")
    time.sleep(0.3)
    if mode == '1':
        voltage.plot(x,y)
    else:
        current.plot(x,y)  
    plt.show()
    voltage.cla()
    current.cla()
    print()
    correction = input("Is this the graph you were expecting (y/n)? ").strip().lower()

    if correction == 'n':
        correction = True
    else:
        correction = 'q'

    while correction != 'q':
        correction = input("Which list of values you like to correct (x or y) or (q to quit)?: ").strip().lower()
        if correction == 'x':
            x = bf.input_list('x')
        elif correction == 'y':
            y = bf.input_list('y')
        elif correction == 'q':
            return

        print()
        print("You need to close the graph to continue the program")
        time.sleep(0.3)
        if mode == '1':
            voltage.plot(x,y)
        else:
            current.plot(x,y)        
        correction = input("Is this the graph you were expecting (y/n)? ").strip().lower()
        if correction == 'y':
            break
    voltage.cla()
    current.cla()
    print()
    c = bf.input_float("inductance")
    
    if mode == '1':
        i0 = bf.input_float("Initial Current")
    
    
    current = plt.subplot(2,2,1)
    current.axhline(0,color='black')
    current.grid()
    current.set_title("Current (A)")

    voltage = plt.subplot(2,2,2,sharex= current)
    voltage.axhline(0,color='black')
    voltage.grid()
    voltage.set_title("Voltage (V)")

    power = plt.subplot(2,2,3,sharex= current)
    power.axhline(0,color='black')
    power.grid()
    power.set_title("Power (w)")

    energy = plt.subplot(2,2,4,sharex= current)
    energy.axhline(0,color='black')
    energy.grid()
    energy.set_title("Energy (J)")
    
    if mode == 1:
        voltage.plot(x,y)
        
        t = sym.Symbol('t')
        slopes = []
        for value in range(0,len(y)-1):
            slopes.append((y[value+1]-y[value])/(x[value+1]-x[value]))
        equations = [slope*t + find_b(slope,(x[xcord],y[xcord])) for xcord, slope in enumerate(slopes)]
        voltage_eqs = equations.copy()
        equations = [c*sym.diff(equation) for equation in equations]

        interval_ini = 0
        eq = 0
        current_yvalues = []
        current_xvalues = []

        power_eqs = [volt_eq * equations[n] for n, volt_eq in enumerate(voltage_eqs)]
        power_yvalues = []

        energy_eqs = [1/2 * c * eq**2 for eq in voltage_eqs]
        energy_yvalues = []
        energy_xvalues = []

        for interval_final in x[1:]:
            current_yvalues.extend([equations[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            current_xvalues.extend(np.linspace(interval_ini,interval_final,20))
            
            power_yvalues.extend([power_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            
            energy_yvalues.extend([energy_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            energy_xvalues.extend(np.linspace(interval_ini,interval_final,20))

            interval_ini = interval_final
            eq +=1

        current.plot(current_xvalues,current_yvalues)

        power_xvalues = current_xvalues.copy()
        power.plot(power_xvalues,power_yvalues)

        energy.plot(energy_xvalues,energy_yvalues)

    if mode == 2:
        current.plot(x,y)
        v0 = list(v0)

        t = sym.Symbol('t')
        slopes = []
        for value in range(0,len(y)-1):
            if(x[value+1]-x[value]) == 0:
                continue
            slopes.append((y[value+1]-y[value])/(x[value+1]-x[value]))
       
        equations = [] 
        for xcord, slope in enumerate(slopes):
            if xcord == len(slopes)-1:
                equations.append(slope*t + find_b(slope,(sorted(list(set(x)))[xcord+1],y[xcord+2])))
                break
            equations.append(slope*t + find_b(slope,(sorted(list(set(x)))[xcord+1],y[xcord+1])))
        
        current_eqs = equations.copy()
        for n,equation in enumerate(equations.copy()):
            equations[n] = ((1/c) * sym.integrate(equation,t) ) 
            equations[n] += (equations[n].subs(t,-sorted(list(set(x)))[n]) + v0[-1]) 
            v0.append(equations[n].subs(t,sorted(list(set(x)))[n+1]))

        print('-'*50)    
        print(slopes)
        print(current_eqs)
        print(equations)

        interval_ini = 0
        eq = 0
        voltage_yvalues = []
        voltage_xvalues = []

        current_xvalues = []
        current_yvalues = []

        power_eqs = [i_eq * equations[n] for n, i_eq in enumerate(current_eqs)]
        power_xvalues = []
        power_yvalues = []

        energy_eqs = [1/2 * c * eq**2 for eq in equations]
        energy_xvalues = []
        energy_yvalues = []

        for interval_final in x[1:]:
            if interval_final == interval_ini:
                continue
            voltage_yvalues.extend([equations[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            voltage_xvalues.extend(np.linspace(interval_ini,interval_final,20))

            current_yvalues.extend([current_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            current_xvalues.extend(np.linspace(interval_ini,interval_final,20))

            power_yvalues.extend([power_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            power_xvalues.extend(np.linspace(interval_ini,interval_final,20))
            
            energy_yvalues.extend([energy_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            energy_xvalues.extend(np.linspace(interval_ini,interval_final,20))
            interval_ini = interval_final
            eq +=1
        voltage.plot(voltage_xvalues,voltage_yvalues)
        power.plot(power_xvalues,power_yvalues)
        energy.plot(energy_xvalues,energy_yvalues)

    plt.show()

def inductor():
    current = plt.subplot(2,2,1)
    current.axhline(0,color='black')
    current.grid()
    current.set_title("Current (A)")

    voltage = plt.subplot(2,2,2,sharex= current)
    voltage.axhline(0,color='black')
    voltage.grid()
    voltage.set_title("Voltage (V)")

    power = plt.subplot(2,2,3,sharex= current)
    power.axhline(0,color='black')
    power.grid()
    power.set_title("Power (w)")

    energy = plt.subplot(2,2,4,sharex= current)
    energy.axhline(0,color='black')
    energy.grid()
    energy.set_title("Energy (J)")

    mode = input("Are you going to input a voltage(1) or a current(2) graph?: ").strip()
    while mode not in '12':
        print(f"{mode} is not a valid type")
        mode = input("Are you going to input a voltage(1) or a current(2) graph?: ").strip()
    x = bf.input_list('x')
    if x == True :
            return
    y = bf.input_list('y')
    if y == True :
            return
    
    while len(x) != len(y):
        print()
        print("You should have the same amount of values for x and y")
        print("To make a vertical line you need to add the value for x twice where there are 2 values of y")
        correction = input("Which list of values you like to correct (x or y) or (q to quit)?: ").strip().lower()
        if correction == 'x':
            x = bf.input_list('x')
        if x == True :
            return
        elif correction == 'y':
            y = bf.input_list('y')
        if y == True :
            return
        elif correction == 'q':
            return

    print()
    print("you need to close the graph to continue the program")
    time.sleep(0.3)
    if mode == '1':
        voltage.plot(x,y)
    else:
        current.plot(x,y)  
    plt.show()
    
    voltage.cla()
    current.cla()
    print()
    correction = input("Is this the graph you were expecting (y/n)? ").strip().lower()

    if correction == 'n':
        correction = True
    else:
        correction = 'q'

    while correction != 'q':
        correction = input("Which list of values you like to correct (x or y) or (q to quit)?: ").strip().lower()
        if correction == 'x':
            x = bf.input_list('x')
        elif correction == 'y':
            y = bf.input_list('y')
        elif correction == 'q':
            return

        while len(x) != len(y):
            print()
            print("You should have the same amount of values for x and y")
            print("To make a vertical line you need to add the value for x twice where there are 2 values of y")
            correction = input("Which list of values you like to correct (x or y) or (q to quit)?: ").strip().lower()
            if correction == 'x':
                x = bf.input_list('x')
            if x == True :
                return
            elif correction == 'y':
                y = bf.input_list('y')
            if y == True :
                return
            elif correction == 'q':
                return

        print()
        print("You need to close the graph to continue the program")
        time.sleep(0.3)
        print(mode, type(mode), mode == '2',1)
        if mode == '1':
            voltage.plot(x,y)
            plt.show()
            print(1)
        else:
            print(2)
            current.plot(x,y)  
            plt.show()      
        plt.show()
        correction = input("Is this the graph you were expecting (y/n)? ").strip().lower()
        if correction == 'y':
            break
        voltage.cla()
        current.cla()
    voltage.cla()
    current.cla()
    print()
    L = bf.input_float("inductance")
    
    if mode == '1':
        i0 = bf.input_float("Initial Current")
    
    
    current = plt.subplot(2,2,1)
    current.axhline(0,color='black')
    current.grid()
    current.set_title("Current (A)")

    voltage = plt.subplot(2,2,2,sharex= current)
    voltage.axhline(0,color='black')
    voltage.grid()
    voltage.set_title("Voltage (V)")

    power = plt.subplot(2,2,3,sharex= current)
    power.axhline(0,color='black')
    power.grid()
    power.set_title("Power (w)")

    energy = plt.subplot(2,2,4,sharex= current)
    energy.axhline(0,color='black')
    energy.grid()
    energy.set_title("Energy (J)")

    if mode == '1':
        voltage.plot(x,y)
        i0 = list(i0)

        t = sym.Symbol('t')
        slopes = []
        for value in range(0,len(y)-1):
            if(x[value+1]-x[value]) == 0:
                continue
            slopes.append((y[value+1]-y[value])/(x[value+1]-x[value]))
       
        equations = [] 
        for xcord, slope in enumerate(slopes):
            if xcord == len(slopes)-1:
                equations.append(slope*t + find_b(slope,(sorted(list(set(x)))[xcord+1],y[xcord+1])))
                break
            equations.append(slope*t + find_b(slope,(sorted(list(set(x)))[xcord+1],y[xcord+1])))
        
        current_eqs = equations.copy()
        for n,equation in enumerate(equations.copy()):
            equations[n] = ((1/L) * sym.integrate(equation,t) ) 
            equations[n] += (equations[n].subs(t,-sorted(list(set(x)))[n]) + i0[-1]) 
            i0.append(equations[n].subs(t,sorted(list(set(x)))[n+1]))



        interval_ini = 0
        eq = 0
        voltage_yvalues = []
        voltage_xvalues = []

        current_xvalues = []
        current_yvalues = []

        power_eqs = [i_eq * equations[n] for n, i_eq in enumerate(current_eqs)]
        power_xvalues = []
        power_yvalues = []

        energy_eqs = [1/2 * L * eq**2 for eq in equations]
        energy_xvalues = []
        energy_yvalues = []

        for interval_final in x[1:]:
            if interval_final == interval_ini:
                continue
            voltage_yvalues.extend([equations[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            voltage_xvalues.extend(np.linspace(interval_ini,interval_final,20))

            current_yvalues.extend([current_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            current_xvalues.extend(np.linspace(interval_ini,interval_final,20))

            power_yvalues.extend([power_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            power_xvalues.extend(np.linspace(interval_ini,interval_final,20))
            
            energy_yvalues.extend([energy_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            energy_xvalues.extend(np.linspace(interval_ini,interval_final,20))
            interval_ini = interval_final
            eq +=1
        current.plot(voltage_xvalues,voltage_yvalues)
        power.plot(power_xvalues,power_yvalues)
        energy.plot(energy_xvalues,energy_yvalues)


    if mode == '2':
        current.plot(x,y)
        
        t = sym.Symbol('t')
        slopes = []
        for value in range(0,len(y)-1):
            slopes.append((y[value+1]-y[value])/(x[value+1]-x[value]))
        equations = [slope*t + find_b(slope,(x[xcord],y[xcord])) for xcord, slope in enumerate(slopes)]
        current_eqs = equations.copy()
        equations = [L*sym.diff(equation) for equation in equations]

        interval_ini = 0
        eq = 0
        voltage_yvalues = []
        voltage_xvalues = []

        power_eqs = [volt_eq * equations[n] for n, volt_eq in enumerate(current_eqs)]
        power_yvalues = []

        energy_eqs = [1/2 * L * eq**2 for eq in current_eqs]
        energy_yvalues = []
        energy_xvalues = []

        for interval_final in x[1:]:
            voltage_yvalues.extend([equations[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            voltage_xvalues.extend(np.linspace(interval_ini,interval_final,20))
            
            power_yvalues.extend([power_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            
            energy_yvalues.extend([energy_eqs[eq].subs(t,tvalue) for tvalue in np.linspace(interval_ini,interval_final,20)])
            energy_xvalues.extend(np.linspace(interval_ini,interval_final,20))

            interval_ini = interval_final
            eq +=1

        voltage.plot(voltage_xvalues,voltage_yvalues)

        power_xvalues = voltage_xvalues.copy()
        power.plot(power_xvalues,power_yvalues)

        energy.plot(energy_xvalues,energy_yvalues)

    plt.show()

if __name__ == "__main__":
    #print(input_float('x'))
    #capacitor_i(2,x,y,0.1,1.4)
    inductor()