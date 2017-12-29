from coinmarketcap import api as cmc
import data

data.save('cmc_ticker',cmc.ticker())
# data.save('cmc_global',cmc.global_data())
