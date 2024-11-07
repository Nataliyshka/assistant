from assistant.config import settings
import pytest
from playwright.sync_api import Page, expect, sync_playwright

# @pytest.fixture(scope="function", autouse=True)
# def page_fixture():
#     with sync_playwright() as p:
#         # Запускаем браузер в режиме headful
#         geo = {"longitude": 91.657232, "latitude": 53.693689} минусинск
#         browser = p.chromium.launch(headless=False, geolocation=geo)  # Установите headless=False
#         page = browser.new_page()
#         yield page
#         browser.close()

def test_auth(page: Page):
    page.goto(settings.base_url)
    page.get_by_label("Логин").click()
    page.get_by_label("Логин").fill(settings.login_user)
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill(settings.password_user)
    page.get_by_role("button", name="Войти").click()
    
    
    #подтверждение нахождение местоположения 
    #page.get_by_role("button", name="Да").click()
    
    page.wait_for_timeout(5000)
