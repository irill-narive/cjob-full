FULL_LIST = ["s0","s2","s3","s4","s5","s6"]

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller,time
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
   # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    # These flags BELOW are recommended for stability when running Chrome in headless or containerized environments (such as GitHub Actions).
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]
for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)
for x in FULL_LIST:
    driver.get(f'http://bplan{x}.onrender.com/kaffeine_port')
    time.sleep(2)
print(driver.title)
