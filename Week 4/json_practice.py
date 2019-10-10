"""

Joe Sterf
 9/25/2019
 Python 2 - DAT-129 - Fall 2019
 JSON Practice
 Week 4

"""

import json

#encode JSON info to file
f = open('sampleJSONout.txt','w')
f.write(json.dumps({'student-count':12,'teach-count':1}))
f.close()

#reading JSON info into python objects
#loads JSON info into test_load variable
test_load = json.loads('{"numbers":[4,2,1,10],"list of strings":["first","second","third"]}')

#print JSON info for 'list of strings'
print(test_load)
print(test_load['list of strings'])
def main():

    print('Finished successfully')

if __name__ == "__main__":
    main()