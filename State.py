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
		self.visitCounter = 1

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



debugg = False
player = Player(0,0)
S = State("f1.txt", player, 4,4)
for i in range(0,5):
	for j in range(0,5):
		S.player.x = i
		S.player.y = j
		actions = S.getActions()
		for x in actions:
			S.field[x[0]][x[1]].obstructed = True
		print(S)
		S.createField("f1.txt")

		


'''
	def obstructed(self,x,y):
		if self.field[x][y] != '.' and self.field[x][y] != '#' :
			return True
		return False

	def getActions(self, player):
			  # TopLeft MiddleL	  BL	TopM   BM	 TopR	MR 	  BR	
		space = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
		if player.y == 0:
				space = [[-1,0],[-1,1],[0,1],[1,0],[1,1]]
		if player.y == len(self.field) -1:
				space = [[-1,-1],[-1,0],[0,-1],[1,-1],[1,0]]
		if player.x == 0:
				space = [[0,-1],[0,1],[1,-1],[1,0],[1,1]]
		if player.x == len(self.field[0]) -1:
				space = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1]]
		
		personalSpace = []
		positions = []
		for s in space:
			#print s[0],s[1],player.y, player.x

			s[0] = s[0] + player.x
			s[1] = s[1] + player.y
			o = self.field[s[0]][s[1]]
			personalSpace.append(o)
			positions.append(s)
		return personalSpace, positions 
'''