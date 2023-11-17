import random
import string
from model.project import Project


def test_add_project(app):
    project = random.choice(string.ascii_letters)
    old_proj = app.soap.project_list(username=app.config["webadmin"]["username"],
                                     password=app.config["webadmin"]["password"])
    app.project.create_project(project)
    new_proj = app.soap.project_list(username=app.config["webadmin"]["username"],
                                     password=app.config["webadmin"]["password"])
    old_proj.append(project)
    assert sorted(old_proj) == sorted(new_proj)
