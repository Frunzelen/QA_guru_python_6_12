import allure
from allure_commons.types import Severity
from selene import browser, be, have, command

from demoqa.pages.registration_page import RegistrationPage

@allure.title("Успешная регистрация на сайте demoqa.com")
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'selenamond')
@allure.description('Данные студента соответсвуют отправленным данным при регистрации')
@allure.story('Регистрация студента')
def test_for_registration_form_demoqa():
    # GIVEN
    with allure.step("Открыли страницу регистрации"):
        registration_page = RegistrationPage()
        registration_page.open()

    # WHEN
    with allure.step("Заполнили все поля формы регистрации"):
        (registration_page
        .fill_first_name('Angelina')
        .fill_last_name('Jolie')
        .fill_email('AngelinaJolie@email.ru')
        .fill_gender('Female')
        .fill_mobile_number('1234567890')
        .fill_date_of_birth('4', 'June', '1975')
        .fill_subjects('Biology')
        .fill_hobbies('Sports')
        .select_picture('Angelina_Jolie.jpg')
        .fill_address('Los Angeles, Borogodskaya, 17')
        .fill_state("NCR")
        .fill_city("Delhi")
        .submit_form()
         )

    # THEN
    with allure.step("Проверили заполненные поля"):
        registration_page.should_have_text('Thanks for submitting the form')
        registration_page.registered_user_data.should(
            have.exact_texts(
                'Angelina Jolie',
                'AngelinaJolie@email.ru',
                'Female',
                '1234567890',
                '04 June,1975',
                'Biology',
                'Sports',
                'Angelina_Jolie.jpg',
                'Los Angeles, Borogodskaya, 17',
                'NCR Delhi')
        )

    # WHEN
    with allure.step("Закрыли форму регистрации"):
        registration_page.close()

    # THEN
    with allure.step("Проверяем,что открылась пустая форма регистрации"):
        registration_page.cleared_registration_form()