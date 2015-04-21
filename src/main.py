import random, time
from sys import stdin
from state_manager import *
from game_over import GameOver

state = StateManager()

bad_dave = [ "What are you doing Dave?", "I'm afraid I can't do that Dave.", "Would you like me to sing you a song Dave?" ]

actionMap = {
	"walk": "go",
	"dance": "go",
	"move": "go",
	"go": "go",
	"yell": "yell"
}

nouns = [ "knife", "skeleton", "hat", "left", "right", "up", "down", "forward", "backwards" ]

while True:
	text = stdin.readline().lower().rstrip('\n')

	action = None
	objectNoun = None
	subjectNoun = None

	for i in text.split(' '):
		if not action and i in actionMap:
			action = actionMap[i]
		elif not objectNoun and i in nouns:
			objectNoun = i
		elif not subjectNoun and i in nouns:
			subjectNoun = i
		if action and objectNoun and subjectNoun:
			# We have all the things
			break
	if action and not objectNoun:
		objectNoun = text.replace(action, '').replace('  ', ' ').lstrip(' ').rstrip(' ')

	try:
		state.do_the_thing(action, objectNoun)#, subjectNoun)
	except GameOver as e:
		print e.value
		print "You have died."
		time.sleep(2)
		print "Sorry."
		state = StateManager()
	except Exception:
		print random.choice(bad_dave)
