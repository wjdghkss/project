import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ---- JSON 로드 함수 ----
def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 메인 페이지
@app.route("/")
def index():
    return render_template("index.html")

# ---- 페이지 라우트 ----
@app.route("/subject")
def subject():
    data = load_data()
    return render_template("subject.html", data=data["subject"])

@app.route("/rationale")
def rationale():
    data = load_data()
    return render_template("rationale.html", data=data["rationale"])

@app.route("/features")
def features():
    data = load_data()
    return render_template("features.html", data=data["features"])

@app.route("/environment")
def environment():
    data = load_data()
    return render_template("environment.html", data=data["environment"])

@app.route("/team")
def team():
    data = load_data()
    return render_template("team.html", data=data["team"])

# ---- JSON API 제공 ----
@app.route("/api/subject")
def api_subject():
    return jsonify(load_data()["subject"])

@app.route("/api/rationale")
def api_rationale():
    return jsonify(load_data()["rationale"])

@app.route("/api/features")
def api_features():
    return jsonify(load_data()["features"])

@app.route("/api/environment")
def api_environment():
    return jsonify(load_data()["environment"])

@app.route("/api/team")
def api_team():
    return jsonify(load_data()["team"])

# 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
