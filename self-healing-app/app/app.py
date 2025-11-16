from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ---- Frontend Route ----
@app.route('/')
def home():
    return render_template('index.html')

# ---- Backend API Route ----
@app.route('/api/status')
def api_status():
    return jsonify({"status": "✅ Backend is healthy and connected!"})

# ---- Health Checks for Kubernetes ----
@app.route('/healthz')
def healthz():
    return "OK", 200

@app.route('/readyz')
def readyz():
    return "Ready", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
