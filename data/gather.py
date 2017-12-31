from coinmarketcap import api as cmc
import data

print(data.update('cmc_ticker',{'id': 'latest'},{'id': 'latest', 'data':cmc.ticker()}))
print(data.update('cmc_global',{'id': 'latest'},{'id': 'latest', 'data':cmc.global_data()}))