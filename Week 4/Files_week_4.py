"""

Joe Sterf
 9/25/2019
 Python 2 - DAT-129 - Fall 2019
 File Practice
 Week 4

"""
#create a file
import os
#if file exists it deletes it and then creates a new one or if doesn't exist create one
if os.path.exists('writeranges2.txt'):
    os.remove('writeranges2.txt')
num_file = open('writeranges2.txt', 'w')

def print_range():
    num = 10
    #prints range of numbers
    while num > 0:
        for n in range(num):
            #writes range of numbers to file
            num_file.write(str(n))
        #moves to next line in file
        num_file.write('\n')
        num -= 1

def main():
    print_range()
    num_file.close()
    print('Process complete')

if __name__ == "__main__":
    main()