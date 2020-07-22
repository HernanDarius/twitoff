"""Main app/routing file for TwitOff."""

from os import getenv
from flask import Flask, render_template, request
from .models import DB, User
from .predict import predict_user
from .twitter import add_users, add_or_update_user, update_all_users

def create_app():
    """ Create and configures an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
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
