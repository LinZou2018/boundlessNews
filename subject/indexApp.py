import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from multiprocessing import Process

from subject.app.myapp import *
from subject.config.mysetting import setting


app = Application([('/index',IndexHandler),
                   ('/login',LoginHandler),
                   ('/register',RegisterHandler),
                   ('/alerts', AlertsHandler),
                    ('/check',CheckHandler),
                   ('/page',PageHandler)],
                  template_path='mytemplates',
                  static_path='mystatics')


server = HTTPServer(app)
server.listen(setting["duankou"])
IOLoop.current().start()