import redis
from .redisconfig import RedisConfig


class RedisConnect:
    def __init__(self, redis_config=RedisConfig()):
        self.redis_config = redis_config
        self.redis = redis.StrictRedis(
            host=self.redis_config.host,
            port=self.redis_config.port
        )

    def exists(self, key):
        return self.redis.exists(key)

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value):
        return self.redis.set(key, value)
