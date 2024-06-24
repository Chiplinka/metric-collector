from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, ChromeService, Remote


def setup_browser(url, headless):
    """Sets up and returns a WebDriver object for Chrome with specified options."""
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument(f'unsafely-treat-insecure-origin-as-secure={url}')
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if headless:
        chrome_options.add_argument("--headless=new")

   # Use ChromeDriverManager to handle driver setup
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver