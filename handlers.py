from tornado.web import RequestHandler, authenticated


class PatientHandler(RequestHandler):

    @authenticated
    def get(self):
        pass

    @authenticated
    def post(self):
        pass


class AdministratorHandler(RequestHandler):

    @authenticated
    def get(self):
        pass

    @authenticated
    def post(self):
        pass
