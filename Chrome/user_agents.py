from selenium import webdriver
import random
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.ChromeOptions()

user_agents = ['Mozilla/5.0 (X11; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0',
               'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/[WEBKIT_VERSION] (KHTML, '
               'like Gecko; Mediapartners-Google) Chrome/[CHROME_VERSION] Mobile Safari/[WEBKIT_VERSION]',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 '
               'Safari/537.36 Edg/88.0.705.63']
#options.add_argument(f"user-agent={random.choice(user_agents)}")
options.add_argument(f"user-agent={useragent.random}")


driver = webdriver.Chrome(options=options)
driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
driver.get_screenshot_as_file('C:\\Users\\kappa\\Desktop\\1.png')
driver.quit()

