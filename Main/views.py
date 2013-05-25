from util import db
import flask, flask.views
from models import *
from Main import app

class Index(flask.views.MethodView):
    def get(self):
        items = Item.query.all()
        return flask.render_template('home.html', items = items)
    def post(self):
        pass
