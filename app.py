from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signInCheck')
def signInCheck():
    return null

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)