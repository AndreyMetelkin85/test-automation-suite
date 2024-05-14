import allure
import pytest
from test_ui.conftest import page_fixture, text_box_form_data, registration_form_data, perform_double_click, \
    perform_right_click, perform_normal_click
from test_ui.conftest import wait
from file.constants import PATH_TO_FILE


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


@allure.story("Elements")
@allure.title("Тест проверяет удаление пользователя")
def test_delete_user_data(driver, page_fixture, registration_form_data, wait):
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
    result_text = [custom.text for custom in result]
    element_results = [text.replace('\n', ' ').split() for text in result_text]

    user_delete = True
    for idx, values in enumerate(element_results):
        if len(values) >= 1:
            for reg_value in registration_form_data.values():
                if values[0] == reg_value:
                    delete_buttons = page_fixture.elements_page.delete_user()
                    delete_buttons[idx].click()
                    user_delete = False
                    break
            if not user_delete:
                break
        else:
            continue

    assert not user_delete, "[INFO!!!], Пользователь не удалён из таблицы"


@allure.story("Elements")
@allure.title("Тест проверяет клики по кнопкам с разными параметрами такими как :"
              " Двойной клик, клик правой кнопкой, динамический клик")
@pytest.mark.parametrize("click_parameter, expected_text",
                         [
                             ("double_click_button", "You have done a double click"),
                             ("right_click_button", "You have done a right click"),
                             ("click_me_button", "You have done a dynamic click")
                         ])
def test_button_clickability_check(driver, page_fixture, perform_right_click, perform_double_click, click_parameter,
                                   expected_text):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[4].click()

    click_buttons = getattr(page_fixture.elements_page, click_parameter)()

    if click_parameter == "double_click_button":
        perform_double_click(click_buttons)
    elif click_parameter == "right_click_button":
        perform_right_click(click_buttons)
    else:
        click_buttons.click()

    info_after_click = page_fixture.elements_page.results_button_click()
    info_text = [custom.text for custom in info_after_click]

    assert any(expected_text in text for text in
               info_text), f"Expected text '{expected_text}' not found in info text: {info_text}"


@allure.story("Elements")
@allure.title("Тест проверяет две кнопки которые открывают новую вкладку с домашней страницей.")
@pytest.mark.parametrize("following_links", ["open_new_tab_home_page", "open_new_tab_dynamic_link_home_page"])
def test_open_new_tab_home_page(driver, page_fixture, wait, following_links):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()

    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[5].click()

    home_page_button = getattr(page_fixture.elements_page, following_links)()
    if following_links == "open_new_tab_home_page":
        home_page_button.click()
    else:
        home_page_button.click()

    driver.switch_to.window(driver.window_handles[1])

    expected_url = "https://demoqa.com/"
    wait.wait_until_the_url_is_visible(expected_url)
    current_url = driver.current_url
    assert current_url == expected_url, "[INFO!!!] URL адрес не был найден!!! "


@allure.story("Elements")
@allure.title("Тест проверяет сообщение из ответ от бэкенда.")
@pytest.mark.parametrize("click_link_button, expected_message", [
    ("created_send_api_call", "Link has responded with staus 201 and status text Created"),
    ("no_content_send_api_call", "Link has responded with staus 204 and status text No Content"),
    ("moved_send_api_call", "Link has responded with staus 301 and status text Moved Permanently"),
    ("bad_request_send_api_call", "Link has responded with staus 400 and status text Bad Request"),
    ("unauthorized_send_api_call", "Link has responded with staus 401 and status text Unauthorized"),
    ("forbidden_send_api_call", "Link has responded with staus 403 and status text Forbidden"),
    ("invalid_url_send_api_call", "Link has responded with staus 404 and status text Not Found")
])
def test_links_will_send_api_call(driver, page_fixture, wait, click_link_button, expected_message):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()
    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()
    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[5].click()

    following_links_buttons = getattr(page_fixture.elements_page, click_link_button)()
    following_links_buttons.click()

    results_message_and_code = page_fixture.elements_page.response_text()[0]
    assert results_message_and_code.text == expected_message, "[INFO!!!] Сообщения отсутствуют!!!"


@allure.story("Elements")
@allure.title("Тест функциональности загрузки файла")
def test_file_upload_functionali(driver, page_fixture):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()
    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[7].click()

    download_button = page_fixture.elements_page.download_button()
    download_button.click()


@allure.story("Elements")
@allure.title("Тест функциональности загрузки файла")
def test_download_functionali(driver, page_fixture, perform_normal_click):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()
    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[7].click()

    download_button = page_fixture.elements_page.upload_file()
    download_button.send_keys(PATH_TO_FILE)

    result_message = page_fixture.elements_page.result_upload_file()
    assert result_message.text == "{}\\file.pdf".format("C:\\fakepath"), "[INFO!!!] Файл не загружен!!!"


@allure.story("Elements")
@allure.title("Проверка динамического нажатия на кнопки")
@pytest.mark.parametrize("buttons", ["will_enable_button", "color_change_button", "visible_after_button"])
def test_check_dynamic_click_button(driver, page_fixture, wait, buttons):
    page_fixture.go_to_web_site_demo_qa.go_to_web_site_demo_qa()
    elements_button = page_fixture.demo_qa_home_page.category_cards_home_page()
    elements_button[0].click()

    elements_button_check_box = page_fixture.demo_qa_home_page.left_panel_buttons()
    elements_button_check_box[8].click()

    dynamic_button = getattr(page_fixture.elements_page, buttons)()
    wait.wait_until_element_is_clickable(dynamic_button)
    dynamic_button.click()

    if buttons == "color_change_button":
        result_button_change_color = page_fixture.elements_page.color_change_button_result()
        assert result_button_change_color, "[INFO!!!] Цвет кнопки не изменился"
