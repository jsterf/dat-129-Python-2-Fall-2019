"""

Joe Sterf
 9/17/2019
 Python 2 - DAT-129 - Fall 2019
 Mini-program
 Week 2

"""
dictionary = {'ID': '1234', 'Student Stats':{'Semester': 'Fall', 'Class':'Algebra II', 'Grades':{'Test 1': 93, 'Test 2': 85, 'Test 3':81}}}
#create 3 empty dictionaries to use to break up main dictionary
dictionary1 = {}
dictionary2 = {}
dictionary3 = {}

#iterate through main dictionary and if there is a nested dictionary assign it to a separate dictionary
def iterate_dictionary (nested_dictionary):
    global dictionary1
    global dictionary2
    global dictionary3
    for key, value in nested_dictionary.items():
        # Python isinstance function https://www.w3schools.com/python/ref_func_isinstance.asp
        if isinstance(value, dict):
            #if value is a dictionary copy key-values to dictionary 2
            for key2, value2 in value.items():
                if isinstance(value2, dict):
            #if value in dict 2 is a dictionary copy key-values to dictionary 3
                    for key3, value3 in value2.items():

                        if isinstance(value3, dict):
                            print()
                        else:
                            dictionary3[key3] = value3
                else:
                    dictionary2[key2] = value2
        else:
            dictionary1[key] = value


#ask user for a new key-value pair to add to dictionary
def add_value():
    global dictionary1
    global dictionary2
    global dictionary3
    i = 0
    #ask user which level they want to add to
    while i != 1:
        dict_select = input('Select a level to add to: ')
        try:
            dict_select = int(dict_select)
            if dict_select == 1:
                dict_update = dictionary1
                i = 1
            elif dict_select == 2:
                dict_update = dictionary2
                i = 1
            elif dict_select == 3:
                dict_update = dictionary3
                i = 1
            else:
                print('Not a valid selection selection')
        except ValueError:
            print('Not a valid selection.')
    #ask user for key-value pair and add it to selected dictionary
    new_key = input('Enter a key: ')
    value = input('Enter a value: ')
    dict_update.update({new_key:value})

#delete user selected key-value pair
def delete_value():
    global dictionary1
    global dictionary2
    global dictionary3
#ask user which dictionary they want to delete a key from
    i = 0
    while i != 1:
        dict_select = input('Select a level to delete from: ')
        try:
            dict_select = int(dict_select)
            if dict_select == 1:
                dict_update = dictionary1
                i = 1
            elif dict_select == 2:
                dict_update = dictionary2
                i = 1
            elif dict_select == 3:
                dict_update = dictionary3
                i = 1
            else:
                print('Not a valid selection selection')
        except ValueError:
            print('Not a valid selection.')

    c  = 0
    while c != 1:
        #ask user for key to delete
        key = input('Select a key to delete: ')
        is_valid = valid(key, dict_update)
        last_item = last_value(dict_update)
        #removes items if it's a valid key and not the last one in the dictionary
        if last_item == 'True':
            print('Can\'t delete the last item in this specific dictionary.')
            c = 1
        elif is_valid == 'True':
            if dict_select == 1:
                dictionary1.pop(key)
                c = 1
            elif dict_select == 2:
                dictionary2.pop(key)
                c = 1
            else:
                dictionary3.pop(key)
                c = 1
        else:
            print('Invalid selection please choose again.')


#checks to see if key selected is in the dictionary
def valid (key, selection_dictionary):
    if key in selection_dictionary.keys():
        return 'True'
    else:
        return 'False'

#checks if selected key is the only value in the dictionary
def last_value (selection_dictionary):

    if len(selection_dictionary) == 1:
        return 'True'
    else:
        return 'False'

#print current dictionary keys
def print_dictionary(level, selection):
    print('Level', level,':')
    for key, value in selection.items():
        print(key, value)


#menu to provide user options
def menu():

    i = 0
    end = 0
    #display options
    print('1. View Dictionary')
    print('2. Add New Key-Values')
    print('3. Delete Key-Value')
    print('4. End Program')
    while i != 1:
        #ask user for selection, check if valid and then perform task if valid
        user_input = input('Make a selection: ')
        try:
            user_input = int(user_input)
            if user_input == 1:
                print_dictionary(1, dictionary1)
                print_dictionary(2, dictionary2)
                print_dictionary(3, dictionary3)

                i = 1
            elif user_input == 2 :
                add_value()
                i = 1
            elif user_input == 3 :
                delete_value()
                i = 1
            elif user_input == 4:
                i = 1
                end = 1
            else:
                print('Not a valid selection')
        except ValueError:
            print('Not a valid selection.')
    return end
def main():
    # split dictionary into 3 separate dictionaries so we can work with them
    iterate_dictionary(dictionary)
    #continue to bring up menu until user decides to stop program
    stop = 0
    while stop != 1:
        stop = menu()
        print()



if __name__ == "__main__":
    main()