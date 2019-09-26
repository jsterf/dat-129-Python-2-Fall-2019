"""

Joe Sterf
 9/25/2019
 Python 2 - DAT-129 - Fall 2019
 File Practice
 Week 4

"""

import os

#open file in read mode
read_file = open('names.txt', 'r')
#create blank list to read names into
names = []
#names ={}
def load_file(file):
    name =  read_file.readline()
    while name != '':
        name = name.rstrip()
        names.append(name)
        name = read_file.readline()

def print_list():
    #loop through values in names list
    for n in names:
        #split names into first and last name
        name_format = (n.split(' '))
        #print text and flip last name and first name
        print('Good evening Dr. {}, would you mind if I called you {}?'.format(name_format[1],name_format[0]))

def main():
    load_file(read_file)
    print_list()

if __name__ == "__main__":
    main()