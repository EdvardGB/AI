from State import *
from Player import *
from Evaluator import *
from KnowledgeBase import * 
import copy

def recursiveValue(goalState, KB):
	print(len(goalState.previousSerie))
	for i in range (0,len(goalState.previousSerie)):
		key = goalState.previousSerie[i]
		state = KB.get((key[0],key[1]))
		value = 10000/(2**(len(goalState.previousSerie)-i))
		state.experience+=value
		print(i, key, value)
		KB.add(state)



def main():
	player = Player(0,0)
	state = State("f1.txt",player, 2,3,0,0,[])
	evaluator = Evaluator(2, None, None,10000)
	actionSeries, value = evaluator.evaluate(state)
	newState = copy.deepcopy(state)
	state.previousSerie.append(actionSeries[len(actionSeries)-1])
	KB = KnowledgeBase()
	KB.load()
	print(KB.memory)
	'''
	KB.flash()
	KB.add(state)
	

	while value != 10000:
		newState = copy.deepcopy(newState)
		newState.previousSerie.append(actionSeries[len(actionSeries)-1])
		newState.movePlayer(actionSeries[len(actionSeries)-1])
		actionSeries, value = evaluator.evaluate(newState)
		KB.add(newState)
		#print(newState)
	recursiveValue(newState,KB)
	KB.save()
	
	'''
main()