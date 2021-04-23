import redis

# Settings
r = redis.Redis(host='localhost', port=6379, db=0)

def setRedis(key,value, ex = 43200):
    r.set(key,value, ex)

def setExpiry(key):
    r.delete(key)

def getValue(key):
    value = r.get(key)
    return value