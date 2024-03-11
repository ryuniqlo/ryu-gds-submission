import unittest
import os
from scripts.q1 import main, extract_relevant_columns
from scripts.utils import get_country_mapping_dict

class TestQ1(unittest.TestCase):

    def test_csv_export(self):
        main()
        self.assertTrue(os.path.isfile('data/restaurants.csv'))

    def test_extract_relevant_columns(self):
        restaurant_dict = {
            'id': '18649486',
            'name': 'The Drunken Botanist',
            'location': {'country_id': 1, 'city': 'Gurgaon'},
            'user_rating': {'votes': '4765', 'aggregate_rating': '4.4'},
            'cuisines': 'Continental, Italian, North Indian, Chinese'
        }
        country_mapping_dict = get_country_mapping_dict()
        result = extract_relevant_columns(restaurant_dict, country_mapping_dict)

        expected_result = {
            'restaurant_id': '18649486',
            'restaurant_name': 'The Drunken Botanist',
            'country': 'India',
            'city': 'Gurgaon',
            'user_rating_votes': '4765',
            'user_aggregate_rating': 4.4,
            'cuisines': ['Continental', 'Italian', 'North Indian', 'Chinese']
        }

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
