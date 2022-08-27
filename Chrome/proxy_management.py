#from selenium import webdriver
import time
from fake_useragent import UserAgent
from seleniumwire import webdriver

# user_agent_list = ["sguwenka",
#                    "best_agent_evah",
#                    "java_#_best_language"]

# proxy_options = {
#     "proxy": {
#         "https": f"http://{login}:{password}@138.128.91.65:8000"
#     }
# }

#seting proxy
proxy= "185.16.138.104"
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities["marionette"] = True
useragent = UserAgent()

firefox_capabilities["proxy"] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}

#options = webdriver.ChromeOptions()
options = webdriver.FirefoxOptions()
options.set_preference("general_useragent_override", useragent.random)

useragent = UserAgent()

#options.add_argument(f"user-agent={useragent.random}")
#options.add_argument("--proxy-server=185.16.138.104")

#driver = webdriver.Chrome()  #(options=options)
driver = webdriver.Firefox(options=options, proxy=proxy)
driver.get("https://2ip.ru")
time.sleep(5)

driver.close()
driver.quit()
