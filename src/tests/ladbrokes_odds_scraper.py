from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.ladbrokes.com.au/sports/tennis")

time.sleep(5)

all_events_container = driver.find_element_by_id("page-content").find_element_by_class_name("competition-events")
events = all_events_container.find_elements_by_class_name("sport-event-card")

for event in events:
	title = event.find_element_by_class_name("sports-event-title__name-text").text
	odds = event.find_elements_by_class_name("price-button-odds-price")
	print("Title: " + title)
	print("\t\t" + odds[0].text + "\t" + odds[1].text)

driver.quit()
