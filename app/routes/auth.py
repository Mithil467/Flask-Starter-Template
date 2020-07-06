import os

from datetime import datetime

from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
    abort,
    flash,
    current_app,
    send_file,
)
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from sqlalchemy import and_
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db

from app.forms import (
    LoginForm,
    RegisterForm,
)
from app.models import User

from sqlalchemy.exc import IntegrityError

auth = Blueprint("auth", __name__)



@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully", "success")
            return redirect(url_for("main.home"))

        flash("Wrong credentials", "warning")

    if current_user.is_authenticated:
        return render_template("login.html", form=form, name=current_user.name)
    else:
        return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        userobj = User(
            email=form.email.data.lower(),
            password=hashed_password,
        )
        try:
            db.session.add(userobj)
            db.session.commit()
            login_user(userobj)
            return redirect(url_for("main.home"))

        except IntegrityError:
            db.session.rollback()
            flash("Email already exists!", "danger")
            return render_template("register.html", form=form)
    return render_template("register.html", form=form)


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for("main.home"))
