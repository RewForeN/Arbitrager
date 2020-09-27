from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")

## Search for facebook
driver.find_element_by_name("q").send_keys("facebook" + Keys.RETURN)

## Find first search result
text = driver.find_element_by_id("search").find_element_by_tag_name("div").find_element_by_tag_name("div")\
	.find_element_by_tag_name("div").find_element_by_tag_name("div").find_element_by_tag_name("div")\
			.find_element_by_tag_name("div").find_element_by_tag_name("a").find_element_by_tag_name("h3")\
				.find_element_by_tag_name("span").text

print("\n--- " + text + " ---\n")

driver.quit()
