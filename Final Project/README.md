#FRED API
This Python program uses the Federal Reserve FRED API to capture three different pieces of historical economic data - GDP, Unemployment Rate and S&P 500 returns.

A separate dictionary is created for each piece of data.  All three dictionaries are then combined into a dataframe using Pandas for analysis.

	def print_chart (dataset):
	    chart = pd.DataFrame(dataset)
	    chart = chart.dropna()
	    lines = chart.plot.line()

#Question
Are GDP and Unemployment a leading indicator for stock market (S&P 500) returns?

#Analysis
Based on the output charts (see GDP-Unemployment Chart and S&P Return Chart) of data from 2010 to 2019, while GDP did not seem to be an indicator for stock market returns, the drop in Unemployment and rise in the S&P 500 appeared to be correlated. However, based on this analysis it is unclear if the Unemployment rate is a true leading indicator of stock market returns.  A future expansion of this project could be done to delve deeper into the relationship between these two metrics.