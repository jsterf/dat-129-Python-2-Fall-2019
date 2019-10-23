#access the St. Louis FRED API
import urllib.request
import json
import csv

def getSearchURL (category, units):
    #calls API for specific series information
  url ='https://api.stlouisfed.org/fred/series/observations?series_id=%s&file_type=json&units=%s&api_key=62c0b2d9bb46e8fcd971673697dae1d2' % (str(category), str(units))
  return url

def getJSON(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return response.read()

def load_json (data):
    # load json information
    json_data = json.loads(data)
    return json_data

def load_sub_info (data, key):
    # load the dictionary for a specific key from the json_data
    sub_data = data[key]
    return sub_data

def output_data (data, key1, key2, date):
    #output the values for specific keys for a specific time period
    # cycle through observational data and only print date and value info
    print('   ',key1,'  :',key2)
    for key in data:
        # get year of information
        year = int(key[str.lower(key1)][:4])
        # only print information if the year is equal to or greater than year selected
        if year >= date:
            print(key[str.lower(key1)], ':', key[str.lower(key2)])

def main():
    #get GDP history
    API = getJSON(getSearchURL('A191RL1Q225SBEA','lin'))
    json_info = load_json(API)
    dict = load_sub_info(json_info,'observations')
    # get unemployment rate history
    API = getJSON(getSearchURL('UNRATE', 'lin'))
    json_info = load_json(API)
    dict2 = load_sub_info(json_info, 'observations')

    print('GDP')
    output_data(dict, 'Date', 'Value', 2000)
    print('')
    print('Unemployement Rate')
    output_data(dict2,'Date','Value',2000)

    #Try to combine values from multiple queries into one dictionary with date as the link.
    #Maybe compare unemployment and GDP to stock market returns to see if they are leading or lagging indicators.
    #Will need to account for not all data sets having the same date information.
    #Can then export the values to CSV to check for coorelation between them.

if __name__ == "__main__":
    main()




