from tornado.ioloop import IOLoop
from tornado.web import Application
from handlers import *


application = Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    IOLoop.instance().start()
