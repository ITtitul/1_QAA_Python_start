import os
from selene import browser, be, have

#browser.open('I:\Мой диск\Aqua\QA Automation\Getting started with Python for Automated Testing in Browser\login.html')
url = "file://" + os.path.abspath("Autorized_login.html")
browser.open(url)
browser.element('[id="username"]').should(be.blank).type('admin')
browser.element('[id="password"]').should(be.blank).type('admin_password')
browser.element('button[type="submit"]').click()
browser.switch_to.alert.accept()
#input("Нажми Enter  для завершения теста!")
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

