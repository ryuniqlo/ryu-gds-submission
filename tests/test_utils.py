import unittest
from scripts.utils import get_restaurants_lst, get_country_mapping_dict

class TestUtils(unittest.TestCase):

    def test_get_restaurants_lst(self):
        restaurants_lst = get_restaurants_lst()
        self.assertTrue(len(restaurants_lst) > 0)

    def test_get_country_mapping_dict(self):
        country_mapping = get_country_mapping_dict()
        self.assertTrue(len(country_mapping) > 0)

if __name__ == '__main__':
    unittest.main()