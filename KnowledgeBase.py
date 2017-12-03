from State import *
from Player import *
import copy
# for the comaprable function, use a function that converts to CNF and considers the truthtable

# create many "rules of beliefs"/ first order logic rules, but make rules for the truthness of those rules based on variables such that
# the credability of a rule is not 100%, and therefore can be changed or more rules can be added to make it more credabel. 

class KnowledgeBase():
	def __init__(self):
		self.memory = {}

	def get(self,key):
		if key in self.memory.keys():
			return self.memory[key]
		return None

	def add(self,state):
		state = copy.deepcopy(state)
		key = (state.player.y, state.player.x)
		if key in self.memory.keys():
			mState = self.get(key)
			print(key, state.experience, "+",(mState.player.y,mState.player.x), mState.experience)
			state.experience += mState.experience
			state.visitCounter += mState.visitCounter
		self.memory[key] = state
		#print(self.memory.keys())

	def save(self):
		file = open("memory.txt", "a")
		for key in self.memory.keys():
			state = self.get(key)
			k=""
			k+=str([action for action in state.previousSerie])
			line = str(key)+ ","+ str(state.goaly)+ ","+ str(state.goalx)+ ","+ str(state.visitCounter)+ ","+ str(state.experience)+ "," + k + "\n"
			file.write(line)
		file.close()

	def load(self):
		file = open("memory.txt", "r")
		content = file.readlines()
		content = [x.strip() for x in content]
		x = 0
		for line in content:
			x+=1
			keyy = ""
			keyx = "" 
			goaly = ""
			goalx = ""
			counter = ""
			experience = ""
			actions = []
			action = []
			c = 0
			for i in range(1,len(line)):
				if line[i] == ',':
					c+=1
					continue
				elif line[i] == " " or line[i] == ")":
					continue
				if c == 6:
					s = False
					#print("start",i)
					while i < len(line):
						#print(x, i, line[i])
						if line[i] == '[':
							s = True
							i+=1
							continue
						elif line[i] == ']':
							s = False
							if len(action) > 1:
								actions.append(action)
							action = []
							i+=1
							continue
						if s:
							if not line[i] == ',' and not line[i] == '[' and not line[i] == ' ':
								action.append(int(line[i]))
								#print(action)
						i+=1
					if i == len(line):
						break
				else:
					if c == 0:
						keyy += line[i] 
					elif c==1:
						keyx += line[i]
					elif c==2:
						goaly += line[i]
					elif c==3:
						goalx += line[i]
					elif c==4:
						counter += line[i]
					elif c==5:
						experience += line[i]  
			#print(int(goaly),int(goalx),int(counter),float(experience),actions)
			state = State(None,Player(int(keyy),int(keyx)),int(goaly),int(goalx),int(counter),float(experience),actions)
			self.add(state)	




			

	def flash(self):
		file = open("memory.txt", "w")
		file.close()