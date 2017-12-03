from Space import *
from Player import *
from PIL import Image

debugg = False


class State(object):
	def __init__(self, field, player, goaly, goalx, counter, experience, actionSerie):
		self.field = []
		self.player = player
		self.createField(field)
		self.goalx = goalx
		self.goaly = goaly
		self.visitCounter = counter	#how many times this state has been "done" or "visited"
		self.experience = experience 	#a number that changes after if it is a good(+) or a bad(-) experience 
		self.possibleValue = 0	#a number used in evaluation
		self.previousSerie = []	#a series of action taken from this state. This will probably be a difference when comparing states
		self.dangers = []		#pits. game over if reached
		self.equlaToStart = 0	#how equal this state is to start
		self.visited = []


	def __repr__(self):
		if debugg:
			print("Representing()")
		self.update()
		for line in self.field:
			print(self.get_nice_string(line))
		print("player: (", self.player.y, ",", self.player.x, "), exp:", self.experience, "visited:",self.visitCounter)
		return ""

	def update(self):
		if debugg:
			print("update()")
		if not len(self.field) == 0:
			if debugg:
				print("updating goal position to: [",self.goaly, ",",self.goalx,"]")
			self.field[self.goaly][self.goalx] = Space(False,True,False)
			if debugg:
				print("putting player on field on position: [",self.player.y, ",",self.player.x,"]" )
			self.field[self.player.y][self.player.x] = self.player
		

	def get_nice_string(self, list_or_iterator):
		return "" + "".join( str(x) for x in list_or_iterator) + ""

	def createField(self, file):
		self.field = []
		if file == None:
			return ""
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
						objectline.append(Space(False, False, False))
					elif s == 'O':
						state.dangers.append(s)
						objectline.append(Space(False, False, True))
					else:
						objectline.append(Space(True, False, False))
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
		self.visited.append(action)
		self.field[self.player.y][self.player.x] = Space(False,False,False)
		self.player.y = action[0]
		self.player.x = action[1]
		self.update()

	def makeImg(self): # print bildet
		images = [Image.new('RGB', (16,16), "white"),	# 0
					Image.new('RGB', (16,16), "black"),	# 1
					Image.new('RGB', (16,16), "red"),	# 2
					Image.new('RGB', (16,16), "green"),	# 3
					Image.new('RGB', (4,4), "blue")]	# 4
		image = Image.new('RGB', (16*16,16*14), "white")
		
		for y in range(len(self.field)):
			for x in range(len(self.field[0])):
				if self.field[y][x].type == "Player":
					image.paste(images[2], (x*16,y*16))
				else:
					if self.field[y][x].obstructed:
						image.paste(images[1], (x*16,y*16))
					elif self.field[y][x].goal:
						image.paste(images[3], (x*16,y*16))
					else:
						image.paste(images[0], (x*16,y*16))
		for n in self.visited:
			image.paste(images[4], (n[1]*16 +6,n[0]*16 +6))
		return image
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

		
