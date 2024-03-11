import unittest
from scripts.q3 import extract_ratings, calculate_thresholds

class TestQ3(unittest.TestCase):

    def test_extract_ratings(self):
        restaurants_lst = [
            {'user_rating': {'rating_text': 'Excellent', 'aggregate_rating': '4.8'}},
            {'user_rating': {'rating_text': 'Very Good', 'aggregate_rating': '4.5'}},
            {'user_rating': {'rating_text': 'Good', 'aggregate_rating': '4.0'}},
            {'user_rating': {'rating_text': 'Average', 'aggregate_rating': '3.5'}},
            {'user_rating': {'rating_text': 'Poor', 'aggregate_rating': '2.0'}},
            {'user_rating': {'rating_text': 'OK', 'aggregate_rating': '3.0'}}
        ]
        expected_ratings = ([4.8, 4.5, 4.0, 3.5, 2.0], ['Excellent', 'Very Good', 'Good', 'Average', 'Poor'])
        aggregate_ratings, rating_texts = extract_ratings(restaurants_lst)
        
        self.assertEqual((aggregate_ratings, rating_texts), expected_ratings)

    def test_calculate_thresholds(self):
        aggregate_ratings = [4.9, 4.4, 3.9, 3.4, 2.2, 4.5, 4.0, 3.5, 2.5, 1.0]
        rating_texts = ['Excellent', 'Very Good', 'Good', 'Average', 'Poor'] * 2
        expected_thresholds = {
            'Excellent': {'min': 4.5, 'max': 4.9},
            'Very Good': {'min': 4.0, 'max': 4.4},
            'Good': {'min': 3.5, 'max': 3.9},
            'Average': {'min': 2.5, 'max': 3.4},
            'Poor': {'min': 1.0, 'max': 2.2},
        }

        thresholds = calculate_thresholds(aggregate_ratings, rating_texts)

        for rating_text, expected_values in expected_thresholds.items():
            self.assertEqual(thresholds.loc[rating_text].to_dict(), expected_values)

if __name__ == '__main__':
    unittest.main()
