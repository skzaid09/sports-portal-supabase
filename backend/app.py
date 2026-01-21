import os
from flask import Flask, render_template, request
import qrcode, base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = "final-year-project"

@app.route("/")
def home():
    portal_url = request.url_root.rstrip("/") + "/roles"

    qr = qrcode.make(portal_url)
    buffer = BytesIO()
    qr.save(buffer)
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render_template("index.html", qr_code=qr_base64, portal_url=portal_url)

@app.route("/roles")
def roles():
    return render_template("role_selection.html")

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
