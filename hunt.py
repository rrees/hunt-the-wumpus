from maze_maker import make_maze, directions
import random

class Hunt:
	def __init__(self):
		self.maze = make_maze()
		self.hunter = random.choice(list(self.maze))
		self.wumpus = random.choice(list(self.maze))
	
	def has_hunter_found_wumpus(self):
		return self.wumpus == self.hunter
	def move_wumpus(self):
		dx, dy = random.choice(directions.values())
		new_position = (self.wumpus[0] + dx, self.wumpus[1] + dy)
		if new_position in self.maze:
			self.wumpus = new_position
	def game(self):
		while True:
			print "You are at %d,%d" % self.hunter
			
			direction = raw_input()
			assert direction in directions.keys()
			
			dx, dy = directions[direction]
			
			new_position =  (self.hunter[0] + dx, self.hunter[1] + dy)
			if new_position in self.maze:
				self.hunter = new_position
			else:
				print "You can't go in that direction!"
			
			if self.has_hunter_found_wumpus():
				print "FOUND WUMPUS"
				return
			print "not yet with the wumpus"
			self.move_wumpus()
			
			# find out if wumpus is next to you
			if (abs(self.hunter[0] - self.wumpus[0]) < 2) and (abs(self.hunter[1] - self.wumpus[1])):
				print "The Wumpus is galluphing nearby!"
				
Hunt().game()