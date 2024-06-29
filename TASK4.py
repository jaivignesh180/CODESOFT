import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
file_path = r'D:\java\INTENSHIP\file.csv'  
data = pd.read_csv(file_path)
user_item_matrix = data.pivot(index='user', columns='item', values='rating').fillna(0)
user_similarity = cosine_similarity(user_item_matrix)
def recommend(user_id, num_recommendations=2):
    similarity_scores = user_similarity[user_id - 1]
    similar_users = np.argsort(-similarity_scores)[1:num_recommendations+1]  
    recommended_items = []
    for user in similar_users:
        rated_items = data[data['user'] == user + 1]['item'] 
        for item in rated_items:
            if item not in data[data['user'] == user_id]['item'].values:
                recommended_items.append(item)
                if len(recommended_items) >= num_recommendations:
                    break
        if len(recommended_items) >= num_recommendations:
            break
    return recommended_items

user_id = 4
recommended_items = recommend(user_id, num_recommendations=2)
print(f'Recommended items for user {user_id}: {recommended_items}')
