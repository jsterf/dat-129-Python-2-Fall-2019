

import urllib.request
import json
import csv

#access the St. Louis FRED API



def getSearchURL (category):
    #calls API for specific series information
  url ='https://api.stlouisfed.org/fred/series/observations?series_id=%s&file_type=json&api_key=62c0b2d9bb46e8fcd971673697dae1d2' % (str(category))
  return url

def getJSON(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return response.read()

def main():
    API = getJSON(getSearchURL('UNRATE'))
    json_data = json.loads(API)
    observation_data = json_data['observations']
    print(observation_data)
    for key in observation_data:
        for second_key in key:
            print(second_key,':',key[second_key])


if __name__ == "__main__":
    main()




