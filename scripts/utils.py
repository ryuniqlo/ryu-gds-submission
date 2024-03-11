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