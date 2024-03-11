from scripts.utils import get_restaurants_lst
import pandas as pd
from datetime import datetime
import calendar

def extract_relevant_event_columns(restaurant, filtered_events):
    extracted_data = []

    for event in filtered_events:
        restaurant_event = {
            'event_id': event.get('event_id','NA'),
            'restaurant_id': restaurant.get('id', 'NA'),
            'restaurant_name': restaurant.get('name', 'NA'),
            'photo_url': restaurant.get('photos_url', 'NA'),
            'event_title': event.get('title', 'NA'),
            'event_start_date': event.get('start_date', 'NA'),
            'event_end_date': event.get('end_date', 'NA')
        }

        extracted_data.append(restaurant_event)
    return extracted_data

def check_event_month(start_date, end_date, target_month, target_year):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    last_day_of_target_month = calendar.monthrange(target_year, target_month)[1]
    target_month_start = datetime(target_year, target_month, 1)
    target_month_end = datetime(target_year, target_month, last_day_of_target_month)

    return (start_date >= target_month_start and start_date <= target_month_end) or (end_date >= target_month_start and start_date <= target_month_end) or (start_date <= target_month_start and end_date >= target_month_end)
        
def filter_events_by_month(restaurants_with_events, month, year):
    all_relevant_events = []

    for restaurant in restaurants_with_events:
        events = [event_dic.get('event', {}) for event_dic in restaurant.get('zomato_events', {}) if event_dic.get('event', {})]
        filtered_events = [event for event in events if check_event_month(event['start_date'], event['end_date'], month, year)]
        if filtered_events:
            all_relevant_events.extend(extract_relevant_event_columns(restaurant, filtered_events))
    
    return all_relevant_events

def main():
    restaurants_lst = get_restaurants_lst()
    restaurants_with_events = [restaurant for restaurant in restaurants_lst if restaurant.get('zomato_events', [])]
    april_2019_events = filter_events_by_month(restaurants_with_events, 4, 2019)

    df = pd.DataFrame(april_2019_events)
    df.to_csv('data/restaurant_events.csv', index=False)


if __name__ == "__main__":
    main()

