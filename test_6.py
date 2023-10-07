from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("test@mail.ru")
    input4 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
    input4.send_keys("+79998547963")
    input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Russia")

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()
