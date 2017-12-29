import requests

class basic():
    def __call_endpoint(self,cls,endpoint):
        return requests.get(self.url+endpoint).json()

    def __init__(self,url):
        self.url = url
        setattr(self.__class__, 'get', classmethod(self.__call_endpoint))



if __name__ == '__main__':
    print(2)
    obj = basic('https://api.coinmarketcap.com/v1/')
    obj.get('ticker')