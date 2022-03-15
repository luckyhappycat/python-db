# coding=utf-8
import redis

db = redis.Redis(host="127.0.0.1", port=6379, decode_responses=False)
db.set('foo', 'Bar')
print(db.get('foo'))