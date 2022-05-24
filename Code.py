import imp
import pandas as pd
import yfinance as yf
import matplotlib as plt

def analysis2():
    tickers= ["SPY","^TNX"]
    data =yf.download(tickers, start="2000-01-01",end="2022-01-01", period='ld')
    print (data.head(5))


#    fig = plt.figure()
#    ax = fig.add_axes([0, 0, 1, 1])
#    ax.scatter(data.iloc[:,0], data.iloc[:,1], color='r')
#    ax.set_xlabel('Market')
#    ax.set_ylabel('Interest rate')
#    ax.set_title('Scatter plot')
#    plt.show()

    plt.scatter(data.iloc[:,0], data.iloc[:,1])
    plt.title('Stock Market Return Vs Interest Rate')
    plt.xlabel('Stock market return')
    plt.ylabel('Interest rate')
    plt.show()
    plt.savefig("Output.png")


analysis2()

