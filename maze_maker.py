import random

maze = set()
directions = {'e': (1,0), 's': (0, 1), 'w': (-1, 0), 'n': (0, -1), 'h': (0, 0)}

def make_maze(path_depth=15):
	x = 0
	y = 0
	
	for i in range(path_depth):
		maze.add((x, y))
		xd, yd= random.choice(directions.values())
		x += xd
		y += yd
		
	return maze
