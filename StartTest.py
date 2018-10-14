import unittest
import time
import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.', pattern='TestCase_C*.py')
    unittest.TextTestRunner().run(suite)