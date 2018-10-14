import Utils


class BaseDate():
    def Klines(self,symbolId,type):
        params={
            'symbolId': symbolId,
            'type': type,
        }
        url='/api/v2/pub/kline'
        return Utils.Utils().http_get_request(url,params)

    def logout(self):
        params={

        }
        url='/api/v2/inner/user/logout'
        return Utils.Utils().http_post_requset(url,params=params)

    def currencys(self):
        params={

        }
        url='/api/v2/pub/currencys'
        return Utils.Utils().http_get_request(url,params=params)

    def depth(self):
        params={

        }
        url='/api/v2/pub/depth'
        return Utils.Utils().http_get_request(url,params=params)

    def exchange(self):
        params={

        }
        url='/api/v2/pub/exchange'
        return Utils.Utils().http_get_request(url,params=params)

    def jexcap(self):
        params={

        }
        url='/api/v2/pub/jexcap'
        return Utils.Utils().http_get_request(url,params=params)

    def option(self):
        params={

        }
        url='/api/v2/pub/option'
        return Utils.Utils().http_get_request(url,params=params)

    def preToSetting(self):
        params={

        }
        url='/api/v2/pub/preToSetting'
        return Utils.Utils().http_get_request(url,params=params)

    def symbols(self):
        params={

        }
        url='/api/v2/pub/symbols'
        return Utils.Utils().http_get_request(url,params=params)

    def ticker(self):
        params={

        }
        url='/api/v2/pub/ticker'
        return Utils.Utils.http_get_request(url,params=params)

    def trades(self):
        params={

        }
        url='/api/v2/pub/trades'
        return Utils.Utils().http_get_request(url,params=params)