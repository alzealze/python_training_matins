import random
import string


def test_del_project(app):
    if len(app.project.get_project_list()) == 1:
        project = random.choice(string.ascii_letters)
        app.project.create_project(project)
    old_project = app.soap.project_list()
    project = random.choice(old_project)
    app.project.delete_project(project)
    new_projects = app.soap.project_list()
    old_project.remove(project)
    assert sorted(old_project) == sorted(new_projects)
