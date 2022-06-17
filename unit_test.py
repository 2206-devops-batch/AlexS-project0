import unittest
from lib import login
import main

class Test(unittest.TestCase):
    def test_signup(self):
        self.assertEqual(login.sign_up("1231sadsa","password"), False)
        self.assertEqual(login.sign_up("!@test","pass1"), False)
    def test_main(self):
        result = "table $150.00\nkeyboard $40.51\ntooth picks $3.95\nbowl $12.99\nphone $599.00\n"
        data =  [["table",150.00], ["keyboard",40.51], ["tooth picks",3.95], ["bowl",12.99], ["phone",599.00]] 
        self.assertEqual(main.menu(data),result)
        main.items.append('table')
        main.items.append('keyboard')
        self.assertEqual(main.lookup_item("table"),True)
        self.assertEqual(main.lookup_item("table2"),False)
        self.assertEqual(main.lookup_item("KeyBoard"),False)
        self.assertEqual(main.lookup_item("keyboard"),True)
        
    def test_login(self):
        self.assertEqual(login.lookup_database("!@test22","pass1"), True)
        self.assertEqual(login.lookup_database("!@t","pass1"), False)



if __name__ == '__main__':unittest.main()