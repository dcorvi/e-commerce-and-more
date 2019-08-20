from app import app, db
from app.models import User, Post
import os

# from the app folder import the app instance variable

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post, 'User': User }


if __name__ == '__main__':
  # app.run(host='0.0.0.0', port=80)
    app.debug = True
    port = int(os.environ.get("PORT", 88))
    app.run(host='0.0.0.0', port=port)
