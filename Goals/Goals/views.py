from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route('/', methods=["GET","POST"])
def goals():
    #exercise_goal = request.form["exercise"]
    #calorie_goal = request.form["calories"]
    return render_template("goals.html")
