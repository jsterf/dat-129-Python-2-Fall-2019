"""

Joe Sterf
 9/11/2019
 Python 2 - DAT-129 - Fall 2019
 Mini-program
 Week 2

"""
dictionary = {'make':'Chevrolet', 'models' : {'car' : {'name':'Malibu','MPG':'30'}, 'SUV':{'name': 'Equinox', 'MPG':'23'}}}

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
    for k in selection:
        print(k)

#print key value
def print_values (dictionary, selection):
    print(dictionary[selection])


#select key
def select_key (dictionary):
    i = 0
    while i == 0:
        key_selected = input('Select a key to view it\'s values: ')
        if valid(key_selected) == 'True':
            print_values(dictionary, key_selected)
            i =1
        else:
            print('Not a valid key, please select again.')


def main():
    print_dictionary(dictionary)
    select_key(dictionary)

if __name__ == "__main__":
    main()