from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Запускаем браузер
    context = browser.new_context()
    page = context.new_page()

    # Открываем Google
    page.goto('https://google.com')

    # Вводим поисковый запрос
    search_box = page.locator('[name="q"]')
    search_box.fill('yashaka/selene')
    search_box.press('Enter')

    # Ожидание загрузки результатов поиска
    search_results = page.locator('#search')
    search_results.wait_for()

    # Проверка наличия текста
    assert 'Selene - User-oriented Web UI browser tests in Python' in search_results.inner_text()

    # Закрываем браузер
    browser.close()

# Запуск Playwright
with sync_playwright() as playwright:
    run(playwright)
