class Space(object):
	def __init__(self, obstructed, goal):
		self.obstructed = obstructed
		self.goal = goal

	def __repr__(self):
		if self.obstructed:
			return "#"
		elif self.goal:
			return "0"
		return "."
