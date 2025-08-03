import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

zillo_url = "https://appbrewery.github.io/Zillow-Clone/"
zillow_html = requests.get(zillo_url, headers=header)

soup = BeautifulSoup(zillow_html.text , "html.parser")

all_property_addresses_raw = soup.select(selector=".ListItem-c11n-8-84-3-StyledListCardWrapper address")
all_property_prices_raw = soup.select(selector=".ListItem-c11n-8-84-3-StyledListCardWrapper .PropertyCardWrapper__StyledPriceLine")
all_property_links_raw = soup.select(selector=".ListItem-c11n-8-84-3-StyledListCardWrapper .StyledPropertyCardPhotoBody a")


all_property_addresses = [property_address.text.strip() for property_address in all_property_addresses_raw]
all_property_prices = [property_price.text[0:6] for property_price in all_property_prices_raw]
all_property_links = [property_link.get("href") for property_link in all_property_links_raw]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeTGyRnhuLYNWMFevsHsY9tpdbuJLUK0_nKc-se_crERPIeig/viewform?usp=header"

driver.get(google_form_url)
for i in range(len(all_property_prices)):
    curr_property_address  = all_property_addresses[i]
    curr_property_price = all_property_prices[i]
    curr_property_link = all_property_links[i]

    time.sleep(1)

    ques_one = driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques_two = driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques_three = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    ques_one.send_keys(curr_property_address)
    ques_two.send_keys(curr_property_price)
    ques_three.send_keys(curr_property_link)
    submit_button.click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

driver.quit()








