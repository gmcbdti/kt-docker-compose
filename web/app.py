import socket
import tornado.web
import tornado.gen

import tornado_swirl as swirl
from redis import Redis


@swirl.restapi('/item/(?P<itemid>\d+)')
class ItemHandler(tornado.web.RequestHandler):
    redis = Redis(host='redis', port=6379)
    host = socket.gethostname()

    def get(self, itemid):
        """Get Item data.

        Gets Item data from database.

        Path Parameter:
            itemid (int) -- The item id

        Tags:
            items
        """
        self.redis.incr('hits')
        hits = self.redis.get('hits')

        self.write('\nHello World!\nI have been seen %s times.\nMy Host name is %s\n\n' % (hits, self.host))


@swirl.schema
class User(object):
    """This is the user class

    Your usual long description.

    Properties:
        name (string) -- required.  Name of user
        age (int) -- Age of user

    """
    pass


def make_app():
    return swirl.Application(swirl.api_routes())


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
