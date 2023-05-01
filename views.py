from flask import Blueprint, render_template, request
from forms.sign_in_form import SignInForm
from forms.sign_up_form import SignUpForm

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

@views.route('/signUp', methods=['GET', 'POST'])
def signUp():
    sign_up_form = SignUpForm()
    if sign_up_form.validate_on_submit():
        name = sign_up_form.name.data
        email = sign_up_form.email.data
        password = sign_up_form.password.data
        return 'Hello'

    return render_template('signUp.html', form=sign_up_form)
