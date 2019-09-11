"""

Joe Sterf
 9/11/2019
 Python 2 - DAT-129 - Fall 2019
 Looping Practice
 Week 2

"""
# print odd numbers from 1 to 100
def odd_num():
    i = 1
    while i < 100:
        print(i, end= '\t')
        i +=2

#print KABOM as K K K A A A B B B O O O O O O M M M

def kabom ():
    #ask user for word to spell out
    #word = input('Input word to spell out with 3 letters each: ')
    word = 'KABOOM'
    #print each letter in word three times
    for w in word:
        c = 0
        while c < 3:
            print(w, end='\t')
            c +=1

#prints every other letter in a work
def print_letter():
    phrase = 'askaliceithinkshe\'llknow'
    i = 1
    for p in phrase:
        if i % 2 != 0:
            print(p, end='')
        i += 1


#prints three column multiplication table
def nested_loop():
    #first column starts with 1
    o = 1
    while o < 5:
        c = 0
        #second column always starts with 5
        i = 5
        while c < 3:
            #third column multiples first and second column
            multiply = o * i
            #print one line of chart
            print('%d | %d | %d'%(o,i,multiply))
            i += 1
            c += 1
        o += 1

#prints out a formatted data structure
def data_structure():
    listoflists = [['mn', 'pa', 'ut'], ['b', 'p', 'c'], ['echo', 'charlie', 'tango']]
    labels = {"state": "US State Abbr: ", "element": "Chemical Element: ", "alpha": "Phonetic Call: "}
    #match list to label, if two letters - state, if one letter - element, other - alpha
    for l in listoflists:
        i = 0
        while i < len(l):
            if len(l[i]) == 1:
                print(labels["element"],l[i])
            elif len(l[i]) == 2:
                print(labels["state"], l[i])
            else:
                print(labels["alpha"], l[i])

            i += 1


def main():
    print('Loop 1')
    odd_num()
    print('Loop 2')
    kabom()
    print('Loop 3')
    print_letter()
    print('Loop 4')
    nested_loop()
    print('Loop 5')
    data_structure()

if __name__ == "__main__":
    main()