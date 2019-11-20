import numpy
import pandas as pd
import matplotlib
from pandas import DataFrame, Series
import csv

def main():
    seriesObj = Series([80000,120000,95000,200000],['Indian','Greek','Italian','Chili']) 
    print(seriesObj)
    print(seriesObj.mean())
    
    with open('usaPowerSources2001-2018.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        energy = [row for row in reader]
    energyDF = DataFrame(energy)
    #print(energyDF)
    energyDF.astype({'coal':'float64'}).describe()
    #print(energyDF.solar.describe())

if __name__ == "__main__":
    main()




