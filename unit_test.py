import unittest
import lib.login as lg

class TestCases(unittest.TestCase):
    def test_signup(self):
        self.assertEquals(lg.sign_up("123213", "password"),False)
        self.assertEquals(lg.sign_up("asb123", "password"),True)
        self.assertEquals(lg.sign_up("asgb3213", ""),False)
        self.assertEquals(lg.sign_up("", "awasd"),False)
    
    def test_lookup_database(self):
        pass

    def test_main(self):
        pass
    