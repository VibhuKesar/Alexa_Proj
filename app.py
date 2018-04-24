import logging
from flask import Flask
from flask_ask import Ask, statement, question
import requests
# import pprint

apiKey = ''

app = Flask(__name__)
ask = Ask(app,"/")

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent("MyNameIsIntent")
def my_name_is(firstname):
	r = requests.get('https://fortnite.y3n.co/v2/player/' + firstname,
                 headers={'X-Key': apiKey}).json()

	kills = r['br']['stats']['pc']['all']['kills']
	kpd =  r['br']['stats']['pc']['all']['kpd']
	winR =  r['br']['stats']['pc']['all']['winRate']
	wins =  r['br']['stats']['pc']['all']['wins']
	
	# print(playerName + " has overall K.D.A " + str(kpd) + " winrate " + str(winR) + " and total Kills " + str(kills) +  " and Wins are " + str(wins))

	msg = "{firstname} has kill death average".format(firstname=firstname)
	 # kpd=kpd, winR = winR, kills = kills, wins = wins)
	return statement(msg)


if __name__ == '__main__':
	app.run(debug=True)






# pp = pprint.PrettyPrinter(indent=4)



# pp.pprint()

