from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.main_page_container = browser.all('.category-cards .card-body')
        self.left_panel_container = browser.element('.left-pannel')

    def open(self, item1, item2):
        browser.open('/')
        self.main_page_container.element_by(have.exact_text(item1)).click()
        self.left_panel_container.all('.menu-list .text').element_by(have.exact_text(item2)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')

    def open_registration_form(self):
        self.open('Forms', 'Practice Form')

