"""

Joe Sterf
 9/11/2019
 Python 2 - DAT-129 - Fall 2019
 Mini-program
 Week 2

"""
dictionary = {'ID': '1234', 'Student Stats':{'Semester': 'Fall', 'Class':'Algebra II', 'Grades':{'Test 1': 93, 'Test 2': 85, 'Test 3':81}}}

#ask user for a new key-value pair to add to dictionary
def add_value():
    new_key = input('Enter a key: ')
    value = input('Enter a value: ')
    dictionary.update({new_key:value})

#delete user selected key-value pair
def delete_value():
    key = input('Select a key to delete: ')
    is_valid = valid(key)
    last_item = last_value()
    #removes items if it's a valid key and not the last one in the dictionary
    if last_item == 'True':
        print('Can\'t delete the last item.')
    elif is_valid == 'True':
        dictionary.pop(key)
    else:
        print('Invalid selection please choose again.')
        delete_value()

#checks to see if key selected is in the dictionary
def valid (key):
    if key in dictionary.keys():
        return 'True'
    else:
        return 'False'

#checks if selected key is the only value in the dictionary
def last_value ():

    if len(dictionary) == 1:
        return 'True'
    else:
        return 'False'

#print current dictionary keys
def print_dictionary(selection):
    for key, value in selection.items():
        print(key, value)
#Python isinstance function https://www.w3schools.com/python/ref_func_isinstance.asp
    #for key, value in selection.items():
     #   if isinstance(value, dict):

      #      for key2, value2 in value.items():
       #         if isinstance(value2, dict):

        #            for key3, value3 in value2.items():

         #               if isinstance(value3, dict):
          #                  print()
           #             else:
            #                print(key3, value3)
             #   else:
              #      print(key2, value2)
        #else:
         #   print(key, value)




#prints values for selected key
def print_values (dictionary_temp, selection):
    print(dictionary_temp[selection])


#select key to print values, makes sure its a valid key first
def select_key (dictionary_temp):
    i = 0
    while i == 0:
        key_selected = input('Select a key to view it\'s values: ')
        if valid(key_selected) == 'True':
            print_values(dictionary_temp, key_selected)
            i =1
        else:
            print('Not a valid key, please select again.')

#menu to provide user options
def menu():
    i = 0
    end = 0
    print('1. View Dictionary')
    print('2. Add New Key-Values')
    print('3. Delete Key-Value')
    print('4. End Program')
    while i != 1:
        user_input = input('Make a selection: ')
        try:
            user_input = int(user_input)
            if user_input == 1:
                print_dictionary(dictionary)
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
    #continue to bring up menu until user decides to stop program
    stop = 0
    while stop != 1:
        stop = menu()
        print()



if __name__ == "__main__":
    main()