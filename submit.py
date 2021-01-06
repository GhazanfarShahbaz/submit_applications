from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Maybe better to just put this into a text file?

data = {line[:line.find("=")].strip(): line[line.find("=")+1:].strip() for line in open("data.txt", "r")}


CUSTOM_QUESTIONS_ANSWERS = {
    "How did you hear about us?" : "TEST1",
    "Given the pandemic, what is your internship plan? When are you available to start?" : "TEST2"
}
CUSTOM_QUESTIONS = []

browser = webdriver.Chrome()
browser.get('https://jobs.lever.co/unify/dca0a7bd-41ab-4f24-a1c3-3176520f7437/apply')

for x in browser.find_elements_by_xpath("//input"):
    print(x.text)


browser.find_element_by_xpath('//input[@name = "resume"]').send_keys(data['RESUME'])
browser.find_element_by_xpath('//input[@name = "name"]').send_keys(data['FULL_NAME'])
# browser.find_element_by_xpath('//input[@name = "email"]').clear()
browser.find_element_by_xpath('//input[@name = "email"]').send_keys(data['PHONE'])
browser.find_element_by_xpath('//input[@name = "phone"]').send_keys(data['PHONE'])
browser.find_element_by_xpath('//input[@name = "org"]').send_keys(data['CURRENT_COMPANY'])
browser.find_element_by_xpath('//input[@name = "urls[LinkedIn]"]').send_keys(data['LINKEDIN_URL'])
browser.find_element_by_xpath('//input[@name = "urls[GitHub]"]').send_keys(data['GITHUB_URL'])

browser.find_element_by_xpath('//textarea[@name = "comments"]').send_keys(data['ADDITIONAL_INFORMATION'])

#next line is submit
# browser.find_element_by_xpath('//button[@class = "postings-btn template-btn-submit cerulean"]').click()

"""
Have to make it so that custom questions ask for input
"""


for x in browser.find_elements_by_xpath('//div[@class="application-label full-width textarea"]'):
    val = x.text
    val = val[0: len(val)-1].strip()
    CUSTOM_QUESTIONS.append(val)


for x,y in enumerate(browser.find_elements_by_xpath('//textarea[@class="card-field-input"]')):
    # y.send_keys(CUSTOM_QUESTIONS_ANSWERS(CUSTOM_QUESTIONS[x]))
    q = CUSTOM_QUESTIONS[x]
    a = CUSTOM_QUESTIONS_ANSWERS[q]
    y.send_keys(a)
    # print(CUSTOM_QUESTIONS_ANSWERS(CUSTOM_QUESTIONS[x]))

print(CUSTOM_QUESTIONS)
