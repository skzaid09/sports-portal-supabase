from flask import Flask, render_template, request
import os, base64, qrcode
from io import BytesIO

app = Flask(__name__)
app.secret_key = "sports-secret"

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
    base_url = request.url_root.rstrip("/")
    portal_url = f"{base_url}/roles"

    qr = qrcode.make(portal_url)
    buf = BytesIO()
    qr.save(buf)
    qr_b64 = base64.b64encode(buf.getvalue()).decode()

    return render_template("index.html", qr_code=qr_b64, portal_url=portal_url)

@app.route("/roles")
def roles():
    return render_template("role_selection.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
