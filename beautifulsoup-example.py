# -*- coding: utf-8 -*-

import requests, re
from bs4 import SoupStrainer,BeautifulSoup as BS

# URL to crawl (Keep http rather than https in URL because requests.get function can't redirect url from https to http)
url = "http://www.iplt20.com/results/men"

# headers (not compulsory)
header_details = {'Upgrade-Insecure-Requests': '1','User-Agent': 'testBot'}
# header_details = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Cookie' : '_ga=GA1.2.1733924135.1546234185; _gid=GA1.2.2107664175.1546427963'}

reqvar = requests.get(url, headers = header_details)

'''
========================================================================================
BeautifulSoup Reference : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
========================================================================================
'''

# created filter - div whose class contains js-match match-list__item
custom_filter = SoupStrainer('div', {'class': re.compile('js-match match-list__item')})

# using lxml’s HTML parser
soup = BS(reqvar.text,'lxml', parse_only = custom_filter)

#fixtures = soup.find_all('div', recursive=False)
fixtures = soup('div', recursive=False)

# if data found
if (fixtures):

	#iterating through all fixtures
	for fixture in fixtures:

		# printing fixture with properly formatted html
		# print(fixture.prettify())

		# searching only in direct child
		# , recursive=False in find and find_all

		#getting class attribute of current element
		#classes = fixture['class']

		# finding divs with class result__team and likewise others
		teams = fixture.find_all('div', {'class': 'result__team'})
		winning_team = teams[0].find('p',{'class':'result__team-name'}).text.strip()
		losing_team = teams[1].find('p',{'class':'result__team-name'}).text.strip()

		winning_team_score = teams[0].find('span',{'class':'result__score'}).text.strip().split("  ")
		losing_team_score = teams[1].find('span',{'class':'result__score'}).text.strip().split("  ")

		result = fixture.find('p', {'class': 'result__outcome u-hide-phablet'}).text.strip()
		match_details = fixture.find('p', {'class': 'result__info u-hide-phablet'}).text.strip()
		
		print("Team 1 : ",winning_team,", Team 2 :",losing_team)
		print("Team 1 Score : ",winning_team_score,", Team 2 Score :",losing_team_score)
		print("Match Details : ",match_details)
		print("Match result : ",result)
		print("--------------------------------------------------------------------")

# CSS Selector		 
# all_matches = soup.select('div[class*="js-match match-list__item "]')