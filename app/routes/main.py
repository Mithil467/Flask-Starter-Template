from flask import (
    Blueprint,
    abort,
    redirect,
    render_template,
    request,
    url_for,
    current_app
)
from flask_login import current_user, login_required

from app.extensions import db
from app.models import User

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def home():
    if current_user.is_authenticated:
        return render_template("home.html", email=current_user.email)
    else:
        return render_template("home.html")
