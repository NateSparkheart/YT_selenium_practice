from selenium import webdriver
import random
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "Hello Frien!")

#options.add_argument(f"user-agent={random.choice(user_agents)}")
options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Firefox(options=options)
driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
driver.get_screenshot_as_file('C:\\Users\\kappa\\Desktop\\1.png')
driver.quit()

