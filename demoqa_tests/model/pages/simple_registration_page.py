from selene import browser, have

from demoqa_tests.data.users import SimpleUser


class SimpleRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')
        self.output = browser.element('#output')

    def open(self):
        browser.open('/text-box')

    def register(self, user: SimpleUser):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit_button.click()

    def should_have_submitted(self, user: SimpleUser):
        self.output.element('#name').should(have.text(user.full_name))
        self.output.element('#email').should(have.text(user.email))
        self.output.element('#currentAddress').should(have.text(user.current_address))
        self.output.element('#permanentAddress').should(have.text(user.permanent_address))


