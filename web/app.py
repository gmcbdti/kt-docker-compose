import socket
import tornado.web
import json
import os
import tornado_swirl as swirl
from redis import Redis

redis = Redis(host=os.environ.get('REDIS_HOST'), port=6379)
host = socket.gethostname()


@swirl.restapi('/')
class InfoHandler(tornado.web.RequestHandler):

    def get(self):
        """Recupera informações.

               Recupera o nome de host do container e a contagem de acessos no endpoint.

               Path Parameter:
                   # itemid (int) -- The item id

               Tags:
                   info
               """
        redis.incr('hits')

        info = {"host": host, "hits": str(redis.get('hits'))}
        self.write(json.dumps(info, sort_keys=True, indent=4))
        self.set_header('Content-Type', 'application/json')

def make_app():
    return swirl.Application(swirl.api_routes())


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
