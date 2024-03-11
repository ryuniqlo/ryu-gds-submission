import requests
import pandas as pd

def get_restaurants_lst():
    url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'
    response = requests.get(url)
    restaurants_lst = []
    
    for page in response.json():
        restaurants_lst.extend([restaurant_json['restaurant'] for restaurant_json in page['restaurants']])

    return restaurants_lst

def get_country_mapping_dict():
    country_df = pd.read_excel('data/Country-Code.xlsx')
    country_mapping = {}
    for index, row in country_df.iterrows():
        country_mapping[row['Country Code']] = row['Country']
    return country_mapping

def extract_relevant_columns(restaurant_full_dict, country_mapping_dict):
    restaurant_simplified_dict = {
        'restaurant_id': restaurant_full_dict['id'],
        'restaurant_name': restaurant_full_dict['name'],
        'country': country_mapping_dict[restaurant_full_dict['location']['country_id']],
        'city': restaurant_full_dict['location']['city'],
        'user_rating_votes': restaurant_full_dict['user_rating']['votes'],
        'user_aggregate_rating': float(restaurant_full_dict['user_rating']['aggregate_rating']),
        'cuisines': restaurant_full_dict['cuisines'].split(', ')
    }
    return restaurant_simplified_dict



def main():
    # Question 1
    restaurants_lst = get_restaurants_lst()
    processed_restaurants_lst = [extract_relevant_columns(restaurant, get_country_mapping_dict()) for restaurant in restaurants_lst]
    pd.DataFrame(processed_restaurants_lst).to_csv('data/restaurants.csv')

if __name__ == "__main__":
    main()