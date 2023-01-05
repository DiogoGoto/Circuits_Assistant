def input_list(name):
    my_list = input(f"Please enter all the important {name} values separated by spaces: ").strip().split()
    valid_character = '0123456789.-'

    list_type = False
    q = False

    while not(list_type and q):
        for index,number in enumerate(my_list.copy()):
            invalid_number = False
            if type(number) == float:
                continue
            for digit in number:
                if digit not in valid_character:
                    print(f"{number} is an invalid number")
                    invalid_number = True
                    break
            if invalid_number:
                break
            my_list[index] = float(my_list[index])
        
        for index,number in enumerate(my_list.copy()):
            q = False
            if type(number) != float:
                user_input = (input(f"Enter the new value to substitute {my_list[index]} (or q to stop): "))
                if user_input == 'q':
                    q = True
                    return q
                my_list[index] = user_input
                break
            list_type = True
            q = True

    
    return my_list

def input_float(name):
    valid_character = '0123456789.-'
    number = input(f"Enter the value for {name}: ")
    while type(number) != float:
        valid_number = True
        for digit in number or number == '':
            if digit not in valid_character:
                print(f"{number} is an invalid number")
                valid_number = False
                break
        if valid_number:
            return float(number)
        number = input(f"Enter the value for {name}: ")

def input_list_complex(name):
    my_list = input(f"Please enter all {name} values separated by spaces: ").strip().split()
    valid_character = '0123456789.-j'

    list_type = False
    q = False

    while not(list_type and q):
        for index,number in enumerate(my_list.copy()):
            invalid_number = False
            if type(number) == float or type(number) == complex:
                continue
            for digit in number:
                if digit not in valid_character:
                    print(f"{number} is an invalid number")
                    invalid_number = True
                    break
            if invalid_number:
                break
            if 'j' in number:
                if number.index('j') != len(number) :
                    my_list[index] = my_list[index].replace('j','')
                    my_list[index] += 'j'
                my_list[index] = complex(my_list[index])
            else:
                my_list[index] = float(my_list[index])
        
        for index,number in enumerate(my_list.copy()):
            q = False
            if (type(number) != float and type(number) != complex):
                user_input = (input(f"Enter the new value to substitute {my_list[index]} (or q to stop): "))
                if user_input == 'q':
                    q = True
                    return q
                my_list[index] = user_input
                break
            list_type = True
            q = True

    
    return my_list