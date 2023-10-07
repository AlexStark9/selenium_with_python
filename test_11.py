from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    input3.send_keys("test@mail.ru")

    file = browser.find_element(By.XPATH, '//*[@id="file"]')
    file_path = os.path.join(r'C:\Users\alexs\Downloads', 'file.txt')
    file.send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
