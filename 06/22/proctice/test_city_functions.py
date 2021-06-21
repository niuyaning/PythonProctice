import unittest
from city_functions import city_function


class city_country(unittest.TestCase):
    def test_city_functions(self):
        cc = city_function("北京","中国",'5000')
        self.assertEqual(cc,'北京中国5000')


if __name__ == "__main__":
    unittest.TestCase()
