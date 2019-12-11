#Dat-129 Final Project
#Access the St. Louis FRED API to determine if GDP and Unemployment are leading indicators for S&P 500 Return


import urllib.request
import json
import pandas as pd


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

def output_data (data, key1, key2, date, dictionary):
    #output the values for specific keys for a specific time period
    # cycle through observational data and only print date and value info
    for key in data:
        # get year of information
        year = int(key[str.lower(key1)][:4])
        # only add information to dictionary if the year is equal to or greater than year selected
        if year >= date:
            #don't include if value is a .
            if key[str.lower(key2)] == '.':
                pass
            else:
                dictionary[key[str.lower(key1)]] = float(key[str.lower(key2)])


def create_dictionary (search, year):
    #calls other functions in order to use FRED API to pull data and assigns it to a dictionary
    dictionary = {}
    API = getJSON(getSearchURL(search, 'lin'))
    json_info = load_json(API)
    dict = load_sub_info(json_info, 'observations')
    output_data(dict, 'Date', 'Value', year, dictionary)
    return dictionary

def print_chart (dataset):
    chart = pd.DataFrame(dataset)
    chart = chart.dropna()
    lines = chart.plot.line()

def main():
    #create dictionary will values for historcial GDP, unemployment rate and S&P 500 returns
    GDP = create_dictionary('A191RL1Q225SBEA',2009)
    Unemployment = create_dictionary('UNRATE', 2009)
    SP500 = create_dictionary('SP500', 2009)

    #combine results dictionaries into one dictionary to create dataframe
    data= {'GDP':GDP, 'Unemployment Rate':Unemployment, 'S&P 500':SP500}
    
    #breakout GDP and Unemployment from S&P 500 in order to show as two separate charts
    subdata1 = {'GDP':GDP, 'Unemployment Rate':Unemployment}
    subdata2 = {'S&P 500':SP500}
    
    #print dataframe
    df = pd.DataFrame(data)
    df = df.dropna()
    print(df)
    
    #print two charts
    print_chart(subdata1)
    print_chart(subdata2)
    


if __name__ == "__main__":
    main()




