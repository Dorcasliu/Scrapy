import csv
import paramaters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def validate_field(field):
    if field:
        pass
    else:
        field = ''
    return field

writer = csv.writer(open(paramaters.file_name, 'wb'))
writer.writerow(['Name', 'Job Title', 'Experience', 'Location', 'URL'])

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://www.linkedin.com")

username=driver.find_element_by_id("session_key")
username.send_keys(paramaters.linkedin_username)
sleep(0.5)

password=driver.find_element_by_id("session_password")
password.send_keys(paramaters.linkedin_password)
sleep(0.5)

sign_in_button=driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(5)

driver.get("https://www.google.com")
sleep(3)

search_query=driver.find_element_by_name("q")
search_query.send_keys(paramaters.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls=driver.find_elements_by_tag_name('cite')

linkedin_urls=[url.text for url in linkedin_urls]
sleep(0.5)

for linkedin_url in linkedin_urls:
    driver.get(linkedin_url)
    sleep(5)

    sel=Selector(text=driver.page_source)
    name=sel.xpath('//*[starts-with(@class,"inline t-24 t-black t-normal break-words")]/text()').extract_first().strip()
    job_title=sel.xpath('//*[starts-with(@class,"mt1 t-18 t-black t-normal break-words")]/text()').extract_first().strip()
    experience=sel.xpath('//*[starts-with(@class,"text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first().strip()
    location=sel.xpath('//*[starts-with(@class,"t-16 t-black t-normal inline-block")]/text()').extract_first()

    linkedin_url=driver.current_url

    name = validate_field(name)
    job_title = validate_field(job_title)
    experience = validate_field(experience)
    location = validate_field(location)
    linkedin_url = validate_field(linkedin_url)


    writer.writerow([name.encode('utf-8'),
                     job_title.encode('utf-8'),
                     experience.encode('utf-8'),
                     location.encode('utf-8'),
                     linkedin_url.encode('utf-8')])


driver.quit()

