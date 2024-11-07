from assistant.config import settings
import pytest
from playwright.sync_api import Page, expect, sync_playwright

def test_location(page:Page):
    page.get_by_placeholder("Поиск").click()
    page.get_by_placeholder("Поиск").fill("Минусинск")
    page.get_by_text("Минусинск ЛО_CENALOM662610").click()
    page.get_by_role("button", name="Выбрать")