from scripts.utils import get_restaurants_lst
import pandas as pd

def extract_ratings(restaurants_lst):
    aggregate_ratings = []
    rating_texts = []

    for restaurant in restaurants_lst:
        valid_rating_texts = ['excellent', 'very good', 'good', 'average', 'poor']
        rating_text = restaurant['user_rating']['rating_text']
        if rating_text.lower() not in valid_rating_texts:
            continue
        aggregate_ratings.append(float(restaurant['user_rating']['aggregate_rating']))
        rating_texts.append(rating_text)

    return aggregate_ratings, rating_texts

def calculate_thresholds(aggregate_ratings, rating_texts):
    data = {'aggregate_rating': aggregate_ratings, 'rating_text': rating_texts}
    df = pd.DataFrame(data)
    result = df.groupby('rating_text')['aggregate_rating'].agg(['min', 'max'])
    result = result.sort_values(by=['min', 'max'], ascending=False)

    return result

def main():
    restaurants_lst = get_restaurants_lst()
    aggregate_ratings, rating_texts = extract_ratings(restaurants_lst)
    thresholds = calculate_thresholds(aggregate_ratings, rating_texts)

    print(thresholds)

if __name__ == "__main__":
    main()