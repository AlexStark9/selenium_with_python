from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: int):
    x = int(x)
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = img.get_attribute('valuex')

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x))

    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    option2.click()

    button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
