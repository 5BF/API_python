import unittest
import requests
import json
import time
import urllib3
urllib3.disable_warnings()
import requests.packages





class Klines(unittest.TestCase):

    def setUp(self):
        pass
    #火币接口demo:https://github.com/huobiapi/REST-Python3-demo/blob/master/HuobiServices.py

    #       JEX线上                                     火币
    #       symbolId:3,   name:eth/btc                  symbolid:ethbtc
    #       symbolId:6,   name:ltc/btc                  symbolid:ltcbtc
    #       symbolId:14,  name:jex/btc                  symbolid:NOME
    #       symbolId:68,  name:eos/btc                  symbolid:eosbtc
    #       symbolId:69,  name:eos/usdt                 symbolid:eosusdt
    #       symbolId:79,  name:dash/usdt                symbolid:dashusdt
    #       symbolId:164: name:ht/usdt                  symbolid:htusdt
    #       symbolId:165, name:bnb/usdt                 symbolid:bnbusdt
    #       symbolId:249, name:wicc/usdt                symbolid:wiccusdt

    def tearDown(self):
        pass

    def test_kline(self):

        #ktime=('1min','5min','15min','30min','60min','4hour')
        #for time in ktime:
        JEX = {
            'symbolId': '79',
            'type': '1min',
        }
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        paramsHUOBI = {
            'symbolId': 'dashusdt',
            'period': '1min',
        }

        # JEX的K线接口
        requests.packages.urllib3.disable_warnings()
        response_JEX = requests.get(url="https://www.jex.com/api/v2/pub/kline", params=JEX,headers=headers,verify=False)
        JEX = response_JEX.json()
        # HUOBI的K线接口
        response_Huobi = requests.get(
            url="https://api.huobipro.com/market/history/kline?period=" + paramsHUOBI['period'] + "&symbol=" +
                paramsHUOBI['symbolId'] + "")
        Huobi = response_Huobi.json()

        for i in range(0, 150):
            # JEX的K线四个值
            jex_high = json.dumps(JEX['data'][i]['high'])
            jex_low = json.dumps(JEX['data'][i]['low'])
            jex_open = json.dumps(JEX['data'][i]['open'])
            jex_close = json.dumps(JEX['data'][i]['close'])

            # JEX的时间戳转换为当前时间
            dateStamp = int(json.dumps(JEX['data'][i]['time']))
            time_stamp = int(dateStamp * (10 ** (10 - len(str(dateStamp)))))  # 将13位的时间戳规范为10位的时间戳
            time_array = time.localtime(time_stamp)
            JEX_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)

            # 火币K线的四个值
            huobi_high = json.dumps(Huobi['data'][i]['high'])
            huobi_low = json.dumps(Huobi['data'][i]['low'])
            huobi_open = json.dumps(Huobi['data'][i]['open'])
            huobi_close = json.dumps(Huobi['data'][i]['close'])

            # 判断这四个值是否相等
            if (
                    jex_high == huobi_high and jex_low == huobi_low and jex_open == huobi_open and jex_close == huobi_close):
                print("没毛病老铁")
                # print("第", i+1, "条A等于：", jex)
                # print("第", i+1, "条B等于：", huobi)
            else:
                print("有数据不相等")
                print("第", i + 1, "条JEX最高价等于：", jex_high, "时间是", JEX_time)
                print("第", i + 1, "条JEX最低价等于：", jex_low, "时间是", JEX_time)
                print("第", i + 1, "条JEX开盘价等于：", jex_open, "时间是", JEX_time)
                print("第", i + 1, "条JEX收盘价等于：", jex_close, "时间是", JEX_time)

                print("第", i + 1, "条Huobi最高价等于：", huobi_high)
                print("第", i + 1, "条Huobi最低价等于：", huobi_low)
                print("第", i + 1, "条Huobi开盘价等于：", huobi_open)
                print("第", i + 1, "条Huobi收盘价等于：", huobi_close)




if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Klines("test_kline"))

    runner = unittest.TextTestRunner
    runner.run(suite)



