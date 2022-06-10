from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.courses_repository as courses_repository
import repositories.members_repository as members_repository

bookings_blueprint = Blueprint("bookings", __name__) 



@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all() 
    return render_template("bookings/index.html", bookings = bookings)


@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = members_repository.select_all()
    courses = courses_repository.select_all()
    return render_template("visits/new.html", members = members, courses= courses )


@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    course_id = request.form['course_id']
    member = members_repository.select(member_id)
    course = courses_repository.select(course_id)
    booking = Booking(member, course,)
    booking_repository.save(booking)
    return redirect('/bookings')


@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')