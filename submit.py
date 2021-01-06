from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def processData() -> dict:
    data = {}
    dataFile = open("data.txt", "r")

    for line in dataFile:
        partitiionAt = line.find("=")
        data[line[:partitiionAt].strip()] = line[partitiionAt:].strip()

    dataFile.close()
    return data


def inputBasicData(browser, data: dict) -> None:
    browser.find_element_by_xpath('//input[@name = "resume"]').send_keys(data['RESUME'])
    browser.find_element_by_xpath('//input[@name = "name"]').send_keys(data['FULL_NAME'])
    try:
        browser.find_element_by_xpath('//input[@name = "email"]').clear()
    except:
        pass
    browser.find_element_by_xpath('//input[@name = "email"]').send_keys(data['PHONE'])
    browser.find_element_by_xpath('//input[@name = "phone"]').send_keys(data['PHONE'])
    browser.find_element_by_xpath('//input[@name = "org"]').send_keys(data['CURRENT_COMPANY'])
    browser.find_element_by_xpath('//input[@name = "urls[LinkedIn]"]').send_keys(data['LINKEDIN_URL'])
    browser.find_element_by_xpath('//input[@name = "urls[GitHub]"]').send_keys(data['GITHUB_URL'])

    browser.find_element_by_xpath('//textarea[@name = "comments"]').send_keys(data['ADDITIONAL_INFORMATION'])


def customQuestions(browser) -> None:
    CUSTOM_QUESTIONS = []

    for x in browser.find_elements_by_xpath('//div[@class="application-label full-width textarea"]'):
        question = x.text
        question = question[0: len(question)-1].strip()
        CUSTOM_QUESTIONS.append(question)

    for index, textbox in enumerate(browser.find_elements_by_xpath('//textarea[@class="card-field-input"]')):
        answer = input(f"{CUSTOM_QUESTIONS[index]}")
        textbox.send_keys(answer)


def applicationSubmit(data, link):
    browser = webdriver.Chrome()
    try:
        browser.get(link)
    except:
        print("This may be an invalid link")
        browser.close()
        return

    inputBasicData(browser, data)
    customQuestions(browser)

    userContinue = True if input("Do you want to submit?").upper() == "Y" else "N"
    if userContinue:
        browser.find_element_by_xpath('//button[@class = "postings-btn template-btn-submit cerulean"]').click()
        browser.close()
    else:
        print("Press on the screen to take over")


def batchSubmit(data):
    linkFile = open("links.txt", "r")

    for line in linkFile:
        applicationSubmit(data, link)

    linkFile.close()


if __name__ == "__main__":
    data = processData()

    if(input("Batch Submit? Y or N: ").upper() == "Y"):
        batchSubmit(data)
    else:
        applicationSubmit(input("What is the link for the application?"), data)
