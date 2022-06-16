import matplotlib.pyplot as plt
import numpy as np
# import urllib + matplotlib
import urllib
import matplotlib.dates as mdates
# places to get info Quandal, google, wkipidia they all have API
# Getting stock prices info

# create a function which create a graph for a specific stock
def graph_data(stock):

    # Need stock price url find it in the internet
    # we want 10 years of data
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'+stock+'/chartdata;type=quote;range=10y/csv'
    # the source code = we want to open stock_price_url and read and decode it
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    # Split the code with lines
    split_source = source_code.split('\n')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intereting Graph\nCheck it out')
    plt.legend()
    plt.show()


# call graph_data for Tesla
graph_data('TSLA')
