from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

#fetches the webdriver and opens the page in the driver
driver = webdriver.Chrome(executable_path=r"C:/Users/Christopher/Downloads/Software/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('https://mymasonportal.gmu.edu/webapps/login/?action=relogin')

login = driver.find_element_by_xpath("//button[@class='masonbutton masonbutton2']")
login.click()

netID = driver.find_element_by_xpath("//input[@id='username']")
netID.clear()
netID.send_keys('criley10')
password = driver.find_element_by_xpath("//input[@id='password']")
password.clear()
password.send_keys('GammaTauFall18')

masonLogin = driver.find_element_by_xpath("//button[@class='form-element form-button']")
masonLogin.click()
accept = driver.find_element_by_xpath("//input[@value='Accept']")
accept.click()

driver.get('https://mymasonportal.gmu.edu/webapps/QW-qwickly-BB5a30bcf95ea52/newAttendance/qwicklyTakeAttendance.jsp?course_id=_338830_1')

container = driver.find_element_by_xpath("//div[@id='qwicklyAttendanceContainer']")
file = open('C:/Users/Christopher/Documents/python/scrapper/qwickly/div.txt', 'w')
file.write(str(container.get_attribute('innerHTML')))
file.close()

driver.close()


