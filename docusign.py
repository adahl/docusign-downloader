import os
import csv

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variables

downloads_dir = os.getcwd() + "/downloads"

login_url = "https://account.docusign.com"
envelope_url = "https://app.docusign.com/documents/details/"

envelopes_csv = "Envelope Report.csv"

# Browser setup

Path(downloads_dir).mkdir(parents=True, exist_ok=True)

options = Options()
options.add_argument("--headless=new")
options.add_experimental_option("prefs", {
    "download.default_directory": downloads_dir
})
driver = webdriver.Chrome(options=options)

# Log into DocuSign

driver.get(login_url)

email = input("Enter email: ")
element = driver.find_element(By.NAME, "email")
element.send_keys(email)
element.send_keys(Keys.RETURN)

password = input("Enter password: ")
element = driver.find_element(By.NAME, "password")
element.send_keys(password)
element.send_keys(Keys.RETURN)

security_code = input("Enter verification code (from email): ")
element = driver.find_element(By.NAME, "security_code")
element.send_keys(security_code)
element.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@data-qa='header-profile-menu-button']"))
)

# Download envelopes

with open(envelopes_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip the heading
    
    for row in reader:
        envelope_id = row[0]
        print("Downloading: " + envelope_id)

        driver.get(envelope_url + envelope_id)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='document-download-button']"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='download-separate']"))
        )
        element.click()

# Done

input("We are done. Close it down...")

driver.quit()
