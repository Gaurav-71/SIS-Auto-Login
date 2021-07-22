from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER_PATH = './chromedriver'

sis_url = "http://parents.msrit.edu/index.php"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

driver.get(sis_url)

usn = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div/input')
day = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/form/div[2]/div/div/select[1]')
month = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/form/div[2]/div/div/select[2]')
year = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/form/div[2]/div/div/select[3]')
login = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div/form/div[3]/input[1]')

#  Enter your info

usn[0].send_keys("1MS18CS046")
day[0].send_keys("28")
month[0].send_keys("Mar")
year[0].send_keys("2000")

login[0].submit()

driver.get('http://parents.msrit.edu/index.php?option=com_studentdashboard&controller=studentdashboard&task=dashboard')

