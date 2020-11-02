## Open browser automatically, login to the linkedin, then from google search for the specific type of profiles
$ sudo pip install selenium\
$ ipython

### Open google chrome:
from selenium import webdriver\
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

### Open linkedin:
driver.get("https://www.linkedin.com")

### Input username:
username=driver.find_element_by_id("session_key")\
username.send_keys("foo@gmail.com")

### Input password:
password=driver.find_element_by_id("session_password")\
password.send_keys("password")

### Click login button:
sign_in_button=driver.find_element_by_xpath('//*[@type="submit"]')\
sign_in_button.click()

### Open the google page:
driver.get("https://www.google.com")

### Input the search requirements:
search_query=driver.find_element_by_name("q")\
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')

### Hit enter to return:
search_query.send_keys(Keys.RETURN)

### get the searching results’ url:
linkedin_urls=driver.find_element_by_tag_name('cite')\ 
len(linkedin_urls)

### The address of the first result:
linkedin_urls[0].text

### Loop to get all results:
linkedin_urls=[url.text for url in linkedin_urls]\
linkedin_urls

### remove the \n
.strip()

### Run method:
cd /../ \
python linkedin.py

### Get current url:
driver.current_url 
