import os
import shutil
import logging
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def screenshot(driver,loop):
    try:
        screenshot_dir = "/screenshots"
        namefile = f"screenshot_{loop}.png"
        screenshot_path = os.path.join(screenshot_dir, namefile)
        os.makedirs(screenshot_dir, exist_ok=True)
        driver.save_screenshot(screenshot_path)
        logging.info(namefile)
    except Exception as e:
        traceback.print_exc()
        logging.error(str(e), exc_info=True)

def get_site(driver):
    try:
        driver.get('http://www.google.com')
    except Exception as e:
        traceback.print_exc()
        logging.error(str(e), exc_info=True)

def create_driver():
    try:

        options = Options()
        profile = FirefoxProfile()
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        geckodriver_path = shutil.which("geckodriver")
        profile.update_preferences()
        if not geckodriver_path:
            raise Exception("geckodriver no encontrado en el sistema")
        service = Service(geckodriver_path)
        driver = webdriver.Firefox(service=service,options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    
    except Exception as e:
        traceback.print_exc()
        logging.error(str(e), exc_info=True)


