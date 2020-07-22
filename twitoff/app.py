"""Main app/routing file for TwitOff."""

from flask import Flask, render_template
from .models import DB, User
from .twitter import add_users

def create_app():
    """ Create and configures an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')
    
    @app.route('/add_users')
    def add_user():
        DB.drop_all() #Always reset first
        DB.create_all()
        add_users
        return 'Users added!'

    @app.route('/view_users')
    def view_user():
        users = User.query.all()
        return '\n'.join([str(user) for user in users])

    return app
