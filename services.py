import Utils


class Service:
    def login(self,user,pwd):
        params={
            'loginName': user,
            'password':pwd,
            'udesk':False,
        }
        url='/api/v2/inner/user/weblogin'
        return Utils.Utils().http_post_requset(url,params)

    def trade(self,symbol,type,price,amount,source):
        params={
            'symbol':symbol,
            'type':type,
            'price':price,
            'amount':amount,
            'source':source,
        }
        url='/api/v2/inner/trade/placeOrder'
        return Utils.Utils().http_post_requset(url,params)

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