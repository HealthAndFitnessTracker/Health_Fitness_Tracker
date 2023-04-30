from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route('/')
def dashboard():
    return render_template('dashboard.html')

@views.route('/signIn')
def signIn():
    return render_template('signIn.html')

@views.route('/signUp')
def signUp():
    return render_template('signUp.html')

@views.route('/signInCheck', methods=['POST'])
def signInCheck():
    return "temp"