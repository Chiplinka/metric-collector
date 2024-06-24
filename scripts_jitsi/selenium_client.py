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

ROOM_NAME = "room1"

def open_tab_admin(driver, url):
    driver.get(url)

    # start window
    input_room_name = driver.find_element(By.ID, "enter_room_field")
    enter_room_button = driver.find_element(By.ID, "enter_room_button")
    input_room_name.clear()
    input_room_name.send_keys(ROOM_NAME)
    # sleep(5)
    enter_room_button.click()

    # first user config
    input_user_name = driver.find_element(By.ID, "premeeting-name-input")
    input_user_name.clear()
    input_user_name.send_keys("user1")
    driver.find_element(By.XPATH, "//div[text()='Join meeting']").click()

def open_tab_participant(driver, url, tab_id):
    url = url + '/'+ ROOM_NAME
    driver.get(url)

    #  user config
    input_user_name = driver.find_element(By.ID, "premeeting-name-input")
    input_user_name.clear()
    input_user_name.send_keys("user_it_" + str(tab_id))
    driver.find_element(By.XPATH, "//div[text()='Join meeting']").click()

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
        open_tab_participant(driver, args.url, args.tab_id)

    # for testing purpose 
    while True:
        time.sleep(10)

    driver.quit()

if __name__ == "__main__":
    main()
