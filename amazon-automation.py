from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr

path = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.amazon.in")

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Product name you want search: ")
    audio = r.listen(source)
    try:
        product = r.recognize_google(audio)
    except:
        print("Sorry! can't hear anything")

amazon_search = driver.find_element_by_id("twotabsearchtextbox")
amazon_search.send_keys(product)
amazon_search.send_keys(Keys.RETURN)

try:
    amazon_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//span[@class ='a-size-medium a-color-base a-text-normal']"))
    )
    amazon_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class ='a-price-whole']"))
    )

finally:
    print(f"{amazon_title.text} | Price: {amazon_price.text}/-")
    driver.quit()


