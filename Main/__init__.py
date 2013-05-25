from flask      import Flask
from util       import Base, engine

app             = Flask(__name__)
#app.database    = 'InvSystem.db'
app.debug       = True
app.secret_key  = 'under_development'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///InvSystem.db'

import Main.views
from views import *

app.add_url_rule('/', 
                 view_func = Index.as_view('index'),
                 methods = ['GET', 'POST'])
from models import *
Base.metadata.create_all(engine)
