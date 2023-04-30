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

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = weight / (height ** 2)
    return render_template('bmi.html', bmi=bmi)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)