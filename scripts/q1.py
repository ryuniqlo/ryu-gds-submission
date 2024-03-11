from scripts.utils import get_restaurants_lst, get_country_mapping_dict
import pandas as pd

def extract_relevant_columns(restaurant_full_dict, country_mapping_dict):
    restaurant_simplified_dict = {
        'restaurant_id': restaurant_full_dict['id'],
        'restaurant_name': restaurant_full_dict['name'],
        'country': country_mapping_dict.get(restaurant_full_dict['location']['country_id'], 'NA'),
        'city': restaurant_full_dict['location']['city'],
        'user_rating_votes': restaurant_full_dict['user_rating']['votes'],
        'user_aggregate_rating': float(restaurant_full_dict['user_rating']['aggregate_rating']),
        'cuisines': restaurant_full_dict['cuisines'].split(', ')
    }
    return restaurant_simplified_dict

def main():
    restaurants_lst = get_restaurants_lst()
    processed_restaurants_lst = [extract_relevant_columns(restaurant, get_country_mapping_dict()) for restaurant in restaurants_lst]
    pd.DataFrame(processed_restaurants_lst).to_csv('data/restaurants.csv')

if __name__ == "__main__":
    main()