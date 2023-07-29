# Автотесты web-приложения Интернет-банк idemo.bspb.ru

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
from unittest import TestCase as TC
import pytest

s = Service("C:/Users/k_tomilov/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/")
time.sleep(2)
driver.set_window_size(1366, 768)

f_name = '//*[@id="login-form"]/div[1]/input'
f_password = '//*[@id="login-form"]/div[2]/input'
f_button = '//*[@id="login-button"]'
otp_code = '//*[@id="otp-code"]'
otp_button = '//*[@id="login-otp-button"]'
payments_form = '//*[@id="payments-form"]'
smart_payment = '//*[@id="smart-payment"]'
deposit = 'html/body/div[7]/ul/li[1]'
dfe = driver.find_element

def out_passed():
    print("\033[32m{}\033[0m".format("Test passed"))
def out_failed():
    print("\033[31m{}\033[0m".format("Test failed"))

def alert(d):
    try:
        d
        out_passed()
    except:
        out_failed()


alert(dfe(By.XPATH, f_name).clear())
alert(dfe(By.XPATH, f_name).send_keys("demo"))
alert(dfe(By.XPATH, f_password).clear())
alert(dfe(By.XPATH, f_password).send_keys("demo"))
dfe(By.XPATH, f_button).click()
time.sleep(5)
alert(dfe(By.XPATH, otp_code).clear())
alert(dfe(By.XPATH, otp_code).send_keys("0000"))
alert(dfe(By.XPATH, otp_button).click())

# "Платежи и переводы"
alert(dfe(By.XPATH, payments_form).click())
alert(dfe(By.XPATH, smart_payment).clear())
alert(dfe(By.XPATH, smart_payment).send_keys('40817 810 0 6666 6666667 Королёва Ольга'))
time.sleep(5)
alert(dfe(By.XPATH, deposit).click())

# Переводы

acc2 = '//*[@id="acc2"]' # счёт куда?
acc2_1 = '//*[@id="acc2"]/option[2]'  # счёт куда _2?
amount = '//*[@id="amount"]'
forward = '//*[@id="forward"]'

alert(dfe(By.XPATH, acc2_1).click())
alert(dfe(By.XPATH, amount).clear())
alert(dfe(By.XPATH, amount).send_keys("1000"))
alert(dfe(By.XPATH, forward).click())
