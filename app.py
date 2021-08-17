from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask.json import load
from project import Project, Part
from dotenv import load_dotenv
import db
import os

load_dotenv(".env")

app = Flask(__name__)
db_interface = db.DBInterface(os.environ.get("DB_USERNAME"), os.environ.get("DB_PASSWORD"), os.environ.get("DB_CLUSTER"))

@app.route("/")
def home():
    projects = db_interface.get_projects()
    
    return render_template("index.html", projects = projects)

@app.route("/project/<project_id>", methods = ["GET", "PUT", "DELETE"])
def project(project_id):

    if request.method == "GET":
        proj = db_interface.get_project(project_id)
        return render_template("project.html", project = proj)
    
    elif request.method == "PUT":
        proj = db_interface.get_project(project_id)
        proj.name = request.form["name"]
        db_interface.update_project(proj)
        return {}
    
    elif request.method == "DELETE":
        db_interface.remove_project(ObjectId(project_id))
        return {}


@app.route("/add", methods = ["POST"])
def add_project():
    new_project = Project(ObjectId(), request.form["name"])
    db_interface.insert_project(new_project)
    return redirect(url_for("home"))

@app.route("/project/<project_id>/add", methods = ["POST"])
def add_part(project_id):
    proj = db_interface.get_project(project_id)

    # If price is not provided, default to 0
    price = request.form["price"]
    if request.form["price"] == "":
        price = 0

    proj.parts.append(Part(ObjectId(), request.form["name"], request.form["link"], price))
    db_interface.update_project(proj)

    return redirect(url_for("project", project_id = project_id))

@app.route("/project/<project_id>/part/<part_id>", methods = ["PUT", "DELETE"])
def part(project_id, part_id):

    if request.method == "PUT":
        proj = db_interface.get_project(project_id)
        form = request.form
        part_index = None
        for i in range(len(proj.parts)):
            if str(proj.parts[i].id) == part_id:
                part_index = i
                break
        
        if part_index is None:
            # TODO
            return {}, 404
        else:
            proj.parts[part_index].name = form["name"]
            proj.parts[part_index].link = form["link"]
            proj.parts[part_index].price = form["price"]
            db_interface.update_project(proj)

        return {}

    elif request.method == "DELETE":
        proj = db_interface.get_project(project_id)

        for part in list(proj.parts):
            if str(part.id) == part_id:
                proj.parts.remove(part)
                break
        
        db_interface.update_project(proj)
        
        return {}

if __name__ == "__main__":
    app.run(host="0.0.0.0")