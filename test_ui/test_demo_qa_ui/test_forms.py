import random
import allure
from conftest import page_fixture, student_registration_form, scroll_down
from file.constants import PATH_TO_PHOTO


@allure.story("Practice Form")
@allure.title("Проверка отправки формы регистрации студента")
def test_student_registration_form(driver, scroll_down, page_fixture, student_registration_form):
    student_registration_form_data = student_registration_form.student_registration_form()
    subject_choices = ["Physics", "Maths", "Biology", "Chemistry", "English", "History"]
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[1].click()

    left_panel_tex_box_buttons = page_fixture.demo_qa_home_page.left_panel_buttons()
    left_panel_tex_box_buttons[0].click()

    practice_form_label = page_fixture.practice_form.practice_form_label()
    assert practice_form_label.is_displayed()

    student_registration_form_label = page_fixture.practice_form.student_registration_form_label()
    assert student_registration_form_label.is_displayed()

    first_name = page_fixture.practice_form.first_name_input()
    first_name.send_keys(student_registration_form_data.first_name)

    last_name = page_fixture.practice_form.last_name_input()
    last_name.send_keys(student_registration_form_data.last_name)

    user_email = page_fixture.practice_form.user_email_input()
    user_email.send_keys(student_registration_form_data.email)

    gender_choice = page_fixture.practice_form.gender_input()
    selecting_gender = random.choice(gender_choice)
    selecting_gender.click()

    mobile_number = page_fixture.practice_form.mobile_number_input()
    mobile_number.send_keys(student_registration_form_data.mobile_number)

    hobbies_choice = page_fixture.practice_form.hobbies_input()
    selecting_hobbies = random.choice(hobbies_choice)
    selecting_hobbies.click()

    picture_upload = page_fixture.practice_form.upload_picture()
    picture_upload.send_keys(PATH_TO_PHOTO)

    current_address = page_fixture.practice_form.current_address_input()
    current_address.send_keys(student_registration_form_data.current_address)

    scroll_down(200)

    state_input = page_fixture.practice_form.state_dropdown()
    state_input.click()

    state_dropdown_open = page_fixture.practice_form.state_and_city_dropdown_open()
    random_index_state = random.randint(0, 3)
    state_dropdown_open[random_index_state].mouse_hover()
    state_dropdown_open[random_index_state].click()

    city_input = page_fixture.practice_form.city_dropdown()
    city_input.click()

    city_dropdown_open = page_fixture.practice_form.state_and_city_dropdown_open()
    random_index_city = random.randint(0, 1)
    city_dropdown_open[random_index_city].mouse_hover()
    city_dropdown_open[random_index_city].click()

    submit_button = page_fixture.practice_form.submit_button()
    submit_button.click()

    result = page_fixture.practice_form.result_submitting_form()
    output_text = [element.text for element in result]

    check_result = False
    for key, value in enumerate(output_text):
        if student_registration_form_data.first_name in value:
            check_result = True
            break
    assert check_result is not False
