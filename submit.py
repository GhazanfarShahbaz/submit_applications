from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

RESUME = "THIS SHOULD BE A PATH"
FIRST_NAME = ""
LAST_NAME = ""
FULL_NAME = ""
EMAIL = ""
SCHOOL_EMAIL = ""
PHONE = ""
LINKEDIN_URL = ""
GITHUB_URL = ""
CURRENT_COMPANY = ""
ADDITIONAL_INFORMATION = ""

browser = webdriver.Chrome()
browser.get('https://jobs.lever.co/applied/c22805d5-2006-4867-bb32-671951b17206/apply')
browser.find_element_by_xpath('//input[@name = "resume"]').send_keys(RESUME)
browser.find_element_by_xpath('//input[@name = "name"]').send_keys(FULL_NAME)
# browser.find_element_by_xpath('//input[@name = "email"]').clear()
browser.find_element_by_xpath('//input[@name = "email"]').send_keys(EMAIL)
browser.find_element_by_xpath('//input[@name = "phone"]').send_keys(PHONE)
browser.find_element_by_xpath('//input[@name = "org"]').send_keys(CURRENT_COMPANY)
browser.find_element_by_xpath('//input[@name = "urls[LinkedIn]"]').send_keys(LINKEDIN_URL)
browser.find_element_by_xpath('//input[@name = "urls[GitHub]"]').send_keys(GITHUB_URL)

browser.find_element_by_xpath('//textarea[@name = "comments"]').send_keys(ADDITIONAL_INFORMATION)
browser.find_element_by_xpath('//button[@class = "postings-btn template-btn-submit cerulean"]').click()