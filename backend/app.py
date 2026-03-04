from flask import Flask, render_template, request
import os, base64, qrcode
from io import BytesIO
from dotenv import load_dotenv
from flask import render_template, session

# =============================
# LOAD ENV VARIABLES
# =============================
load_dotenv()

# =============================
# CREATE APP
# =============================
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.getenv("SECRET_KEY", "sports-secret")

# =============================
# IMPORT BLUEPRINTS
# =============================
# IMPORTANT: Make sure these paths match your folder
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.coord import coord_bp
from routes.player import player_bp

# =============================
# REGISTER BLUEPRINTS
# =============================
# ⚠️ No prefix for auth → required for /api/login
app.register_blueprint(auth_bp)

# Other modules
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(coord_bp, url_prefix="/coord")
app.register_blueprint(player_bp, url_prefix="/player")


# =============================
# HOME + QR GENERATION
# =============================
@app.route("/")
def home():
    base_url = request.url_root.rstrip("/")
    portal_url = f"{base_url}/roles"

    # Generate QR code
    qr = qrcode.make(portal_url)
    buf = BytesIO()
    qr.save(buf)
    qr_b64 = base64.b64encode(buf.getvalue()).decode()

    return render_template(
        "index.html",
        qr_code=qr_b64,
        portal_url=portal_url
    )


# =============================
# ROLE SELECTION PAGE
# =============================
@app.route("/roles")
def roles():
    return render_template("role_selection.html")

# =============================
# LOGOUT ROUTE 
# =============================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# =============================
# HEALTH CHECK (IMPORTANT FOR RENDER)
# =============================
@app.route("/health")
def health():
    return {"status": "ok"}


# =============================
# ERROR HANDLING (GOOD FOR VIVA)
# =============================
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return "Internal Server Error", 500


# =============================
# RUN APP (LOCAL ONLY)
# =============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)