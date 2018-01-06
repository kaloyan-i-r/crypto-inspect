import repackage
repackage.up()
from gather import apiclient

url = 'https://api.coinmarketcap.com/v1/'
endpoints = ['ticker','global']

class api():

    @staticmethod
    def call_endpoint(endpoint):
        return apiclient.basic(url).get(endpoint)

    @staticmethod
    def ticker():
        return api.call_endpoint('ticker?limit=200')

    @staticmethod
    def global_data():
        return api.call_endpoint('global')

