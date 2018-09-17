from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"C:/Users/Christopher/Downloads/Software/chromedriver_wexe",  chrome_options=chrome_options)
driver.get_screenshot_as_file("capture.png")