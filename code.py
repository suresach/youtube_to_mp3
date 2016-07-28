from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
code_box = urlopen('https://www.youtube.com/results?search_query=divya+kathayein+hanuman').read()
soup = BeautifulSoup(code_box, 'html.parser')
lins = soup.find_all('a', href=True)
for links in lins:
        if '/watch?v=' in links['href'] and 'Hanuman Kathayein' in links.get_text() and 'Private Video' not in links.get_text():
                print("Initiated for : " + links.get_text())
                link_to_download = "http://www.youtube.com" + links['href']
                print(link_to_download)
                browser.get('http://mp3fiber.com/index.php')
                reciever_input = browser.find_elements_by_class_name('inputbg')
                reciever_input[0].send_keys(link_to_download)
                browser.find_element_by_class_name('submit').click()
                time.sleep(90)
                browser.find_element_by_link_text("Download Now!").click()
                print("Downloading started for : " + links.get_text())
print("Downloading Complete")
