import unittest
import Common
import ComMeth

class TestCase_AUser(unittest.TestCase):
    success="'code':0"
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_login(self):
        try:
            print('test_login_by_phone')
            response= ComMeth.ComMeth().login(13866666666)
            Common.contrast(response,self.success)    ##验证接口结果是否符合要求
            print(response)
        except Exception as ex:
            raise ex
    '''def test_lagout(self):
        try:
            print("test_lagout")
            response=ComMeth.ComMeth().logout()
            print(response)
        except Exception as ex:
            raise ex'''



