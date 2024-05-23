import json
import random
from faker import Faker

fake = Faker("ko_KR")

# Generate comment data
comments = []

for pk in range(1, 401):
    user_id = random.randint(1, 50)
    review_id = random.randint(1, 277)
    num_like_users = random.randint(0, 10)  # 최대 10명의 좋아요 사용자
    like_users = random.sample(range(1, 51), num_like_users)
    created_at = fake.date_time_between(start_date="-2y", end_date="now").strftime("%Y-%m-%dT%H:%M:%S")
    updated_at = fake.date_time_between(start_date="-2y", end_date="now").strftime("%Y-%m-%dT%H:%M:%S")
    content = fake.sentence()

    comment_data = {
        "model": "community.comment",
        "pk": pk,
        "fields": {
            "user": user_id,
            "review": review_id,
            "like_users": like_users,
            "content": content,
            "created_at": created_at,
            "updated_at": updated_at
        }
    }
    comments.append(comment_data)

# Write comment data to JSON file
with open('comments.json', 'w', encoding='utf-8') as f:
    json.dump(comments, f, indent=4, ensure_ascii=False)