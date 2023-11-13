import random
import string

from model.project import Project


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 1:
        project = random.choice(string.ascii_letters)
        app.project.create_project(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects[:-1])
    app.project.delete_project(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



