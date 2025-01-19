import os
from dotenv import load_dotenv
import redis

load_dotenv()

r = redis.Redis(
    host='redis-18856.c124.us-central1-1.gce.redns.redis-cloud.com',
    port=18856,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASSWORD"),
)

success = r.set('rediskey', 'redisvalue')

result = r.get('rediskey')
print(result)
