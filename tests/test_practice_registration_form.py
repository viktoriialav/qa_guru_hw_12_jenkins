from datetime import date

from demoqa_tests.application import app
from demoqa_tests.data import users


def test_demoqa_simple_practice_form():
    # GIVEN
    app.left_panel.open_simple_registration_form()
    vika = users.simple_vika

    # WHEN
    app.simple_registration_page.register(vika)

    # THEN
    app.simple_registration_page.should_have_submitted(vika)


def test_demoqa_practice_form_general_step():
    # GIVEN
    app.left_panel.open_registration_form()
    vika = users.vika

    # WHEN
    app.registration_steps.register(users.vika)

    # THEN
    app.registration_steps.should_have_registered(users.vika)


def test_demoqa_practice_form_all_steps():
    # GIVEN
    app.left_panel.open_registration_form()

    # WHEN
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