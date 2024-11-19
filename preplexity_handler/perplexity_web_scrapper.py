from datetime import datetime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from model import User
import time

from utils.json_responses import JsonResponse


class PerplexityHandler:

    @classmethod
    def scrape_amazon_webpage(self, query, user: User):
        try:

            webDriver = user.webDriverHandler

            webDriver.get_screenshot_as_file('perplexity.png')
            # dismiss_dialog_if_open(driver)
            # Modify URL as needed
            webDriver.find_element(By.CLASS_NAME, "overflow-auto").send_keys(query)
            webDriver.get_screenshot_as_file('perplexity1.png')
            # dismiss_dialog_if_open(driver)
            time.sleep(2)
            webDriver.get_screenshot_as_file('perplexity33.png')
            isVisible = checkButtonIsVisibleOrNot(webDriver, "p2")
            if isVisible:
                submit_button = webDriver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit']")
                submit_button.click()
                webDriver.get_screenshot_as_file("p4.png")
            else:
                time.sleep(12)
                isVisible = checkButtonIsVisibleOrNot(webDriver, "p3")
                submit_button = webDriver.find_element(By.CLASS_NAME, "bg-super")
                submit_button.click()
                webDriver.get_screenshot_as_file("p5.png")
            time.sleep(7)
            webDriver.get_screenshot_as_file('perplexity6.png')
            divs = webDriver.find_elements(By.XPATH, "//div[contains(@class, 'prose')]")
            responseList = list()
            for div in divs:
                responseList.append(div.text)

            return JsonResponse.getSuccessResponse(responseList, "Received response", 1, 200)

        except Exception as e:
            with open("PreplexException.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: Exception in scrape_amazon_webpage(): \n{e}")
                #webDriver.get_screenshot_as_file("p4.png")
            return JsonResponse.getSuccessResponse("Error Model not Working", "try later", 2, 401)


def checkButtonIsVisibleOrNot(driver, imageName):
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit']")
    if submit_button.is_displayed() and submit_button.is_enabled():
        #submit_button.click()
        driver.get_screenshot_as_file(imageName + ".png")
        return True
        # dismiss_dialog_if_open(driver)
    # submit_button.click()
    # driver.get_screenshot_as_file('perplexity4.png')
    else:
        print("Button is either not visible or not enabled.")
        return False
