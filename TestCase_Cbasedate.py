import unittest
import Common
import ComMeth



class Kline(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_kline(self):
        responses=ComMeth.ComMeth().Klines('117','1min')
        print(responses)
    def test_currencys(self):
        pass
