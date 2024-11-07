from assistant.config import settings
import pytest
from playwright.sync_api import Page, expect, sync_playwright

#Authorization
def test_auth(page:Page):
    page.goto(settings.base_url)
    page.get_by_label("Логин").click()
    page.get_by_label("Логин").fill(settings.login_user)
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill(settings.password_user)
    page.get_by_role("button", name="Войти").click()
    
    
#location   
def test_location(page:Page):
    page.get_by_placeholder("Поиск").click()
    page.get_by_placeholder("Поиск").fill("Минусинск")
    page.get_by_text("Минусинск ЛО_CENALOM662610").click()
    page.get_by_role("button", name="Выбрать")
    

#serch items  
def test_search_items(page:Page):
    page.get_by_role("button", name="Поиск").click()
    page.get_by_placeholder("Поиск").click()
    page.get_by_placeholder("Поиск").fill("br1243")
    page.get_by_text("Блендер погружной BRAYER").click()
    page.get_by_role("button", name="Выбрать").click()
    
    
#install customer
def test_create_customer(page:Page):
    page.get_by_placeholder("+7 (9__) - ___ - ____").click()
    page.get_by_placeholder("+7 (9__) - ___ - ____").fill("+7 (923) 314 36-23")
    page.locator("._button_1jt2t_1").first.click()
    
    
    
#use bonuses
def use_bonuses(page:Page):
    page.get_by_role("button", name="Списать баллы").click()
    page.get_by_placeholder("399").click()
    page.get_by_placeholder("399").fill("399")
    
#send to the cashier
def send_to_the_cashier(page:Page):
    page.locator("div").filter(has_text=re.compile(r"^Список товаровМинусинск ЛО_CENALOMОтправить на кассуУдалить корзину$")).get_by_role("button").click()
    page.get_by_role("button", name="Отправить на кассу").click()
    page.locator("div").filter(has_text="Корзина отправлена на кассу").nth(4).click()
    
    
    
#settings.base_url.close()

# with sync_playwright() as playwright:
#     run(playwright)