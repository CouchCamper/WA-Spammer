from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://web.whatsapp.com/")

target = "Fabi"
message = "oha :("
amount = 50

time.sleep(5)

qr = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/canvas")

while True:
    try:
        qr.is_displayed()
        print("waiting...")
        time.sleep(3)
    except:
        print("linking successful...")
        break

time.sleep(4)
print("starting spam...")

driver.find_element_by_xpath("//span[text()='" + target + "']").click()
time.sleep(4)
actions = ActionChains(driver)
i = 0
while i < amount:
    actions.send_keys(message)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    i += 1
    time.sleep(0.3)

print("Spam complete")
print(str(i) + " messages were sent")