from flask import Flask, render_template
from routes.auth import auth_bp
from routes.player import player_bp
from routes.admin import admin_bp
from routes.coord import coord_bp
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecret"

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(player_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(coord_bp)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roles")
def roles():
    return render_template("role_selection.html")

if __name__ == "__main__":
    app.run(debug=True)
