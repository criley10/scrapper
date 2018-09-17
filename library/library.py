from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import datetime
from datetime import timedelta

def oneWeek():
	today = datetime.date.today()
	d = timedelta(weeks=1)
	oneWeek = today + d
	return oneWeek.day

timeSlots = ['6:30pm', '6:00pm', '5:30pm', '5:00pm', '4:30pm', '4:00pm', '3:30pm', '3:00pm']
#fetches the webdriver and opens the page in the driver
driver = webdriver.Chrome(executable_path=r"C:/Users/Christopher/Downloads/Software/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('https://gmu.libcal.com/spaces?lid=1205&gid=2118')
driver.execute_script("window.scrollTo(0, 400)")
dateBtn = driver.find_element_by_xpath("//button[@class='fc-goToDate-button btn btn-default']")
dateBtn.click()

dates = driver.find_elements_by_xpath("//td[@class='day']")
nextWeek = oneWeek()
for n in dates:
	if n.text == str(nextWeek):
		date = n
date.click()
boxes = driver.find_elements_by_xpath("//a[@class='fc-timeline-event fc-h-event fc-event fc-start fc-end s-lc-eq-avail']")
room = [x for x in boxes if '4701' in x.get_attribute('title')]
times = [x for x in room for y in timeSlots if y in x.get_attribute('title')]
for n in times:
	n.click()
	driver.implicitly_wait(10)

