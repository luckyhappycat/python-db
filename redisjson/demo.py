import redis
import json

data = {
    'foo': 'bar'
}
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.StrictRedis(connection_pool=pool)

# r.json().set('doc', '$', json.dumps(data))
reply = json.loads(r.json().get('doc', '$')[0])
print(reply)
print(reply["foo"])
