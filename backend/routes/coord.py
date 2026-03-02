# #new3
# from flask import Blueprint, render_template, session, redirect

# coord_bp = Blueprint("coord", __name__, url_prefix="/coord")


# @coord_bp.route("/login")
# def login():
#     return render_template("coord/login.html")


# @coord_bp.route("/dashboard")
# def dashboard():
#     if "role" not in session or session["role"] != "coord":
#         return redirect("/coord/login")

#     return render_template("coord/dashboard.html")

#new4
# from flask import Blueprint, render_template, session, redirect

# coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

# @coord_bp.route("/login")
# def login():
#     return render_template("coord/login.html")

# @coord_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "coord":
#         return redirect("/coord/login")
#     return render_template("coord/dashboard.html")

#polish
from flask import Blueprint, render_template, session, redirect

coord_bp = Blueprint("coord", __name__, url_prefix="/coord")


# COORD LOGIN
@coord_bp.route("/login")
def login():
    return render_template("coord/login.html")


# COORD DASHBOARD
@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/coord/login")

    return render_template("coord/dashboard.html")