import  unittest
import services
import  Common
import Utils
import DB
from Services import BaseDate_Interface


class ComMeth(unittest.TestCase):
    SUCCESS_RESULT="'code':0"


    def login(self,name):
        try:
            response = services.Service().login(name, Common.pwdOne)
            token = response['data']['token']
            Utils.Utils.headers['headerToken'] = token
            print(token)
            #return response
            return ("用户的ID是：",DB.DB().get_userid(name))
        except Exception as ex:
            raise ex

    def trade(self,symbol,type,price,amount,source):
        response=services.Service().trade(symbol,type,price,amount,source)
        print (response)

    def Klines(self,symbolId,type):
        try:
            response=services.Service().Klines(symbolId,type)
            return (response)
        except Exception as ex:
            raise ex

    def logout(self):
        try:
            response=services.Service().logout()
            return (response)
        except Exception as ex:
            raise ex

    def depth(self):
        try:
            response=BaseDate_Interface.BaseDate().depth()
            return (response)
        except Exception as ex:
            raise ex

    def exchange(self):
        try:
            response=BaseDate_Interface.BaseDate().exchange()
            return (response)
        except Exception as ex:
            raise ex

    def jexcap(self):
        try:
            response=BaseDate_Interface.BaseDate().jexcap()
            return (response)
        except Exception as ex:
            raise ex

    def option(self):
        try:
            response=BaseDate_Interface.BaseDate().option()
            return (response)
        except Exception as ex:
            raise ex

    def preToSetting(self):
        try:
            response=BaseDate_Interface.BaseDate().preToSetting()
            return (response)
        except Exception as ex:
            raise ex

