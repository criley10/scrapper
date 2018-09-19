from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
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

def find(driver, el):
    element = el
    if element:
        return element
    else:
        return False

#defining global variables
timeout = 10
timeSlots = ['6:30pm', '6:00pm', '5:30pm', '5:00pm', '4:30pm', '4:00pm', '3:30pm', '3:00pm']
nextWeek = oneWeek()

#fetches the webdriver and opens the page in the driver, scrolls and clicks button to open calendar
#driver = webdriver.Chrome(executable_path=r"C:/Program Files/Python36/Scripts/chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"C:/Users/Christopher/AppData/Local/Programs/Python/Python36-32/Scripts/chromedriver.exe")

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('https://gmu.libcal.com/spaces?lid=1205&gid=2118')
driver.execute_script("window.scrollTo(0, 400)")
dateBtn = driver.find_element_by_xpath("//button[@class='fc-goToDate-button btn btn-default']").click()

#finds the day one week from today
dates = driver.find_elements_by_xpath("//td[@class='day']")
for n in dates:
	if n.text == str(nextWeek):
		date = n
date.click()



#clicks the time boxes in order
for n in range(0, len(timeSlots)):
	if 'avail' in driver.find_element_by_xpath("//a[contains(@title, '4603') and contains(@title, '"+timeSlots[n]+"')]").get_attribute('class'):
		if n == 0 :
			time = driver.find_element_by_xpath("//a[contains(@title, '4603') and contains(@title, '"+timeSlots[n]+"')]").click()
			select = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@id, 'bookingend_"+str(n+1)+"')]")))
			continue
		else:
			try:
				print(timeSlots[n])
				time = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@title, '4603') and contains(@title, '"+timeSlots[n]+"')]")))
				time.click()
			finally:
				select = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@id, 'bookingend_"+str(n+1)+"')]")))

#submit and continue buttons
submitBtn = driver.find_element_by_xpath("//button[@id='submit_times']").click()
continueBtn = driver.find_element_by_xpath("//button[@id='terms_accept']").click()

#input areas and sending keys, clicking submit
fName = driver.find_element_by_xpath("//input[@id='fname']") 
fName.clear()
fName.send_keys('Chris')
lName = driver.find_element_by_xpath("//input[@id='lname']") 
lName.clear()
lName.send_keys('Riley')
email = driver.find_element_by_xpath("//input[@id='email']")
email.clear()
email.send_keys('criley10@gmu.edu')
subBookingBtn = driver.find_element_by_xpath("//button[@id='btn-form-submit']").click()

driver.get("https://www.office.com/")
signInBtn = driver.find_element_by_xpath("//a[@id='hero-banner-sign-in-to-office-365-link']").click()
emailOutlook = driver.find_element_by_xpath("//input[@id='i0116']")
emailOutlook.clear()
emailOutlook.send_keys('criley10@masonlive.gmu.edu')
subEmail = driver.find_element_by_xpath("//input[@type='submit']").click()
passOutlook = driver.find_element_by_xpath("//input[@id='i0118']")
passOutlook.clear()
passOutlook.send_keys('Crex204!')
signedInBtn = driver.find_element_by_xpath("//input[@id='idBtn_Back']").click()
timeBtn = driver.find_element_by_xpath("//select[@name='tzid']/option[@value='Eastern Standard Time']").click()
saveBtn = driver.find_element_by_xpath("//div[@role='button']").click()