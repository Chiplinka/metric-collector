import argparse
import threading
from datetime import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import argparse
import requests
import psutil
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, ChromeService, Remote
from selenium.webdriver.common.by import By

# common imports
from scripts_common.system_monitor import send_system_usage, print_system_usage, init_thread_send_system_usage
from scripts_common.argparser import parse_arguments
from scripts_common.sel_broser_setup import setup_browser

def open_tab_admin(driver, url):
    driver.get(url)

    # button = driver.find_element(By.CLASS_NAME, "btn btn-primary")
    # button.click()

    submit_button = driver.find_elements(By.TAG_NAME, "button")[0]
    submit_button.click()

def open_tab_participant(driver, url):
    driver.get(url)

    # button = driver.find_element(By.CLASS_NAME, "btn btn-primary")
    # button.click()

    submit_button = driver.find_elements(By.TAG_NAME, "button")[0]
    submit_button.click()

def main():
    print_system_usage()
    args = parse_arguments()

    driver = setup_browser(args.url, args.headless)
    driver.implicitly_wait(5)


    # init thread 
    start_time = time.time()
    init_thread_send_system_usage(args.url_statistics, args.client_id, args.interval, start_time)



    if args.host:
        open_tab_admin(driver, args.url)
    else:
        open_tab_participant(driver, args.url)

    # for testing purpose 
    while True:
        time.sleep(10)    

    driver.quit()

if __name__ == "__main__":
    main()
