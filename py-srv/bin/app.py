from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, RequestHandler
from tornado_sqlalchemy import SQLAlchemy, SessionMixin, as_future

import settings
from model import PopModel

database_url = '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    )

class MainHandler(SessionMixin, RequestHandler):
    def get(self):
        with self.make_session() as session:
            pops = session.query(PopModel).all()
            results = [
                {
                    "id": pop.id,
                    "name": pop.name,
                    "color": pop.color
                } for pop in pops]

        self.write({'result': results})

define('host', default='0.0.0.0', help='Docker specific address')
define('port', default=8000, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    app = Application([
        ('/pop', MainHandler)
    ], db=SQLAlchemy(database_url))
    http_server = HTTPServer(app)
    http_server.listen(options.port, options.host)
    print(f'Listening on http://{options.host}:{options.port}')
    IOLoop.current().start()

if __name__ == '__main__':
    main()
