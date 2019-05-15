# -*- coding: utf-8 -*-

from requests_html import HTMLSession

'''
========================================================================================
Reference : https://html.python-requests.org/
========================================================================================
'''

session = HTMLSession()
resp = session.get("http://www.iplt20.com/results/men")

# CSS Selector
matches = resp.html.find(".match-list__item")

for match in matches:

	# Finding divs with class result__team and likewise others
	# first=True (for getting only 1 item)
	teams = match.find(".result__team")
	winning_team = teams[0].find('.result__team-name', first=True).text.strip()
	losing_team = teams[1].find('.result__team-name', first=True).text.strip()
	
	winning_team_score = teams[0].find('span.result__score', first=True).text.strip().split("  ")
	losing_team_score = teams[1].find('span.result__score', first=True).text.strip().split("  ")

	result = match.find(".result__outcome", first=True).text.strip()
	match_details = match.find('.result__info', first=True).text.strip()
	
	print("Team 1 : ",winning_team,", Team 2 :",losing_team)
	print("Team 1 Score : ",winning_team_score,", Team 2 Score :",losing_team_score)
	print("Match Details : ",match_details)
	print("Match result : ",result)
	print("--------------------------------------------------------------------")


# JavaScript

'''
script = """
        () => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }
    """

# Render JavaScript
resp.html.render()

# We can execute custom script also by providing script paramenter in render
# resp.html.render(script=script, reload=False)
print(resp.html.html)
print(resp.html.find(".match-list__item"))
'''