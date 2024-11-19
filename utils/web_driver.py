import json
import os
import random
import time
import traceback
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Proxy, DesiredCapabilities, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from seleniumwire import webdriver as seleniumWire
import seleniumwire.undetected_chromedriver as uc
from selenium_stealth import stealth

from utils.extension import proxies
from utils.json_responses import JsonResponse


class WebDriverHandler:
    user_drivers = {}
    proxyIp: int
    proxyPort: int

    def __init__(self, ip, port):
        self.proxyIp = ip
        self.proxyPort = port

    @classmethod
    def initialize_chrome_driver(cls, appId, proxyIp, proxyPort, protocals):
        try:
            # extension_path = cls.update_extension_config(proxyIp, proxyPort,protocals)
            hub_url = "http://172.20.10.3:4444/wd/hub"
            PROXY = "http://148.251.5.30:823:6e4162a6906dc79e20fa:33e81c17912ec20d"
            ## Disable loading images for faster crawling
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_chrome_drive")

            options = webdriver.ChromeOptions()
            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)

            # options.browser_version = "127"
            #
            # options.platform_name = "Windows 10"
            #options.add_argument("--headless")
            options.add_argument("--enable-features=WebContentsForceDark")
            options.add_argument('--force-dark-mode')
            options.add_argument("--disable-gpu")
            options.add_argument(f'--user-agent={user_agent}')
            options.add_argument("--no-sandbox")
            options.add_argument("--window-size=1920x1080")
            options.add_argument("start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--disable-web-security")
            options.add_argument("--disable-blink-features=AutomationControlled")

            proxies_extension = proxies("6e4162a6906dc79e20fa", "33e81c17912ec20d", "gw.dataimpulse.com", "823")

            options.add_extension(proxies_extension)
            options.add_argument("--headless=new")

            # Disable WebRTC
            options.add_argument("--disable-features=WebRTC")

            # Set up Firefox options

            #options.add_argument(f'--proxy-server={PROXY}')


            seleniumwire_options = {
                'proxy': {
                    'https': 'socks5://6e4162a6906dc79e20fa:33e81c17912ec20d@gw.dataimpulse.com:824',
                }
            }
            # Set the desired capabilities to Chrome
            # Set the desired capabilities to Chrome
            # capabilities = DesiredCapabilities.CHROME.copy()
            #
            # # Merge Chrome options into desired capabilities manually
            # for option in options.arguments:
            #     capabilities['goog:chromeOptions'] = capabilities.get('goog:chromeOptions', {})
            #     capabilities['goog:chromeOptions']['args'] = capabilities['goog:chromeOptions'].get('args', [])
            #     capabilities['goog:chromeOptions']['args'].append(option)
            # Merge capabilities with options
            driver = webdriver.Remote(command_executor=hub_url,
                                      options=options)
            driver.delete_all_cookies()

            # # Assign a unique user data directory to avoid conflicts
            # user_data_dir = os.path.join(tempfile.gettempdir(), f"chrome_user_data_{appId}")
            # options.add_argument(f"--user-data-dir={user_data_dir}")
            # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            # # Store the driver in the dictionary with the user_id as the key
            cls.random_sleep()
            driver.get("https://www.perplexity.ai/")

            # Wait for the popup to appear (adjust the sleep time as necessary)
            # time.sleep(2)
            #
            # # Handle the authentication popup by sending the username and password
            # alert = driver.switch_to.alert
            # alert.send_keys("6e4162a6906dc79e20fa" + Keys.TAB + "33e81c17912ec20d")
            # alert.accept()

            return driver
        except Exception as e:
            # Log exception details to ScreenFlow.txt
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_chrome_driver Exception\n")
                # Log the full traceback for detailed debugging
                traceback_str = traceback.format_exc()
                f.write(f"{current_datetime}: {traceback_str}\n")

            # Log exception details to WebDriverException.txt
            with open("WebDriverException.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: Exception in webDriver: {str(e)}\n")
                # Log the full traceback for detailed debugging
                f.write(f"{current_datetime}: {traceback_str}\n")

            # Raise a new exception with a custom error message
            raise Exception(JsonResponse.getErrorResponse("Something went wrong", 500))




    @classmethod
    def random_sleep(cls):
        time.sleep(random.uniform(2, 5))
