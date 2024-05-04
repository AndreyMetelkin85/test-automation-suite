import allure
from test_ui.conftest import page_fixture, text_box_form_data, registration_form_data
from test_ui.conftest import wait


@allure.story("Elements")
@allure.title("Тест проверяет заполнение тестовой формы и как отображаются данные в ответе")
def test_element_text_box(driver, page_fixture, text_box_form_data):
    text_box_form_data = text_box_form_data.text_box_form_data
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()
    tools_qa_home_page = page_fixture.demo_qa_home_page.tools_qa_label()
    assert tools_qa_home_page.is_displayed()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    left_panel_tex_box_buttons = page_fixture.demo_qa_home_page.left_panel_buttons()
    left_panel_tex_box_buttons[0].click()

    text_box_label = page_fixture.elements_page.text_box_label()
    text_box_label.is_displayed()

    text_box_form_full_name = page_fixture.elements_page.user_name_input()
    text_box_form_full_name.send_keys(text_box_form_data["fullname"])

    text_box_form_email = page_fixture.elements_page.user_email_input()
    text_box_form_email.send_keys(text_box_form_data["email"])

    text_box_form_current_address = page_fixture.elements_page.current_address_input()
    text_box_form_current_address.send_keys(text_box_form_data["current address"])

    text_box_form_permanent_address = page_fixture.elements_page.permanent_address_input()
    text_box_form_permanent_address.send_keys(text_box_form_data["permanent address"])

    text_box_submit_button = page_fixture.elements_page.submit_button()
    text_box_submit_button.click()

    result_output = page_fixture.elements_page.output_field()
    output_text = [element.text for element in result_output]

    for key, value in text_box_form_data.items():
        value_cleaned = value.replace('\n', ' ').strip()
        assert any(
            value_cleaned in text for text in output_text), f"[INFO!!!] Ошибка, значение - '{value}' не найдено!!!"


@allure.story("Elements")
@allure.title("Тест проверяет общее раскрытие и закрытие check_box")
def test_check_box_expand_and_close_folders(driver, page_fixture):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[1].click()

    check_box_expand_button = page_fixture.elements_page.expand_all_button()
    check_box_expand_button.click()

    check_box_collapse_all_button = page_fixture.elements_page.collapse_all_button()
    check_box_collapse_all_button.click()


@allure.story("Elements")
@allure.title("Тест проверяет кликабельность check_box")
def test_check_box_home_click(driver, page_fixture):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[1].click()

    home_dropdown_arrow = page_fixture.elements_page.dropdown_arrow_home_button()
    home_dropdown_arrow.click()

    home_title = page_fixture.elements_page.home_title()
    home_title.click()

    chose_result = page_fixture.elements_page.you_have_selected_results()
    chose_result.is_displayed()


@allure.story("Elements")
@allure.title("Тест проверяет кликабельность и ответ при выборе нужного radio button")
def test_radio_button_check(driver, page_fixture):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[2].click()

    radio_button_yes = page_fixture.elements_page.radio_button_yes()
    driver.execute_script("arguments[0].click();", radio_button_yes)

    radio_button_result = page_fixture.elements_page.selected_result()
    assert radio_button_result.is_displayed()

    radio_button_impressive = page_fixture.elements_page.radio_button_impressive()
    driver.execute_script("arguments[0].click();", radio_button_impressive)

    radio_button_result = page_fixture.elements_page.selected_result()
    assert radio_button_result.is_displayed()


@allure.story("Elements")
@allure.title("Тест проверяет форму регистрации")
def test_submit_registration_form(driver, page_fixture, registration_form_data, wait):
    registration_form_data = registration_form_data.registration_form_data()
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[3].click()

    page_fixture.elements_page.add_button()

    registration_form_label = page_fixture.registration_form.registration_form_label()
    wait.wait_until_the_element_is_visible(registration_form_label)
    assert registration_form_label.is_displayed()

    page_fixture.registration_form.fill_form_and_submit(
        first_name=registration_form_data["first_name"],
        last_name=registration_form_data["last_name"],
        email=registration_form_data["email"],
        age=registration_form_data["age"],
        salary=registration_form_data["salary"],
        department=registration_form_data["department"])

    result = page_fixture.elements_page.results_table()
    result_text = [element.text for element in result]
    element_results = [text.replace('\n', ' ').strip() for text in result_text]

    for key, value in registration_form_data.items():
        value_str = str(value)
        assert any(value_str in text for text in element_results)


@allure.story("Elements")
@allure.title("Тест проверяет обновление информации о пользователе")
def test_update_user_data(driver, page_fixture, registration_form_data, wait):
    registration_form_data_update = registration_form_data.registration_form_data()
    registration_form_data = registration_form_data.registration_form_data()
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[3].click()

    page_fixture.elements_page.add_button()

    registration_form_label = page_fixture.registration_form.registration_form_label()
    wait.wait_until_the_element_is_visible(registration_form_label)
    assert registration_form_label.is_displayed()

    page_fixture.registration_form.fill_form_and_submit(
        first_name=registration_form_data["first_name"],
        last_name=registration_form_data["last_name"],
        email=registration_form_data["email"],
        age=registration_form_data["age"],
        salary=registration_form_data["salary"],
        department=registration_form_data["department"])

    result_table = page_fixture.elements_page.results_table()
    text_result = [customer.text for customer in result_table]
    element_results = [text.replace('\n', ' ').strip() for text in text_result]

    name_updated = False
    for idx, text_value in enumerate(element_results):
        values = text_value.split()
        if len(values) >= 1:
            for reg_value in registration_form_data.values():
                if values[0] == reg_value:
                    update_button = page_fixture.elements_page.update_data_button()
                    update_button[idx].click()
                    update_name_data = page_fixture.registration_form.first_name()
                    update_name_data.clear()
                    update_name_data.send_keys(registration_form_data_update["first_name"])
                    submit_button = page_fixture.registration_form.submit_button()
                    submit_button.click()
                    name_updated = True
                    break
            if name_updated:
                break
        else:
            continue

    assert name_updated, "[INFO!!!] Обновленное имя не найдено в элементах таблицы"
