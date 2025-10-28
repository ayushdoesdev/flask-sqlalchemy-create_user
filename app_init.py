from flask import Flask

app = Flask(__name__)

import db_init
from users import user_page

app.register_blueprint(user_page)

