from flask import Blueprint, render_template, request
from forms.sign_in_form import SignInForm

views = Blueprint(__name__, "views")

@views.route('/')
def dashboard():
    return render_template('dashboard.html')

@views.route('/signIn', methods=['GET', 'POST'])
def signIn():
    sign_in_form = SignInForm()
    if sign_in_form.validate_on_submit():
        email = sign_in_form.email.data
        password = sign_in_form.password.data

        return 'Hello'
    return render_template('signIn.html', form=sign_in_form)

@views.route('/signUp')
def signUp():
    return render_template('signUp.html')

@views.route('/signInCheck', methods=['POST'])
def signInCheck():
    return "temp"