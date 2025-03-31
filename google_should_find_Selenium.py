from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver (Chrome)
driver = webdriver.Chrome()

try:
    # Открываем Google
    driver.get("https://google.com")

    # Ожидаем, пока строка поиска станет доступной
    search_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Вводим текст в строку поиска и отправляем запрос
    search_box.clear()  # Аналог be.blank
    search_box.send_keys("yashaka/selene")
    search_box.send_keys(Keys.RETURN)

    # Проверяем, что в HTML-странице присутствует нужный текст
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "html"), "About this page")
    )

    # Проверяем, что в результатах поиска есть упоминание о Selene
    search_results = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    assert "Selene - User-oriented Web UI browser tests in Python" in search_results.text

finally:
    # Закрываем браузер
    driver.quit()
