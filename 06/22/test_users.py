import unittest
from users import get_user_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        full_name = get_user_name('niu','ya','ning')
        self.assertEqual(full_name,'niuyaning')

if __name__ == 'main__':
    unittest.TestCase()