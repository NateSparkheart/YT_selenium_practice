import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from auth_data import vk_login, vk_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle # сохранение куки


driver = webdriver.Chrome()
driver.get('https://vk.com/')


# login_field = driver.find_element(By.ID, "index_email")
# login_field.send_keys(vk_login)
# driver.find_element(By.CSS_SELECTOR, "button.FlatButton.FlatButton--primary.FlatButton--size-l.FlatButton--wide"
#                                          ".VkIdForm__button.VkIdForm__signInButton > span").click()
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button > span.vkuiButton__in")))
# driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(vk_password)
# driver.find_element(By.CSS_SELECTOR, "button > span.vkuiButton__in").click()
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#l_nwsf > a > span.left_label.inl_bl")))
# driver.find_element(By.CSS_SELECTOR, "#l_nwsf > a > span.left_label.inl_bl").click()
#
# time.sleep(3)
# # cookies
# pickle.dump(driver.get_cookies(), open(f"{vk_login}_cookies", "wb"))
#

# time.sleep(5)
#
for cookie in pickle.load(open(f"{vk_login}_cookies", "rb")):
    driver.add_cookie(cookie)

time.sleep(2)
driver.refresh()
time.sleep(10)

driver.quit()

