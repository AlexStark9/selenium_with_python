from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://bestmerchant.ru/pages/authentication/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    input1 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/input")
    # input1.click()
    input1.send_keys("Tester")
    input2 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div/div/input")
    # input2.click()
    input2.send_keys("Osa2677678+")
    button = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
