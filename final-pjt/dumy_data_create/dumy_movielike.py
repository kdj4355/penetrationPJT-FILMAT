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

# 영화 PK 값
movie_pks = [823464, 653346, 940721, 1219685, 693134, 967847, 1011985, 1111873, 1093995, 1094844, 920342, 843527, 119450, 1096197, 996154, 1147400, 934632, 1057001, 748783, 7451, 872585, 940551, 385687, 438631, 79474, 929590, 634492, 281338, 346698, 61791, 414906, 359410, 1041613, 1062807, 617127, 838209, 378018, 298618, 395990, 284053, 601796, 293660, 603, 11, 299537, 263115, 508947, 399170, 10138, 635, 1064178, 1105407, 218, 43074, 1079810, 284054, 64635, 577922, 475557, 348, 235, 1216299, 157336, 976906, 609681, 297762, 850888, 760104, 680, 62, 799583, 339403, 1366, 320288, 27205, 405774, 206647, 786892, 106, 490132, 126889, 845111, 141, 829]

# 이전에 선택된 movie_id와 user_id 추적
selected_combinations = set()

# Generate movie_like_users data
movie_like_users = []

for i in range(1, 300):
    # 중복을 피하기 위해 새로운 movie_id와 user_id 선택
    while True:
        movie_id = random.choice(movie_pks)
        user_id = random.randint(3, 50)
        if (movie_id, user_id) not in selected_combinations:
            selected_combinations.add((movie_id, user_id))
            break
    
    movie_like_user_data = {
        "model": "movies.movie_like_users",
        "pk": i,
        "fields": {
            "movie": movie_id,
            "user": user_id
        }
    }
    movie_like_users.append(movie_like_user_data)

# Write movie_like_users data to JSON file
with open('movie_like_users.json', 'w', encoding='utf-8') as f:
    json.dump(movie_like_users, f, indent=4, ensure_ascii=False)