from selenium import webdriver
import time


##### MODIFY courseNums, termText, username, and password BEFORE RUNNING!

courseNums = '21002,20979,20981,25174,20314' # string of course registration numbers without spaces
termText = 'Spring 2019' # string of the official term name
username = "user" # student username
password = "pass" #student password

####### DON'T EDIT ANYTHING BELOW

loginLink = 'https://bannerss.wellesley.edu:4453/dbprod/twbkwbis.P_WWWLogin'
termUrl = 'https://bannerss.wellesley.edu:4453/dbprod/bwskfreg.P_AltPin'

courseNums = courseNums.split(',')

d = webdriver.Chrome()
d.get(loginLink)

d.find_element_by_id("UserID").send_keys(username)
d.find_element_by_name("PIN").send_keys(password) 
d.find_element_by_xpath("/html/body/div[3]/form/p/input").click()

d.get(termUrl)

d.find_element_by_name("term_in").send_keys(termText)

input('Click any button to proceed\n')

d.find_element_by_xpath("/html/body/div[3]/form/input").click()


for i in range(1,len(courseNums) + 1):
	id = "crn_id{}".format(str(i))
	print(courseNums[i-1])
	d.find_element_by_id(id).send_keys(courseNums[i-1])


d.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()
time.sleep(999999)
d.close()
