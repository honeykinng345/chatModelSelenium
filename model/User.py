from selenium.webdriver.chrome.webdriver import WebDriver


class User:
    webDriverHandler: WebDriver

    def __init__(self, uid, proxyIP, webDev):
        self.userId = uid
        self.proxyIP = proxyIP
        self.webDriverHandler = webDev
