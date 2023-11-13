from selenium import webdriver

from fixture.project import ProjectHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognizer browser %s" % browser)
        self.session = SessionHelper(self)
        self.baseUrl = baseUrl
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            # Узнаем адрес текущей страницы
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()
