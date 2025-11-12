from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 각 메뉴 페이지
@app.route('/subject')
def subject():
    return render_template('subject.html')

@app.route('/rationale')
def rationale():
    return render_template('rationale.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/environment')
def environment():
    return render_template('environment.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

