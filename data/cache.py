import redis

r = redis.StrictRedis(host='redis', port=6379, db=0)

# expiration time set to 120 seconds
def set(key,value):
    r.setex(key,120,value)

def get(key):
    return r.get(key)