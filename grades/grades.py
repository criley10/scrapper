from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def writeGrades(gradeEls):
	grades = open(r'C:/Users/Christopher/Documents/python/scrapper/grades/grades.txt', 'a')
	retList = []
	for n in range(len(gradeEls)-1,-1,-1):
		actions.move_to_element(gradeEls[n]).perform()
		gradeEls[n].click()
		x = gradeEls[n].text.split('\n')
		driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
		grade = driver.find_element_by_xpath('//td[@class="gradeCellGrade"]').text
		grades.write('{0}, {1}, {2}\n'.format(x[3].split(' ')[2],x[2],grade))
		driver.switch_to.default_content()
		retList.append([x[3].split(' ')[2], x[2], grade, x[1]])
	grades.close()
	return retList

# Creating driver and setting arguments
driver = webdriver.Chrome(executable_path=r"C:/Program Files/Python36/Scripts/chromedriver.exe")
print('Created Driver')
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# Get Blackboard and click login
driver.get('https://blackboard.gmu.edu')
driver.find_element_by_xpath("//a[contains(@href, 'https://mymasonportal.gmu.edu/auth-saml/saml/login?apId=_134_1&redirectUrl=https%3A%2F%2Fmymasonportal.gmu.edu%2Fwebapps%2Fportal%2Fexecute%2FdefaultTab')]").click()

# Login page
netID = driver.find_element_by_xpath("//input[@id='username']")
netID.send_keys('criley10')
passwrd = driver.find_element_by_xpath("//input[@id='password']")
passwrd.send_keys('GammaTauFall18')
loginBtn = driver.find_element_by_xpath("//button[@type='submit']").click()
accept = driver.find_element_by_xpath("//input[@value='Accept']").click()

# Get grades page buy URL, store stream of grades in streamList
driver.get("https://mymasonportal.gmu.edu/webapps/streamViewer/streamViewer?cmd=view&streamName=mygrades_d")
active = driver.find_element_by_xpath("//div[@class='stream_item active_stream_item']")
streamList = driver.find_elements_by_xpath("//div[@class='stream_item']")

# Load grades.txt
grades = open(r'C:/Users/Christopher/Documents/python/scrapper/grades/grades.txt', 'r')
gradesList = grades.readlines()
grades.close()
gradesList = [n.strip().split(',') for n in gradesList]
if active.text.split('\n')[2].split(',')[0] != gradesList[-1][1].strip():
	if streamList[1].text.split('\n')[2].split(',')[0] != gradesList[-1][1].strip():
		start = 0
		for n in range(1,20):
			grade = streamList[n]
			actions.move_to_element(grade).perform()
			print(n, grade.text)
			if grade.text.split('\n')[2].split(',')[0] == gradesList[-1][1].strip():
				start = n-1
				break
		print("{} grades added since last run".format(start+2))
		returned = writeGrades(streamList[0:start+1])
		for n in returned:
			print(n[1])
		x = writeGrades([active])
		print(x[1])
	else:
		print("2 grades added since last run")
		returned = writeGrades([streamList[0], active])
		for n in returned:
			print(n[1])
else:
	print("1 grade added since last run")
	x = writeGrades([active])
	print(x[0][1])

# Close the driver
driver.close()



