from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from configparser import ConfigParser

# Put your email and password for linkein in config.ini file 

file = "config.ini"
config = ConfigParser()
config.read(file)
EMAIL = config['Account']['EMAIL']
PASSWORD = config['Account']['PASSWORD']
CONNECTION_LIMIT = 10
# You can set here how many connections you want to send request

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

driver.get("https://www.linkedin.com/login")

action = ActionChains(driver)
driver.implicitly_wait(10)


email = driver.find_element(By.XPATH, "//input[@id='username']")
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(PASSWORD)

submit = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
submit.click()

network = driver.find_element(By.XPATH, "//a[@data-link-to='mynetwork']")
network.click()

links = driver.find_elements(By.XPATH, "(//ul[contains(@class,'artdeco-card')]/li)[1]/ul/li")

sections = driver.find_elements(By.XPATH, "//ul[contains(@class,'artdeco-card')]/li")
req_sent = 0
for sec in sections:
    text = sec.find_element(By.XPATH, './/div/h2').text
    print(text)
    links = sec.find_elements(By.XPATH, ".//ul/li")
    for card in links:
        if req_sent >= 10:
            break
        time.sleep(2)
        btn = card.find_element(By.XPATH, ".//button[contains(@aria-label,'Follow') or contains(@aria-label , 'connect')]")
        try:
            btn.click()
            req_sent = req_sent + 1
            print("[+] Request sent ")
        except:
            pass

