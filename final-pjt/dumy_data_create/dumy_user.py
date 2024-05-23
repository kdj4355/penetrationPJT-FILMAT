import json
from faker import Faker
import random
import hashlib

fake = Faker('ko-KR')

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

# 영화 PK 값
movie_pks = [823464, 653346, 940721, 1219685, 693134, 967847, 1011985, 1111873, 1093995, 1094844, 920342, 843527, 119450, 1096197, 996154, 1147400, 934632, 1057001, 748783, 7451, 872585, 940551, 385687, 438631, 79474, 929590, 634492, 281338, 346698, 61791, 414906, 359410, 1041613, 1062807, 617127, 838209, 378018, 298618, 395990, 284053, 601796, 293660, 603, 11, 299537, 263115, 508947, 399170, 10138, 635, 1064178, 1105407, 218, 43074, 1079810, 284054, 64635, 577922, 475557, 348, 235, 1216299, 157336, 976906, 609681, 297762, 850888, 760104, 680, 62, 799583, 339403, 1366, 320288, 27205, 405774, 206647, 786892, 106, 490132, 126889, 845111, 141, 829, 381288, 578, 400928, 287947, 526896, 16320, 329865, 1924, 339846, 5548, 103, 821937, 615777, 620, 335983, 15, 699280, 1700, 284052, 141052, 1701, 424139, 869, 49047, 383498, 597891, 2666, 
68730, 1022789, 787699, 16281, 111, 9482, 719221, 784651, 766507, 198184, 794, 315635, 948549, 391713, 297802, 865921, 621, 615457, 447200, 720321, 984324, 14564, 299536, 807, 369885, 10155, 1093231, 34152, 2756, 447332, 489, 9348, 948, 505948, 36647, 1010581, 951491, 439079, 419430, 497698, 62215, 639720, 293167, 301337, 27579, 480530, 1148817, 763215, 395458, 910, 804095, 550, 861, 474350, 935271, 525, 467407, 765, 68721, 4233, 13765, 426563, 400106, 34851, 670292, 769, 420818, 969492, 696, 
505642, 264660, 407448, 9003, 274855, 1072790, 618588, 402900, 38147, 1375, 1374, 395834, 550988, 345, 862, 1209288, 282035, 19, 926393, 792307]


# Generate user data
users = []
for i in range(3, 51):
    plain_password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    hashed_password = hash_password(plain_password)
    user_data = {
        "model": "accounts.user",
        "pk": i,
        "fields": {
            "password": hashed_password,
            "last_login": fake.iso8601(tzinfo=None),
            "is_superuser": False,
            "username": fake.user_name(),
            "first_name": "",
            "last_name": "",
            "is_staff": False,
            "is_active": True,
            "date_joined": fake.iso8601(tzinfo=None),
            "email": fake.email(),
            "nickname": fake.first_name(),
            "groups": [],
            "user_permissions": [],
            "followings": random.sample(range(3, 51), random.randint(0, 10)),
        }
    }
    users.append(user_data)

# Write user data to JSON file
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, indent=4, ensure_ascii=False)


# import os
# import django

# # Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fianl_pjt_back')

# # Setup Django
# django.setup()

# from movies.models import Movie

# top_200_movie_ids = Movie.objects.order_by('-popularity').values_list('id', flat=True)[:200]

# print(list(top_200_movie_ids))


from django.contrib.auth.models import User
from movies.models import Movie

# Print movies liked by each user
users = User.objects.all()
for user in users:
    liked_movies = user.liked_movies.all()
    print(f"User {user.username} (ID: {user.id}) likes the following movies:")
    for movie in liked_movies:
        print(f"  - {movie.title} (ID: {movie.id})")
    print("\n")