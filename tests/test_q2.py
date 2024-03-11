import unittest
import os
from scripts.q2 import filter_events_by_month, extract_relevant_event_columns, main, check_event_month
from scripts.utils import get_restaurants_lst

class TestQ2(unittest.TestCase):
    unittest.TestCase.maxDiff = None

    def test_csv_export(self):
        main()
        self.assertTrue(os.path.isfile('data/restaurants.csv'))

    def test_filter_events_by_month(self):
        april_2019_events = filter_events_by_month(get_restaurants_lst(), 4, 2019)
        self.assertTrue(len(april_2019_events) > 0)

    def test_check_event_month(self):
        self.assertTrue(check_event_month('2021-01-01', '2023-01-01', 10, 2022))

    def test_extract_relevant_event_columns(self):
        test_restaurant = {
            'id': '18649486',
            'name': 'The Drunken Botanist',
            'photos_url': 'https://www.zomato.com/ncr/the-drunken-botanist-dlf-cyber-city-gurgaon/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop',
            'zomato_events': [
                {
                    'event': {
                        'event_id': 322331,
                        'start_date': '2019-03-06',
                        'end_date': '2019-08-28'
                        }
                },
                {
                    'event': {
                        'event_id': 322332,
                        'start_date': '2019-04-06',
                        'end_date': '2019-04-07',
                        'title': 'April Fools',
                        }
                },
                {
                    'event': {
                        'event_id': 322333, 
                        'start_date': '2024-03-06', 
                        'end_date': '2024-03-07'
                    }
                }
            ]
        }

        extracted_data = filter_events_by_month([test_restaurant, {}], 4, 2019)
        expected_result = [
            {
                'event_id': 322331,
                'restaurant_id': '18649486',
                'restaurant_name': 'The Drunken Botanist',
                'photo_url': 'https://www.zomato.com/ncr/the-drunken-botanist-dlf-cyber-city-gurgaon/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop',
                'event_title': 'NA',
                'event_start_date': '2019-03-06',
                'event_end_date': '2019-08-28'
            },
            {
                'event_id': 322332,
                'restaurant_id': '18649486',
                'restaurant_name': 'The Drunken Botanist',
                'photo_url': 'https://www.zomato.com/ncr/the-drunken-botanist-dlf-cyber-city-gurgaon/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop',
                'event_title': 'April Fools',
                'event_start_date': '2019-04-06',
                'event_end_date': '2019-04-07'
            }
        ]

        self.assertEqual(extracted_data, expected_result)


if __name__ == '__main__':
    unittest.main()
