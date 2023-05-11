from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route('/')
def measurements():
    return render_template('measurements.html')
