import graphing_225
import AC_assistant
import DC_Assistant
import PySimpleGUI as psg

def print_menu():
    print(f"{'Menu':^50}")
    print('-'*50)
    print("1 - Graphing inductors and capacitors")
    print("2 - AC Assistant")
    print('3 - DC Assistant')
    print()

def print_graphing_menu():
    print(f"{'Graphing Menu':^50}")
    print('-'*50)
    print('1 - Plots i, v, p, e of an inductor')
    print('2 - Plots i, v, p, e of a capacitor')
    print()

def print_ac_assistant_menu():
    print(f"{'AC Assistant Menu':^50}")
    print('-'*50)
    print('1 - Combine impedance in seires')
    print('2 - Combine impedances in parallel')
    print('3 - Calculates the impedance of a capacitor')
    print('4 - Calculates the impedance of an inductor')
    print('5 - Updates \u03C9')
    print('6 - Hz to \u03C9')
    print('7 - \u03C9 to Hz ')
    print()

def print_dc_assistant_menu():
    print(f"{'DC Assistant Menu':^50}")
    print('-'*50)
    print('1 - Combine Resistance in parallel')
    print('2 - Combine Resistance in series')
    print()

def invalid_command():
    print("Invalid Commnand")

def invalid_app():
    print("Invalid App")


functions = {
        '1': {'1':graphing_225.inductor,
              '2': graphing_225.capacitor,
              'menu': print_graphing_menu,
             },
        '2': {'1': AC_assistant.series_impedance,
              '2': AC_assistant.parallel_impedance,
              '3': AC_assistant.impedace_capacitor,
              '4': AC_assistant.impedance_inductor,
              '5': AC_assistant.update_omega,
              '6': AC_assistant.frequency_to_omega,
              '7': AC_assistant.omega_to_frequency,

              'menu': print_ac_assistant_menu,
             },
        '3':{'1':DC_Assistant.parallel_resistance,
             '2':DC_Assistant.series_resistance,},       
            }

print_menu()

app = input("Select the App you want to use (q to quit): ").strip()
command = invalid_command

while not(app == 'q' or command == 'q'):
    if app in functions:
        functions[app]['menu']()
        command = input("Enter the number of the command (q to quit): ").strip()
        if command == 'q':
            break
        command = functions[app].get(command,invalid_command)
        print()
        command()
        print()

    elif app == 'q':
        break
    else:
        invalid_app()
    print_menu()
    app = input("Select the App you want to use (q to quit): ").strip()
        
 
print()
print(f"{'Thanks for Using Circuits Assistant':^175}")
print(f"{'All Rights Reserverd':^175}")