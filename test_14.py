import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x: int):
    x = int(x)
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'),
                                                                                       "$100"))
    browser.find_element(By.XPATH, '//*[@id="book"]').click()

    x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text

    browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(calc(x))

    browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
