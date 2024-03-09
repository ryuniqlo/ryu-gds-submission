import requests
import pandas as pd


def extract_restaurant_data():
    url = 'https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json'
    response = requests.get(url)
    data = response.json()

    restaurant_lst = []

    for page in data:
        for row in page['restaurants']:
            restaurant = row['restaurant']
            restaurant_simplified_dict = {
                'restaurant_id': restaurant['id'],
                'restaurant_name': restaurant['name'],
                'country_id': restaurant['location']['country_id'],
                #Country - map and replace country_id
                'city': restaurant['location']['city'],
                'user_rating_votes': restaurant['user_rating']['votes'],
                'user_aggregate_rating': float(restaurant['user_rating']['aggregate_rating']),
                'cuisines': restaurant['cuisines'].split(', ')  # Convert cuisines to a list
            }

            restaurant_lst.append(restaurant_simplified_dict)

    return pd.DataFrame(restaurant_lst)

def main():
    extract_restaurant_data().to_csv('data/restaurants.csv')

if __name__ == "__main__":
    main()