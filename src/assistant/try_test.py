# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(
#         geolocation={"longitude": 41.890221, "latitude": 12.492348},
#         permissions=["geolocation"]
#     )
#     page = context.new_page()
#     page.goto("https://stage-assistant.cenalom.tech/login")
#     page.get_by_label("Логин").click()
#     page.get_by_label("Логин").press("CapsLock")
#     page.get_by_label("Логин").fill("У")
#     page.get_by_label("Логин").press("CapsLock")
#     page.get_by_label("Логин").fill("")
#     page.get_by_label("Логин").press("CapsLock")
#     page.get_by_label("Логин").fill("Ц")
#     page.get_by_label("Логин").press("CapsLock")
#     page.get_by_label("Логин").fill("Цепелева ")
#     page.get_by_label("Логин").press("CapsLock")
#     page.get_by_label("Логин").fill("Цепелева Н")
#     page.get_by_label("Логин").press("CapsLock")
#     page.get_by_label("Логин").fill("Цепелева Наталья")
#     page.get_by_label("Пароль").click()
#     page.get_by_label("Пароль").fill("6vmzmvk8")
#     page.get_by_role("button", name="Войти").click()
#     page.wait_for_timeout(10000)

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
