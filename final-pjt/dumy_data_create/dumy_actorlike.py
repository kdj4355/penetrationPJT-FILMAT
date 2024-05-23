# from movies.models import Actor

# # Retrieve all actor_ids from the Actor model
# actor_ids = list(Actor.objects.values_list('actor_id', flat=True))

# # Print the list of actor_ids
# print(actor_ids)


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

# 영화배우 PK 값
actor_pks = [31, 64, 85, 114, 131, 139, 190, 192, 287, 380, 500, 501, 524, 880, 887, 934, 976, 1038, 1158, 1245, 1269, 1813, 1892, 2037, 2227, 2231, 2440, 2461, 2524, 2882, 2963, 3061, 3131, 3141, 3223, 3293, 3810, 3896, 3967, 4174, 4587, 4589, 4724, 5081, 5292, 6161, 6384, 6614, 6856, 6885, 6952, 6972, 9195, 10696, 10814, 10859, 10882, 10912, 10990, 11150, 11288, 11701, 12799, 12835, 13240, 15110, 15135, 15556, 16483, 16828, 17244, 
17288, 17521, 17743, 17832, 18897, 18973, 19211, 19537, 19961, 21657, 22226, 26723, 29222, 37917, 37995, 38673, 41421, 46074, 49624, 52404, 54693, 54882, 55638, 62064, 62220, 62747, 63312, 66743, 70851, 71070, 73968, 74568, 77700, 79072, 81685, 82809, 83271, 87722, 90633, 94185, 109513, 115150, 115440, 117642, 118545, 125025, 220448, 221018, 224513, 234352, 298410, 505710, 582130, 587020, 933238, 974169, 989325, 1024395, 
1095818, 1136406, 1161474, 1168778, 1172108, 1190668, 1196101, 1212111, 1222992, 1223059, 1252318, 1253360, 1253391, 1258305, 1290466, 1351386, 1373737, 1397778, 1424928, 1425934, 1434487, 1497557, 1522703, 1563442, 1575317, 1590844, 1604826, 1613836, 1617957, 1684536, 1767250, 1833002, 1883366, 1907997, 1914924, 1955840, 1972974, 2025252, 2049994, 2091759, 2117890, 2146942, 2214888, 2349944, 2472212, 2511949, 2554414, 2786960, 3124615, 3371804]

# 이전에 선택된 actor_id와 user_id 추적
selected_combinations = set()

# Generate actor_like_users data
actor_like_users = []

for user_id in range(3, 51):
    # 사용자가 영화배우를 선택할지 여부를 랜덤하게 결정
    if random.random() < 0.8:  # 80%의 확률로 영화배우를 선택하지 않음
        continue
    
    # 임의의 영화배우 선택 (최소 1명)
    num_actors = random.randint(1, len(actor_pks))
    selected_actors = random.sample(actor_pks, num_actors)
    
    # 중복을 피하기 위해 선택된 actor_id와 user_id 추적
    for actor_id in selected_actors:
        if (actor_id, user_id) not in selected_combinations:
            selected_combinations.add((actor_id, user_id))
    
            actor_like_user_data = {
                "model": "movies.actor_like_users",
                "pk": len(actor_like_users) + 1,
                "fields": {
                    "actor": actor_id,
                    "user": user_id
                }
            }
            actor_like_users.append(actor_like_user_data)

# Write actor_like_users data to JSON file
with open('actor_like_users.json', 'w', encoding='utf-8') as f:
    json.dump(actor_like_users, f, indent=4, ensure_ascii=False)
