from ..lib import login
import unittest


class LogInTest(unittest.TestCase):
    def test_sign_up(self):
        self.assertEqual(login.sign_up('123ssd','1234'), False)
        self.assertEqual(login.sign_up('sd','1234'), True)

