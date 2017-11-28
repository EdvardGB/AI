#from KnowledgeBase import * as KB
import copy

class Evaluator(object):
	

	def __init__(self,depthLimit,depthVar,startVar,goalpoints):
		self.depthLimit = depthLimit
		self.depthVar = depthVar
		#self.counterVar = counterVar
		#self.visitedVar = visitedVar
		self.startVar = startVar
		self.goalpoints = goalpoints
		#self.threshold = threshold		#for what? i forgot
		

	def isTerminal(self,state):
		#checking if state reached goal state

		if state.player.y == state.goaly and state.player.x == state.goalx:
			return True
		return False 

	def evaluate(self, state):
		
		# prepare any preparable values and such
		# run the evaluator

		#retun a int value of how good this state is  
		return self.evaluator(state,0)

	def generateRiskValue(self, state, depth):
		pass
		#The riskValue should be negative if bad and positive if good.
		
		#Based On the values: 
			# -increase of possible value loss
			# -unknownness
			# 	-state has been proven to generate low risk in the past. Does an action become less risky by getting experience/doing it multiple times.
			# 	-Would the program make decicions that lessens the possibility of doing a risky move, is that equal to experience of a human?
			# 	-generate a experience value 
			#	-Has nothing to do with the actual risk of an action expect avoidng that action 
			# -memory space
			# -depth
		# maybe implemented inside the recursive algo

		unknownnessValue = 2	#to be changed
		depthValue = 1 			#maybe to be changed
		riskValue = 1 			#or 10^10? Is a big number better?

		# if something-bad-will-happen-function():
		# 	set unknownnessValue*someVar, eks: someVar = 10^10 
		#for pit in 
		#if state.player

		#the calculation of risk is  

		# probably to be changed
		#if state.visited > 0
		#	riskValue = 
		#else:
		#	riskValue = 

		#return riskValue

	def getPossibleActionSerie(self, state, depth):
		#check if action is possible
		#if not, return None
		bestAction = None
		bestActionSeries = []
		bestValue = 0

		actions = state.getActions()

		for action in state.getActions():
			fstate = copy.deepcopy(state)
			fstate.movePlayer(action)
			actionSeries, value = self.evaluator(fstate, depth)
			if value > bestValue and not action in state.visited:
				bestAction = action
				bestActionSeries = actionSeries
				bestValue = value
		if bestAction == None:
			for action in state.getActions():
				qstate = copy.deepcopy(state)
				if not action in state.visited:
					bestAction = action
		if bestAction == None:
			bestAction = state.getActions()[0]
		bestActionSeries.append(bestAction)
		return bestActionSeries, bestValue

	def getPossibleMemoryActionSerie(self, state, depth, memory):
		pass
		value = 0
		for action in state.getActions():
			state.movePlayer(action)

		return 0

	def aquireMemories(self, state):
		pass
		memories = KB.getMemories(state) #Find nearly or equal previous states. Not implemented
		return memories

	def isBadState(self, state, value):
		pass
		#if value

	def updateState(self, state, experience):
		state.experience +=experience
		return 0

	def getGoalValue(self,state, depth):
		#return values based on reaching the goal
		value = self.goalpoints/(2**depth)
		return value

	def getValue(self, state, depth):
		pass
		#value = self.

		#return values based on not reaching the goal, but maybe a path that leads to goal.
		return 0

	def evaluator(self, state, depth):
		# may contain functions like:
		# -getting the relation between time and expected profitt
		# -

		#if reached terminal state or depth is reached, return a value
		if self.isTerminal(state):	
			return [], self.getGoalValue(state,depth)
		elif depth >= self.depthLimit:
			return [], self.getValue(state,depth)
		depth = depth +1
		actions = state.getActions()
		for action in actions:

			#####
			# Defining values for the algorith

			possibleNewState = copy.deepcopy(state) # Creating new state equal to the current. 
			#memories = aquireMemories(possibleNewState)
			#riskValue = generateRiskValue(possibleNewState) #Get possible risk of doing this action. Not implemented


			#####
			# The algotihm is based on
			# -Checking the best memories first, if there is one
			# -then checking a set of other possible action
			# -compare all values and return best value
			# -"checking" means:
			# 	- generate risk of the move
			#	- see if this is a state visited before
			#	- experience
			# -pruning?
			# -If state x<y, and y is not tolerable, add x to notPossible list
			'''
			if memories != None:
				for memory in memories:
					actionSeries = memory.actionSeries()
					actionSeriesValue = memory.stateValue
					possibleBetterActionSeries = []
					possibleBetterActionSeriesValue = 0

					for action in actionSeries:
						#possible better actionSeries = check if other possible actions are better
						#get value of doing the action in the memory actionseries
						memoryState = deepcopy(state) 
						actionseries, actionSeriesValue = getPossibleActionSerie(memoryState,depth,memory)
						
						possibleBetterActionSeries, possibleBetterActionSeriesValue = getPossibleActionSerie(possibleNewState, depth, action)
						

						
						if actionSeriesValue < possibleBetterActionSeriesValue:

							return possibleBetterActionSeries, possibleBetterActionSeriesValue
						return actionSeries, actionseries
				
			else:'''
			actionSeries = []
			actionSeriesValue = 0
			possibleBetterActionSeries, possibleBetterActionSeriesValue = self.getPossibleActionSerie(possibleNewState, depth)
			#if possibleBetterActionSeriesValue > actionSeriesValue:
			actionSeries = possibleBetterActionSeries
			actionSeriesValue = possibleBetterActionSeriesValue
			return actionSeries, actionSeriesValue
				#check other options

			

			



