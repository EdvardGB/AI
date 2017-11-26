from Space import *
from Player import *

debugg = False


class State(object):
	def __init__(self, field, player, goaly, goalx):
		self.field = []
		self.player = player
		self.createField(field)
		self.goalx = goalx
		self.goaly = goaly
		self.field[goaly][goalx] = Space(False,True)
		self.visitCounter = 0	#how many times this state has been "done" or "visited"
		self.experience = 0 	#a number that changes after if it is a good(+) or a bad(-) experience 
		self.actionSerie = []	#a series of action taken from this state. This will probably be a difference when comparing states
		self.stateValue = 0			#a number of how good it is to bee in this state

	def __repr__(self):
		if debugg:
			print("Representing()")
		self.update()
		for line in self.field:
			print (self.get_nice_string(line))
		print("player: ", self.player.y, ",", self.player.x)
		return ""

	def update(self):
		if debugg:
			print("update()")
		if debugg:
			print("updating goal position to: [",self.goaly, ",",self.goalx,"]")
		self.field[self.goaly][self.goalx] = Space(False,True)
		if debugg:
			print("putting player on field on position: [",self.player.y, ",",self.player.x,"]" )
		self.field[self.player.y][self.player.x] = self.player
		

	def get_nice_string(self, list_or_iterator):
		return "" + "".join( str(x) for x in list_or_iterator) + ""

	def createField(self, file):
		self.field = []
		if debugg:
			print("createField()")
		with open(file) as f:
			lines = f.readlines()
			lines = [x.strip() for x in lines] 
			for line in lines:
				line = [x.strip() for x in line]
				objectline = []
				for s in line:
					if s == '.':
						objectline.append(Space(False, False))
					else:
						objectline.append(Space(True, False))
				self.field.append(objectline)	

	def getActions(self):
				# top   left	right bottom 	
		space = [[-1,0],[0,-1],[0,1],[1,0]]
		
		#top
		if self.player.y == 0:
			if debugg:
				print("1: y == 0")
			space = [[0,-1],[0,1],[1,0]]
			if debugg:
				print("space:", space)
			#top left and right
			if self.player.x == 0:
				if debugg:
					print("x == 0")
				space = [[0,1],[1,0]]
				if debugg:
					print("space:", space)
			elif self.player.x == len(self.field[0]) -1:
				if debugg:
					print("x == len(field)")
				space = [[1,0], [0,-1]]
				if debugg:
					print("space: ", space)

		#bottom
		elif self.player.y == len(self.field) -1:
			if debugg:
				print("2: y = len(field)")
			space = [[-1,0],[0,-1],[0,1]]
			if debugg:
				print("space:", space)
			# bottom left and right
			if self.player.x == 0:
				if debugg:
					print("x = 0")
				space = [[-1,0], [0,1]]
				if debugg:
					print("space:", space)
			if self.player.x == len(self.field[0]) -1:
				if debugg:
					print("x = len(field)")
				space = [[0,-1], [-1,0]]
				if debugg:
					print("space:", space)

		#left
		elif self.player.x == 0:
			if debugg:
				print("3: x = 0")
			space = [[-1,0],[0,1],[1,0]]
			if debugg:
				print("space:", space)

	

		#bottom
		elif self.player.x == len(self.field[0]) -1:
			if debugg:
				print("4: x = len(field)")
			space = [[-1,0],[0,-1],[1,0]]
			if debugg:
				print("space:", space)

			

		actions = []
		for s in space:
			s = [self.player.y + s[0], self.player.x + s[1]]
			if not self.field[s[0]][s[1]].obstructed:
				actions.append(s)
		return actions

		def movePlayer(self, action):
			self.player.y = action[0]
			self.player.x = action[1]
			self.update()
'''
debugg = False
player = Player(0,0)
S = State("f1.txt", player, 4,4)
for i in range(0,5):
	for j in range(0,5):
		S.player.x = i
		S.player.y = j
		actions = S.getActions()
		print(S)
		S.createField("f1.txt")


'''

		
