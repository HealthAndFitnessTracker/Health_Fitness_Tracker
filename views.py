from flask import Blueprint, render_template, request, session, redirect,  url_for
from forms.sign_in_form import SignInForm
from forms.sign_up_form import SignUpForm
from user import User

views = Blueprint(__name__, "views")

@views.route('/')
def dashboard():
    username = session.get('username')
    return render_template('dashboard.html', username=username)

@views.route('/signIn', methods=['GET', 'POST'])
def signIn():
    sign_in_form = SignInForm()
    if sign_in_form.validate_on_submit():
        email = sign_in_form.email.data
        password = sign_in_form.password.data
        try:
            user = User.login(email, password)
            session['username'] = user.username
            session['email'] = user.email
        except ValueError as e:
            error = str(e)
            return render_template('signIn.html', form=sign_in_form, error=error)

        return redirect(url_for('views.myBoard'))
    return render_template('signIn.html', form=sign_in_form)

@views.route('/signUp', methods=['GET', 'POST'])
def signUp():
    sign_up_form = SignUpForm()
    if sign_up_form.validate_on_submit():
        name = sign_up_form.name.data
        email = sign_up_form.email.data
        password = sign_up_form.password.data
        try:
            user = User(email, name, password)
            user.register()
            session['username'] = name
        except ValueError as e:
            error = str(e)
            return render_template('signUp.html', form=sign_up_form, error=error)
        return redirect(url_for('views.myBoard'))
    return render_template('signUp.html', form=sign_up_form)

@views.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('views.dashboard'))

@views.route('/myBoard', methods=['GET', 'POST'])
def myBoard():
    username = session.get('username')
    if username:
        return render_template('myBoard.html', username=username)
    else:
        return redirect(url_for('views.dashboard'))
    