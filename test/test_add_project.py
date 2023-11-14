import random
import string


def test_add_project(app):
    project = random.choice(string.ascii_letters)
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    old_projects = list(map(str, old_projects))
    new_projects = list(map(str, new_projects))
    assert sorted(old_projects) == sorted(new_projects)
