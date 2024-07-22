from demoqa_tests.model.components.left_panel import LeftPanel
from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.model.pages.registration_steps import RegistrationSteps
from demoqa_tests.model.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration_page = SimpleRegistrationPage()
        self.left_panel = LeftPanel()
        self.registration_page = RegistrationPage()
        self.registration_steps = RegistrationSteps()


app = Application()
