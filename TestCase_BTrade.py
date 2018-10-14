import unittest
import ComMeth
import Common


class TestCase_BTrade(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testA_trade(self):
        print("JEX交易")
        ComMeth.ComMeth().trade(14,1,0.000009,1,0)



