import json
from faker import Faker
import random
import hashlib

fake = Faker()

# 비밀번호 해싱 함수
def hash_password(password):
    return hashlib.pbkdf2_hmac(
        'sha256',  # 해시 알고리즘
        password.encode('utf-8'),  # 비밀번호를 바이트로 인코딩
        b'salt',  # 솔트 값
        100000  # 반복 횟수
    ).hex()

# 장르 PK 값
genre_pks = [28, 12, 16, 35, 80, 99, 18, 10751, 14, 36, 27, 10402, 9648, 10749, 878, 10770, 53, 10752, 37]

# 이전에 선택된 genre_id와 user_id 추적
selected_combinations = set()

# Generate genre_like_users data
genre_like_users = []

for i in range(1, 70):
    # 중복을 피하기 위해 새로운 user_id 선택
    user_id = random.randint(1, 50)
    
    # 임의의 장르 선택 (최소 1개, 최대 5개)
    num_genres = random.randint(1, 5)
    selected_genres = random.sample(genre_pks, num_genres)
    
    # 중복을 피하기 위해 선택된 genre_id와 user_id 추적
    for genre_id in selected_genres:
        if (genre_id, user_id) not in selected_combinations:
            selected_combinations.add((genre_id, user_id))
    
            genre_like_user_data = {
                "model": "movies.genre_like_users",
                "pk": len(genre_like_users) + 1,
                "fields": {
                    "genre": genre_id,
                    "user": user_id
                }
            }
            genre_like_users.append(genre_like_user_data)

# Write genre_like_users data to JSON file
with open('genre_like_users.json', 'w', encoding='utf-8') as f:
    json.dump(genre_like_users, f, indent=4, ensure_ascii=False)