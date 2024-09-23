from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

browser = webdriver.Chrome()
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
browser.get(link)

button = (browser.find_element(By.XPATH, "//a[@href='/ru/basket/]'"))
button.click()

