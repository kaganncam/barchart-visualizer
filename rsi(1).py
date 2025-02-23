import time 
from binance.spot import Spot
from matplotlib import pyplot

api_key = "API_KEY"
api_secret ="API_SECRET"
limit = 50


def fetch():
    client = Spot(api_key,api_secret)
    data =  client.klines("BTCUSDT","1m",limit = limit)
    highest = [bar[2] for bar in data] 
    lowest = [bar[3] for bar in data]
    open_price = [bar[1] for bar in data]
    close_price = [bar[4] for bar in data]
    volume = [bar[7] for bar in data]
    height = [abs(float(bar[1]) - float(bar[4])) for bar in data ]
    low_point = [min(float(bar[1]),float(bar[4])) for bar in data] 
    highest_lowest_difference = [abs(float(bar[2]) - float(bar[3])) for bar in data]
    x = range(0,limit)
    color = ["green" if bar[1] < bar[4]   else "red" for bar in data] 
    return x,height,low_point,color,highest,lowest,volume

def main():
    x , height ,low_point,color,highest,lowest,volume= fetch()
    fig,ax = pyplot.subplots()
    ax.bar(x,height,bottom = low_point,color = color)
    ax.vlines(x,lowest,highest,color= color ,linestyles = "solid",linewidth = 10)
    ax.set_ylim(low_point[0]-200,height[0]+ low_point[0] +200 )
    ax.legend()
    pyplot.show()
main()   