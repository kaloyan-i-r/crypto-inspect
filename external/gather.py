from coinmarketcap import api as cmc
import repackage
repackage.up()
from data import crud

print(crud.update('cmc_ticker',{'id': 'latest'},{'id': 'latest', 'data':cmc.ticker()}))
print(crud.update('cmc_global',{'id': 'latest'},{'id': 'latest', 'data':cmc.global_data()}))