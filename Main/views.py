from util           import session
import flask, flask.views
from models         import *
from Main           import app

class Index(flask.views.MethodView):
    def get(self):
        item = Item('test', '1', 1, 1, 1)
        session.add(item)
        session.commit()
#        items = Item.query.all()
#        return flask.render_template('home.html', items = items)
        return "hi"
    def post(self):
        pass
