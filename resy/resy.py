from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import psutil

"""
Chris Riley - 9/5/18

Python and Selenium to crawl the resy.com page for The Dabney in DC
-currently works for dates across one contained month. have not tested for multiple calendars.
-used to book on the date of the newest reservations available 

"""

print(psutil.cpu_percent(interval=None))

#fetches the webdriver and opens the page in the driver
driver = webdriver.Chrome(executable_path=r"C:/Users/Christopher/Downloads/Software/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('https://resy.com/cities/dc/the-dabney')

#starts manipulating page

#finds the button to open the calendar to view all dates, scrolls to view all dates
todayBtn = driver.find_element_by_xpath("//resy-button[@class='ResyButtonGroup__option ResyButtonGroup__option--date']")
todayBtn.click()
driver.execute_script("window.scrollTo(0, 400)")

#finds available calendars and prints the heading for each shown
calendars = driver.find_elements_by_xpath("//resy-calendar[@calendar='vm.calendar']")
for n in range(0, len(calendars)):
	if calendars[n].find_element_by_tag_name('h1').text != '':
		print(calendars[n].find_element_by_tag_name('h1').text)

#finds all dates that are available for reservation and clicks the newest date posted
dates = driver.find_elements_by_xpath("//div[@class='date available']")
print(dates[-1].text)
dates[-1].click()

#finds the times and prints them with indexes for selection of time then clicks selection
times = driver.find_elements_by_xpath("//div[@class='time']")
timeBtns = driver.find_elements_by_xpath("//resy-reservation-button")
driver.execute_script("window.scrollTo(0, 700)")
for n in range(0, len(times)):
	if times[n].text == sys.argv[1]:
		print('Selection found')
		selection = n
		break
print("Clicking " + str(sys.argv[1]))
timeBtns[selection].click()

#switches to the new iframe as it appears and clicks the reserve button
driver.switch_to_frame(0)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='price-string']")))
reserve = driver.find_element_by_xpath("//a[@class='button primary']")
print('Clicking reserve')
reserve.click()

#finds email and pass input elements, clears and sends info, clicks the login button
emailElement = driver.find_element_by_xpath("//input[@type='email']")
passElement = driver.find_element_by_xpath("//input[@type='password']") 
emailElement.clear()
emailElement.send_keys('chrisrex2041@gmail.com')
passElement.clear()
passElement.send_keys('Pass')
loginBtn = driver.find_element_by_xpath("//button[@class='primary']")
loginBtn.click()

#closes the webdriver
driver.close()
print(psutil.cpu_percent(interval=None))