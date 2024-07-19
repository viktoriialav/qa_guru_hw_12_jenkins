from datetime import date

import allure
from allure_commons.types import Severity

from demoqa_tests.application import app
from demoqa_tests.data import users


@allure.feature('Simple registration form')
@allure.title('Test of simple student registration form')
@allure.description('This step includes only general steps of the simple student registration form')
@allure.tag('Simple registration Form', 'Student', 'class SimpleUser')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Barbra Streisand')
@allure.link('https://demoqa.com/text-box', 'Testing')
def test_demoqa_simple_practice_form():
    # GIVEN
    with allure.step('Open registration form and create user'):
        app.left_panel.open_simple_registration_form()
        vika = users.simple_vika

    # WHEN
    with allure.step('Fill form'):
        app.simple_registration_page.register(vika)

    # THEN
    with allure.step('Check form results'):
        app.simple_registration_page.should_have_submitted(vika)


@allure.feature('Registration form')
@allure.title('Test of student registration form')
@allure.description('This test includes only general steps of the student registration form')
@allure.tag('Registration Form', 'Student', 'class User')
@allure.severity(severity_level=Severity.CRITICAL)
@allure.label('owner', 'Tom Smith')
@allure.link('https://demoqa.com/automation-practice-form', 'Testing')
def test_demoqa_practice_form_general_step():
    # GIVEN
    with allure.step('Open registration form and create user'):
        app.left_panel.open_registration_form()
        vika = users.vika

    # WHEN
    with allure.step('Fill form'):
        app.registration_steps.register(users.vika)

    # THEN
    with allure.step('Check form results'):
        app.registration_steps.should_have_registered(users.vika)


@allure.feature('Registration form')
@allure.title('Test of student registration form considering all steps')
@allure.description('This test includes all steps of the student registration form')
@allure.tag('Registration Form', 'Student')
@allure.severity(severity_level=Severity.TRIVIAL)
@allure.label('owner', 'Ivan Ivanov')
@allure.link('https://demoqa.com/automation-practice-form', 'Testing')
def test_demoqa_practice_form_all_steps():
    # GIVEN
    with allure.step('Open registration form'):
        app.left_panel.open_registration_form()

    # WHEN
    with allure.step('Fill form'):
        app.registration_page.fill_first_name('Viktoriia')
        app.registration_page.fill_last_name('Lav')
        app.registration_page.fill_user_email('newuser@gmail.com')
        app.registration_page.fill_gender('Female')
        app.registration_page.fill_user_number('8800222334')

        app.registration_page.fill_date_of_birth(date(1993, 5, 17))

        app.registration_page.fill_subjects('Chemistry')
        app.registration_page.fill_hobbies('Sports')
        app.registration_page.fill_hobbies('Reading')

        app.registration_page.upload_picture('photo.png')

        app.registration_page.fill_current_address('144 Broadway, suit 12')
        app.registration_page.fill_state('NCR')
        app.registration_page.fill_city('Gurgaon')

        app.registration_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.registration_page.should_have_submitting_form()
        app.registration_page.should_have_registered('Viktoriia Lav',
                                                 'newuser@gmail.com',
                                                 'Female',
                                                 '8800222334',
                                                 date(1993, 5, 17),
                                                 'Chemistry',
                                                 'Sports, Reading',
                                                 'photo.png',
                                                 '144 Broadway, suit 12',
                                                 'NCR Gurgaon')