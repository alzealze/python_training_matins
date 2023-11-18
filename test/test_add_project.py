import random
import string


def test_add_project(app):
    project = random.choice(string.ascii_letters)
    old_project = app.soap.project_list()
    app.project.create_project(project)
    new_project = app.soap.project_list()
    old_project.append(project)
    assert sorted(old_project) == sorted(new_project)
