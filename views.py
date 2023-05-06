from flask import Blueprint, render_template, request
from forms.sign_in_form import SignInForm
from forms.sign_up_form import SignUpForm
from src.User import User
from appbase import db
from Measurements import Measurements

views = Blueprint(__name__, "views")

@views.route('/')
def dashboard():
    return render_template('dashboard.html')

# changed part of the sign in method to get the information stored on the database. it will still function like it previously did.
@views.route('/signIn', methods=['GET', 'POST'])
def signIn():
    # this part is to get the data from sign in requests and to use them in the profile and user. Done by Noah
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

    sign_in_form = SignInForm()
    if sign_in_form.validate_on_submit():
        email = sign_in_form.email.data
        password = sign_in_form.password.data

        return render_template('profile.html', Name=user.name, Measurements=user.measurements)
    return render_template('signIn.html', form=sign_in_form)
# changed this function to send a new accounts info into the database. it will still act like it previously did. done by Noah
@views.route('/signUp', methods=['GET', 'POST'])
def signUp():
    # this part is to get the data from sign in requests and to use them in the profile and user.
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        measurements = Measurements(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

        data = request.form
        print(data)
        new_user = User(name=name, email=email, password=password, measurements=measurements)
        db.session.add(new_user)
        db.session.commit()

    sign_up_form = SignUpForm()
    if sign_up_form.validate_on_submit():
        name = sign_up_form.name.data
        email = sign_up_form.email.data
        password = sign_up_form.password.data
        return render_template('profile.html', Name=new_user.name)

    return render_template('signUp.html', form=sign_up_form)

@views.route('/profile', methods=['GET', 'POST'])
def profile():
    args = request.args
    username = args.get('name')