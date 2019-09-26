"""

Joe Sterf
 9/25/2019
 Python 2 - DAT-129 - Fall 2019
 File Practice
 Week 4

"""

import csv


#open CSV file
jail_stats = open('jail_june.csv', newline='')
#creates a dictionary for each row in file
reader = csv.DictReader(jail_stats)

def main():

    totBlack = 0
    totWhite = 0
    censusDate = '2019-06-01'
    for row in reader:
        #only pull info in which the date is equal to the census date
        if row['Date'] == censusDate:
            #increase count if race equals B
            if row ['Race'] == 'B':
                totBlack += 1
            #increase count if race equals W
            elif row['Race'] == 'W':
                totWhite += 1
    #close file
    jail_stats.close()
    per_black = totBlack / (totWhite + totBlack) * 100
    per_white = totWhite / (totWhite + totBlack) * 100
    #print results
    print('Total count of black inmates on',censusDate, 'is',format(totBlack,',.0f'))
    print('Percent of black to white inmates is', format(per_black,'0.2f'),'percent')
    print('Total count of white inmates on',censusDate, 'is',format(totWhite,',.0f'))
    print('Percent of white to black inmates is', format(per_white,'0.2f'),'percent')


if __name__ == "__main__":
    main()