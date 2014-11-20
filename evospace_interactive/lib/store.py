import os
import redis

REDISTOGO_URL ='redis://redistogo:979f0fde04936ce7435196d32abe7395@greeneye.redistogo.com:11907/'
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)