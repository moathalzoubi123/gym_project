from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.members_repository as members_repository

members_blueprint = Blueprint("members", __name__)



@members_blueprint.route("/members")
def member():
    members = members_repository.select_all()
    return render_template("members/index.html", members = members)


# @members_blueprint.route("/members/<id>")
# def show(id):
#     members = members_repository.select(id)
#     return render_template("members/show.html", members = members)    


@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")


@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    age = request.form["age"]
    membership = request.form["membership"]
    active = request.form["active"]
    new_member = Member(name, age, membership, active)
    members_repository.save(new_member)
    return redirect("/members")


@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = members_repository.select(id)
    return render_template('members/edit.html', member=member)


@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    age = request.form["age"]
    membership = request.form["membership"]
    active = request.form["active"]
    member = Member(name, age, membership, active,id)
    members_repository.update(member)
    return redirect("/members")


@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    members_repository.delete(id)
    return redirect('/members')    