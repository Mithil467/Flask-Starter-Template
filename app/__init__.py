from flask import Flask, render_template
from app.extensions import bs, db, login_manager, migrate
from app.models import User
from app.routes.auth import auth
from app.routes.main import main
from app.commands import create_tables

def unauthorized(e):
    return render_template("401.html"), 401

def page_not_found(e):
    return render_template("404.html"), 404

def server_error(e):
    return render_template("500.html"), 500

def create_app(config_file="settings.py"):
    app = Flask(__name__)

    app.register_error_handler(401, unauthorized)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, server_error)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    
    bs.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    app.cli.add_command(create_tables)

    return app
