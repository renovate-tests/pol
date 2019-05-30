import pickle

import aioredis
from aioredis.commands import _NOTSET, Redis

from app.core import config


class PickleRedis(Redis):
    async def get(self, key, *, encoding=_NOTSET):
        r = await self.execute(b'GET', key, encoding=encoding)
        if r:
            return pickle.loads(r)

    async def set(self, key, value, *, expire=0, pexpire=0, exist=None):
        await Redis.set(
            self,
            key,
            pickle.dumps(value),
            expire=expire,
            pexpire=pexpire,
            exist=exist
        )


async def setup_redis_pool():
    return await aioredis.create_redis_pool(
        config.REDIS_URI,
        password=config.REDIS_PASSWORD,
        minsize=5,
        maxsize=20,
        commands_factory=PickleRedis,
    )
