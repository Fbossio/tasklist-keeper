from website import create_app, db
import os

app = create_app(os.environ.get('FLASK_ENV'))
db = db(app)
