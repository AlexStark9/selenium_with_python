from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: int):
    x = int(x)
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x))

    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    option2.click()

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
