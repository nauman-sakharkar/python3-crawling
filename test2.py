# -*- coding: utf-8 -*- 

from selenium import webdriver
from translate import Translator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException,ElementClickInterceptedException
import pandas as pd


translator= Translator(from_lang="es",to_lang="en")
driver = webdriver.Firefox()
driver.get('https://www.inba.gob.mx/inba/musica')
			
df = pd.DataFrame(columns=["No","Crawl Title","Date","Time","Venue"])
wait = WebDriverWait(driver, 3)

driver.find_element_by_xpath('//span[@class="bar-btn list-view"]').click()

events = driver.find_elements_by_xpath('//div[@class="tiva-event-list-full tiva-event-list"]/div/div[@class="event-item-right pull-left"]')

for i in range(len(events)):
	print(i)
	row=[]
	
	try:
		evs = driver.find_element_by_xpath('(//div[@class="tiva-event-list-full tiva-event-list"]/div/div[@class="event-item-right pull-left"])[position()='+str(i+1)+']/div[@class="event-name link"]').click()
		row.append(i+1)
		row.append(driver.find_element_by_xpath('//div[@class="event-name"]').text)
		print(driver.find_element_by_xpath('//div[@class="event-name"]').text)
		row.append(driver.find_element_by_xpath('//div[@class="event-date"]').text)
		row.append(driver.find_element_by_xpath('//div[@class="event-time"]').text)
		row.append(driver.find_element_by_xpath('//div[@class="event-location"]').text)
		try:
			#element = driver.find_element_by_xpath('//span[@class="bar-btn list-view"]')
			#driver.execute_script("return arguments[0].scrollIntoView(true);", element)
			#element.click()
			
			#driver.execute_script("arguments[0].scrollIntoView();", element)
			driver.find_element_by_xpath('//span[@class="bar-btn list-view"]').click().perform()
			wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="calendar-event-name one-day')))
		except Exception as e:
			print(e,"WAY===================")
			pass
	except TimeoutException:
		pass
	except NoSuchElementException:
		pass
	except Exception:
		driver.find_element_by_xpath('//span[@class="bar-btn list-view"]').click()
	df.loc[i]=row
df.to_csv('output.csv',index=False, sep='\t', encoding = 'utf-8')
			

#element=driver.find_element_by_class_name("nameOfClass")
#print(element.text)

driver.quit()