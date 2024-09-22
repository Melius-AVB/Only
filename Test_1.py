from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://only.digital/projects#brief")
driver.implicitly_wait(15)
waits=WebDriverWait(driver, 10)
time.sleep(5)

NAME=driver.find_element_by_name("name")
NAME.send_keys('Test_1')

MAIL=driver.find_element_by_name('email')
MAIL.send_keys('Test_1@mail.com')

PHONE=driver.find_element_by_name('phone')
PHONE.click()
PHONE.send_keys('9111111111')

COMPANY=driver.find_element_by_name('company')
COMPANY.send_keys('Test_1')

driver.find_element_by_xpath("//span[text()='Дизайн']").click()

COMENT=driver.find_element_by_css_selector('[placeholder="Расскажите о вашем проекте"]')
COMENT.send_keys('Test_1,Test_2,Test_3,Test_4,Test_5,Test_6')

#File=('C:\IMG_1758.jpeg')
#Upload = driver.find_element_by_xpath("//span[text()='Прикрепить файл']")
#Upload.send_keys(File)

driver.find_element_by_xpath("//span[text()='3–5 млн']").click()

driver.find_element_by_xpath("//span[text()='Соцсети']").click()

#time.sleep(3)
#CAP=driver.find_element_by_class_name('rc-anchor-center-item')
#driver.execute_script("return arguments[0].scrollIntoView(true);", CAP)
#CAP.click()
#time.time(5)
driver.find_element_by_xpath("//span[text()='Отправить']").click()
