from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")


class RegistrationHandler(BaseHandler):

    def get(self):
        self.render('registration.html')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")

        ''' TO DO:
        connection to db
        '''
