from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.courses_repository as courses_repository

courses_blueprint = Blueprint("courses", __name__)



@courses_blueprint.route("/courses")
def courses():
    courses = courses_repository.select_all()
    return render_template("courses/index.html", courses = courses)

@courses_blueprint.route("/courses/<id>")
def show(id):
    courses = courses_repository.select(id)
    return render_template("courses/show.html", courses = courses )     


@courses_blueprint.route("/courses/new")
def new_courses():
    return render_template("courses/new.html")


@courses_blueprint.route("/courses", methods=["POST"])
def create_courses():
    name = request.form["name"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    active = request.form["active"]
    new_courses = Course(name, start_date, end_date, time, duration,capacity, active)
    courses_repository.save(new_courses)
    return redirect("/courses")


@courses_blueprint.route("/courses/<id>/edit")
def edit_member(id):
    courses = courses_repository.select(id)
    return render_template('courses/edit.html', courses = courses)


@courses_blueprint.route("/courses/<id>", methods=["POST"])
def update_courses(id):
    name = request.form["name"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    active = request.form["active"]
    course = Course(name, start_date, end_date, time, duration,capacity, active,id)
    courses_repository.update(course)
    return redirect("/courses")

@courses_blueprint.route("/course/<id>/delete", methods=['POST'])
def delete_course(id):
    courses_repository.delete(id)
    return redirect('/courses')   