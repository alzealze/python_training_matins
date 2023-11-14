from time import sleep
from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'Manage').click()
        wd.find_element(By.LINK_TEXT, 'Manage Projects').click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        wd.find_element(By.CSS_SELECTOR, "input[name='name']").click()
        wd.find_element(By.CSS_SELECTOR, "input[name='name']").clear()
#        wd.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("NEW Project")
        wd.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(project)
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()
        wd.find_element(By.LINK_TEXT, 'My View').click()
#        sleep(2)
        self.project_cache = None

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element(By.LINK_TEXT, "%s" % project).click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "tr.row-1, tr.row-2"):
                ProjectName = element.find_element(By.TAG_NAME, "td").text
                self.project_cache.append(Project(ProjectName=ProjectName))
        return list(self.project_cache)
