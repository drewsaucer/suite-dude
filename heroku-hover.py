# Minutes: 20m
# Navigate to http://the-internet.herokuapp.com/hovers
# Hover over each avatar
# Verify the correct names appear for each user (user1, user2, user3)
# Verify there is a View Profile link for each user

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
driver.implicitly_wait(10)

# Navigate to http://the-internet.herokuapp.com/hovers
driver.get("http://the-internet.herokuapp.com/hovers")

# Hover over each avatar
figures = driver.find_elements_by_class_name("figure")
c = 0
for figure in figures:
    c += 1
    ActionChains(driver).move_to_element(figure).perform()
# Verify the correct names appear for each user (user1, user2, user3)
    caption = figure.find_element_by_tag_name("h5").get_attribute("innerHTML")
    if caption == "name: user" + str(c):
        print "pass"
    else:
        print "FAIL: caption for figure " + str(c)
# Verify there is a View Profile link for each user
    if figure.find_element_by_link_text("View profile"):
        print "pass"
    else:
        print "FAIL: profile link for figure " + str(c)

print "\n"
driver.quit()
