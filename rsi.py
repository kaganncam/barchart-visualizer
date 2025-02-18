import time 
from binance.spot import Spot
from matplotlib import pyplot

api_key = "API_KEY"
api_secret ="API_SECRET"
limit = 50

def fetch():
    client = Spot(api_key,api_secret)
    data =  client.klines("BTCUSDT","1m",limit = limit)
    open_price = [bar[1] for bar in data]
    close_price = [bar[4] for bar in data]
    height = [abs(float(bar[1]) - float(bar[4])) for bar in data ]
    low_point = [min(float(bar[1]),float(bar[4])) for bar in data] 
    x = range(0,limit )
    color = ["green" if bar[1] < bar[4]   else "red" for bar in data] 
    return x,height,low_point,color

def upgrade(x,height,low_point,color):
    pyplot.clf()
    pyplot.bar( x = x, height=height ,width=0.8,bottom=low_point,color = color)
    pyplot.pause(0.1)
    pyplot.draw()

def main():
    x , height ,low_point,color = fetch()
    pyplot.bar(x,height,bottom=low_point,color = color)
    pyplot.xlabel("Zaman Dakika 1m")
    pyplot.ylabel("BTC USDT")
    pyplot.title("BTC")
    pyplot.xticks(x[::5])
    pyplot.show(block = False)
    while True: 
        time.sleep(60)
        x,height,low_point,color = fetch()
        upgrade(x,height,low_point,color)
        print("refresh")

main()   