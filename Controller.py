from State import *
from Player import *
from Evaluator import *
from KnowledgeBase import * 
import copy

def recursiveValue(goalState, KB, gv):
	for i in range (0,len(goalState.previousSerie)):
		key = goalState.previousSerie[i]
		state = KB.get((key[0],key[1]))
		#print(key, state.experience)
		value = gv/(2**(len(goalState.previousSerie)-i))
		state.experience+=value
		#print(key, state.experience)



def main():
	goalValue = 100

	player = Player(0,0)
	state = State("f1.txt",player, 2,3,1,0,[])
	evaluator = Evaluator(2, None, None,goalValue)
	actionSeries, value = evaluator.evaluate(state)
	newState = copy.deepcopy(state)
	state.previousSerie.append(actionSeries[len(actionSeries)-1])
	KB = KnowledgeBase()
	KB.load()
	KB.add(state)
	
	while value != goalValue:
		newState = copy.deepcopy(newState)
		newState.previousSerie.append(actionSeries[len(actionSeries)-1])
		newState.movePlayer(actionSeries[len(actionSeries)-1])
		actionSeries, value = evaluator.evaluate(newState)
		KB.add(newState)
		#print(newState)
	recursiveValue(newState,KB, goalValue)
	KB.flash()
	KB.save()
	#print(KB.memory)
main()