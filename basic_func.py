#!/usr/bin/python
import sys
# python basic_func.py < WordGrid.txt
orig_grid = []
vert_grid = []
diag_left = []
diag_right = []

def read_grid(r,grid) :
	print "inCreate"
	global orig_grid
	line = r.readline()
	while line != "" :
		orig_grid.append(line.split())
		line = r.readline()

def alter_vert(grid):
	print "inAlterVert"
	return zip(*grid) #alters the view for it to be vertical
	#return zip (*grid[::-1]) 


def diag_left(grid) :
	max_word_length = min(len(grid[0]),len(grid))	
	
def print_grid(grid) :
	print "Printitng"
	for item in grid : 
		print item #pretty print


read_grid(sys.stdin,sys.stdout)
print_grid(orig_grid)
vert_grid = alter_vert(orig_grid)
print_grid(vert_grid)
print "Script Done"
