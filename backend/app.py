from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key = "sports-portal-secret"

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.coord import coord_bp
from routes.player import player_bp

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(coord_bp, url_prefix="/coord")
app.register_blueprint(player_bp, url_prefix="/player")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roles")
def roles():
    return render_template("role_selection.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
