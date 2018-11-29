from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

grades = open(r'C:/Users/Christopher/Documents/python/scrapper/grades/grades.txt', 'r')
gradeList = grades.readlines()

driver = webdriver.Chrome(executable_path=r"C:/Program Files/Python36/Scripts/chromedriver.exe")
print('Created Driver')

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get('https://blackboard.gmu.edu')
driver.find_element_by_xpath("//a[contains(@href, 'https://mymasonportal.gmu.edu/auth-saml/saml/login?apId=_134_1&redirectUrl=https%3A%2F%2Fmymasonportal.gmu.edu%2Fwebapps%2Fportal%2Fexecute%2FdefaultTab')]").click()
netID = driver.find_element_by_xpath("//input[@id='username']")
netID.send_keys('criley10')
passwrd = driver.find_element_by_xpath("//input[@id='password']")
passwrd.send_keys('GammaTauFall18')
loginBtn = driver.find_element_by_xpath("//button[@type='submit']").click()
accept = driver.find_element_by_xpath("//input[@value='Accept']").click()
driver.get("https://mymasonportal.gmu.edu/webapps/streamViewer/streamViewer?cmd=view&streamName=mygrades_d")
active = driver.find_element_by_xpath("//div[@class='stream_item active_stream_item']")
streamList = driver.find_elements_by_xpath("//div[@class='stream_item']")

grades = open(r'C:/Users/Christopher/Documents/python/scrapper/grades/grades.txt', 'w')
for n in streamlist:
	x = n.text.split('\n')
	if x[1].split('')[1] = 'month':
		break
	grades.write('{0}, {1}, {2},')


sel.run_script("$('#right_stream_mygrades_d').contents().find('td.gradeCellGrade')")
#streamDetailMainBodyRight > div > div:nth-child(2) > table > tbody > tr > td.gradeCellGrade