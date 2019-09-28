"""

Joe Sterf
 9/28/2019
 Python 2 - DAT-129 - Fall 2019
 JSON Homework
 Week 4

"""
#urllib import and opening URL file from https://docs.python.org/3/howto/urllib2.html
import urllib.request
import json

#create log file and clear contents
log_file = open('error_log.txt', 'w')
log_file.truncate(0)
#assign JSON url to variable
url = "https://data.wprdc.org/dataset/b0bfd969-d300-4117-8c85-fc9907a501dc/resource/242ed55e-d486-4f6d-b1cc-d2e251785444/download/cgcapitalprojects_img.geojson"

#create blank list
search_list =[]

def load_dict(webpage):
    # open URL and assign to variable
    url_data = urllib.request.urlopen(webpage)
    # load file to dictionary
    dictionary = json.loads(url_data.read())
    return dictionary

def display_file(f):
    #print dictionary
    for key in f:
        print(key,':', f[key])

def no_area(dict):
    #create list from features dictionary
    features_list = dict['features']
    #determine length of features list

    #loop through features list and send project id to log file if missing area
    i = 0
    while i < len(features_list):

        if features_list[i]['properties']['area'] == '':
            logMalformedProject(features_list[i]['properties']['id'])
        i += 1

def logMalformedProject(error):
    #write project id to log file
    log_file.write(str(error))
    log_file.write('\n')

def create_list(d):
    area = d['features']
    #add Area value to list if it's not already in list
    i = 0
    while i < len(area):
        value = area[i]['properties']['area']
        if value not in search_list:
            search_list.append(value)
        i += 1

    #print all area values
    c = 0
    while c < len(search_list):
        print(search_list[c])
        c += 1

def main():
    # open JSON file
    json_dict = load_dict(url)
    #print dictionary
    #mini task 1
    print('Contents of JSON file:')
    display_file(json_dict)
    #mini task 2
    no_area(json_dict)
    print('\n','IDs without an area sent to log file.','\n')
    #mini task 3
    print('Here is a list of the areas: ')
    create_list(json_dict)
    log_file.close()


if __name__ == "__main__":
    main()