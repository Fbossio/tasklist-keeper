from website import create_app
import os

app = create_app(os.environ.get('FLASK_ENV'))
