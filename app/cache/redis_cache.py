import json 
import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.redis_url)


def get_cache_prediction(key :str):
    value = redis_client.get(key)

    if value:
        return json.load(value)
    else:
        return None
    
def set_cache_prediction(key: str , value : dict , expity_time = 3600):
    redis_client.set(key , ex=expity_time , value=json.dump(value))
