from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.implicitly_wait(30)

#OPENING TEXT FILE 
with open("file.txt","r") as file:
    for num in file:
       print(num)
       
       driver.get("https://www.truecaller.com/")
       print("No for which search is going on is : ",num)
       driver.find_element_by_xpath("""//*[@id="app"]/nav/div/form/input""").send_keys(num)
       name=driver.find_element_by_xpath("""//*[@id="app"]/main/div/div[1]/div[1]/header/div[2]/h1""").text

       #writing text
       with open("file.txt","a") as file:
       	file.write("\nOwner Detail : {}{}".format(num,name))
       	print("Appedned sucessfully.....")



	    