from State import *
from Player import *
from Evaluator import *
#from Knowledgebase import *

def main():
	player = Player(0,0)
	startState = State("f2.txt",player, 10,7,0,0,[])
	evaluator = Evaluator(3, None, None,10000)
	actionSeries, value = evaluator.evaluate(startState)

	while value != 10000:
		print(startState)
		startState.movePlayer(actionSeries[len(actionSeries)-1])
		actionSeries, value = evaluator.evaluate(startState)

	image = startState.makeImg()
	
	image.save("_3_DJK.png")
		


main()