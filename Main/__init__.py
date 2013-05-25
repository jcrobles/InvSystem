from flask import Flask

app             = Flask(__name__)
app.database    = 'InvSystem.db'
app.debug       = True
app.secret_key  = 'under_development'

import Main.views

app.add_url_rule('/', 
                 view_func = Index.as_view('index'),
                 methods = ['GET', 'POST'])

from views import *

