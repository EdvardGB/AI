#from KnowledgeBase import * as KB

class Evaluator(object):
	
	'''
	def __init__(self,depthLimit,depthVar,counterVar,visitedVar,startVar,goalpoints):
		self.depthVar = depthVar
		self.counterVar = counterVar
		self.visitedVar = visitedVar
		self.startVar = startVar
		self.goalpoints = goalpoints

		self.depthLimit = depthLimit

	'''

	def getGoalValue(self,depth):
		pass
		#value = 

		#return values based on reaching the goal
		return value

	def getValue(self, depth):
		pass
		#value = 

		#return values based on not reaching the goal, but maybe a path that leads to goal.
		return value

	def isTerminal(self,state):
		pass
		#checking if state reached goal state

		if state.player.y == state.goaly and state.player.x == state.goalx:
			return True
		return False 

	def evaluate(self, state):
		pass
		# prepare any preparable values and such
		# run the evaluator

		#retun a int value of how good this state is  
		return 0

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
		depthValue = 1 		#maybe to be changed
		riskValue = 1 #or 10^10? Is a big number better?

		# if something-bad-will-happen-function():
		# 	set unknownnessValue*someVar, eks: someVar = 10^10 

		#the calculation of risk is  

		# probably to be changed
		if state.visited > 0
			riskValue = 
		else:
			riskValue = 

		return riskValue

	def getPossibleActionSerie(self, state, depth, memoryAction):
		pass

		return 0

	def getPossibleMemoryActionSerie(self, state, depth, memory):
		pass

		return 0

	def aquireMemories(self, state):
		memories = KB.getMemories(state) #Find nearly of equal previous states Not implemented
		return memories

	def evaluator(self, state, depth):
		# may contain functions like:
		# -getting the relation between time and expected profitt
		# -

		#if reached terminal state or depth is reached, return a value
		if isTerminal(state):
			return getGoalValue (depth)
		elif depth >= self.depthLimit:
			return getValue(depth)
		depth = depth +1
		actions = state.getActions()
		for action in actions:

			#####
			# Defining values for the algorith

			possibleNewState = deepcopy(state) # Creating new state equal to the current. 
			possibleNewState.movePlayer(action) # change state to possible next state
			memories = aquireMemories(possibleNewState)
			riskValue = generateRiskValue(possibleNewState) #Get possible risk of doing this action. Not implemented


			#####
			# The algotihm is based on
			# -Checking the best memories first, if there is one
			# -then checking a set of other possible action
			# -compare all values and return best value
			# -"checking" means:
			# 	- generaate risk of the move
			#	- see if this is a state visited before
			#	- experience

			if memories != None:
				for memory in memories:
					actionSeries = memory.actionSeries()
					actionSeriesValue = memory.stateValue

					possibleBetterActionSeries = []
					possibleBetterActionSeriesValue = 0

					for action in actionSeries:
						#possible better actionSeries = check if other possible actions are better
						#get value of doing the action in the memory actionseries
						possibleBetterActionSeries, possibleBetterActionSeriesValue = getPossibleActionSerie(possibleNewState, depth, action)
						
			else:
				#check other options

			

			



