from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Checkout bot 
# Samuel Nummela ©
# https://github.com/Saow


selainhaku = input("Mikä selain haluat käyttää? (Chrome, Firefox, Edge): ")

if selainhaku == "Chrome":
    driver = webdriver.Chrome()
    driver.get("https://www.nike.com/fi/t/air-jordan-1-mid-shoes-K7N7lM/DQ8426-615")
    ## accept all cookies button
    time.sleep(10)
    driver.find_element("id", "hf_cookie_text_cookieAccept").click()
    ## selecte size Eu 45 (US 11) 
    time.sleep(5)
    driver.find_element("id", "skuAndSize__28644640").click()
    ## add to bag button
    time.sleep(5)
    driver.find_element("class", "ncss-btn-primary-dark btn-lg add-to-cart-btn").click()



elif selainhaku == "Firefox":
    driver = webdriver.Firefox()
    driver.get("https://www.nike.com/fi/t/air-jordan-1-mid-shoes-K7N7lM/DQ8426-615")
    ## accept all cookies button
    time.sleep(10)
    driver.find_element("id", "hf_cookie_text_cookieAccept").click()
    ## selecte size Eu 45 (US 11) 
    time.sleep(5)
    driver.find_element("id", "skuAndSize__28644640").click()
    ## add to bag button
    time.sleep(5)
    driver.find_element("class", "ncss-btn-primary-dark btn-lg add-to-cart-btn").click()

elif selainhaku == "Edge":
    driver = webdriver.Edge()
    driver.get("https://www.nike.com/fi/t/air-jordan-1-mid-shoes-K7N7lM/DQ8426-615")
    ## accept all cookies button
    time.sleep(10)
    driver.find_element("id", "hf_cookie_text_cookieAccept").click()
    ## selecte size Eu 45 (US 11) 
    time.sleep(5)
    driver.find_element("id", "skuAndSize__28644640").click()
    ## add to bag button
    time.sleep(5)
    driver.find_element("class", "ncss-btn-primary-dark btn-lg add-to-cart-btn").click()











## Koitetaan uudelleen typon takia
else:
    print(f"Valitse jokin muu selain tai kirjoita oikein jos kirjoitit väärin. Tässä mitä kirjoitit : {selainhaku}")
    time.sleep(1)
    selainhaku = input("Mikä selain haluat käyttää? (Chrome, Firefox, Edge): ")

if selainhaku == "Chrome":
    driver = webdriver.Chrome()
    driver.get("https://www.nike.com/fi/t/air-jordan-1-mid-shoes-K7N7lM/DQ8426-615")
    ## accept all cookies button
    time.sleep(10)
    driver.find_element("id", "hf_cookie_text_cookieAccept").click()
    ## selecte size Eu 45 (US 11) 
    time.sleep(5)
    driver.find_element("id", "skuAndSize__28644640").click()
    ## add to bag button
    time.sleep(5)
    driver.find_element("class", "ncss-btn-primary-dark btn-lg add-to-cart-btn").click()



elif selainhaku == "Firefox":
    driver = webdriver.Firefox()
    driver.get("https://www.nike.com/fi/t/air-jordan-1-mid-shoes-K7N7lM/DQ8426-615")
    ## accept all cookies button
    time.sleep(10)
    driver.find_element("id", "hf_cookie_text_cookieAccept").click()
    ## selecte size Eu 45 (US 11) 
    time.sleep(5)
    driver.find_element("id", "skuAndSize__28644640").click()
    ## add to bag button
    time.sleep(5)
    driver.find_element("class", "ncss-btn-primary-dark btn-lg add-to-cart-btn").click()

elif selainhaku == "Edge":
    driver = webdriver.Edge()
    driver.get("https://www.nike.com/fi/t/air-jordan-1-mid-shoes-K7N7lM/DQ8426-615")
    ## accept all cookies button
    time.sleep(10)
    driver.find_element("id", "hf_cookie_text_cookieAccept").click()
    ## selecte size Eu 45 (US 11) 
    time.sleep(5)
    driver.find_element("id", "skuAndSize__28644640").click()
    ## add to bag button
    time.sleep(5)
    driver.find_element("class", "ncss-btn-primary-dark btn-lg add-to-cart-btn").click()