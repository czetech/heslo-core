from asyncio import ensure_future, sleep, create_task
from logging import DEBUG, basicConfig, getLogger
from os import environ

from aiohttp_cors import setup as cors_setup, ResourceOptions
import aioredis
from connexion import AioHttpApp

logger = getLogger(__name__)

g = {}


async def main_redis():
    while True:
        try:
            redis = aioredis.from_url('redis://redis-tg1-gen.8mvege.ng.0001.euc1.cache.amazonaws.com')
            phrase = await redis.get('phrase')
            g['phrase'] = phrase.decode() if phrase else None
            message1 = await redis.get('message1')
            g['message1'] = message1.decode() if message1 else None
            message2 = await redis.get('message2')
            g['message2'] = message2.decode() if message2 else None
            await redis.close()
            logger.info(f"Redis data received ({g})")
            await sleep(1)
        except Exception as e:
            logger.exception('Error in main_redis()')


async def main_redis_start(app):
    create_task(main_redis())


def main():
    basicConfig()
    getLogger(__name__).level = DEBUG
    
    # Create Connexion application
    app = AioHttpApp(__name__,
                     port=int(environ.get('HESLO_CORE_PORT', '80')),
                     specification_dir='openapi/')
    api = app.add_api('api_v1.yaml')
    
    # Add CORS to Connexion's underline AioHttp application
    resource_options = ResourceOptions(allow_credentials=True,
                                       expose_headers='*', allow_headers='*',
                                       allow_methods='*')
    cors = cors_setup(app.app, defaults={'*': resource_options})
    for route in list(app.app.router.routes()):
        cors.add(route)

    app.app.on_startup.append(main_redis_start)

    app.run()
