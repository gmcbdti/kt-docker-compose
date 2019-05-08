import socket
import tornado.web
import json
import os
import tornado_swirl as swirl
from redis import Redis

redis = Redis(host=os.environ.get('REDIS_HOST'), port=6379)
host = socket.gethostname()


@swirl.restapi('/v1/system/info')
class InfoHandler(tornado.web.RequestHandler):

    def get(self):
        """Recupera informações.

        Recupera o nome de host do container e a contagem de acessos no endpoint.

        Path Parameter:
            #

        Tags:
            Sistema

        """
        redis.incr('hits')
        s_info = SystemInfo(host=host, hits=int(redis.get('hits')))
        self.write(json.dumps(s_info, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4))
        self.set_header('Content-Type', 'application/json')


@swirl.schema
class SystemInfo(object):
    """This is the system_info class

    System Information

    Properties:
        host (string) -- required. Hostname
        hits (int) --  required. System Hits

    """
    def __init__(self, host="", hits=0):
        self.host = host
        self.hits = hits

if __name__ == "__main__":
    app = swirl.Application(swirl.api_routes())
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
