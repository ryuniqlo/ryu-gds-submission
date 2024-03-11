from data_extraction import get_restaurants_lst, pd

def extract_relevant_event_columns(restaurant, filtered_events):
    extracted_data = []

    for event in filtered_events:
        restaurant_event = {
            'event_id': event.get('event_id','NA'),
            'restaurant_id': restaurant['id'],
            'restaurant_name': restaurant['name'],
            'photo_url': restaurant.get('photos_url', 'NA'),
            'event_title': event.get('title', 'NA'),
            'event_start_date': event.get('start_date', 'NA'),
            'event_end_date': event.get('end_date', 'NA')
        }

        extracted_data.append(restaurant_event)
    return extracted_data

def filter_events_by_month(restaurants_with_events, month, year):
    all_relevant_events = []

    for restaurant in restaurants_with_events:
        events = [event_dic['event'] for event_dic in restaurant['zomato_events']]
        filtered_events = [event for event in events if event['start_date'].startswith(f"{year}-{month}")]
        if filtered_events:
            all_relevant_events.extend(extract_relevant_event_columns(restaurant, filtered_events))
    
    return all_relevant_events

def main():
    restaurants_lst = get_restaurants_lst()
    restaurants_with_events = [restaurant for restaurant in restaurants_lst if restaurant.get('zomato_events', [])]
    april_2019_events = filter_events_by_month(restaurants_with_events, '04', '2019')

    df = pd.DataFrame(april_2019_events)
    df.to_csv('data/restaurant_events.csv', index=False)


if __name__ == "__main__":
    main()

