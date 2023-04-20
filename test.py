from time import sleep
from selene import have
from selene.support.shared import browser

browser.open('https://duckduckgo.com/')
browser.element('[name="q"]').type('itstep').press_enter()
browser.all('.Wo6ZAEmESLNUuWBkbMxx')[0].click()
browser.element('.menu__link ').click()

