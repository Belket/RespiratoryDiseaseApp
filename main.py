from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from tornado.httpserver import HTTPServer
import os
import asyncio
from handlers import PatientHandler, AdministratorHandler
from authorization import LoginHandler, RegistrationHandler

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

html_path = os.path.join(os.path.dirname(__file__), "static/html")
css_path = os.path.join(os.path.dirname(__file__), "static/css")
js_path = os.path.join(os.path.dirname(__file__), "static/js")
img_path = os.path.join(os.path.dirname(__file__), "static/img")
assets_path = os.path.join(os.path.dirname(__file__), "static/assets")

settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
}

application = Application(
    [(r'(favicon.ico)', StaticFileHandler, {"path": img_path}),
     (r"/login", LoginHandler),
     (r"/registration", RegistrationHandler),
     ("r/admin", AdministratorHandler),
     ("/", PatientHandler)],
    template_path=html_path, static_path=os.path.join(os.path.dirname(__file__), "static"), **settings)

server = HTTPServer(application)
server.listen(8080)
print("Server was started on port ", 8080)
IOLoop.current().start()
