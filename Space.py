class Space(object):
	def __init__(self, obstructed, goal, pit):
		self.type = "Space"
		self.obstructed = obstructed
		self.goal = goal
		self.pit = pit

	def __repr__(self):
		if self.obstructed:
			return "#"
		elif self.goal:
			return "G"
		elif self.pit:
			return "O"
		return "."
