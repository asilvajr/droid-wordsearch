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


def alterDiagLeft(grid) :
	row_size = len(grid[0])-1
	col_size = len(grid)-1
	diag = []
	print "alter left"
	# row_size + col_size - 1 => num_of_rows
	max_word_length = min(len(grid[0]),len(grid))	
	for i in xrange(col_size,0,-1) :
		lst=[]
		for j in xrange(0,col_size-i+1):	
			lst.append(grid[i+j][j])
		diag.append(lst)
	for j in xrange(0, row_size+1):
		lst=[]
		for i in xrange(0,row_size-j+1): 
#			print i, " ", j #debug tool
			lst.append(grid[i][i+j])
		diag.append(lst)
	return diag
			


def alter_right(grid):
        row_size = len(grid[0])-1
        col_size = len(grid)-1
	diag = []
        print "Alter right",row_size,col_size
	# row_size + col_size - 1 => num_of_rows
        for i in xrange(col_size,0,-1) :
                lst=[]
		for j in xrange(col_size,i-1,-1):
			print i," ",j
                        lst.append(grid[i-j][j])
                diag.append(lst)
        for j in xrange(0,row_size+1):
                lst=[]
                for i in xrange(0,row_size-j+1):
       #                 print j, " ", i #debug tool
                        lst.append(grid[j][j-i])
                diag.append(lst)
        return diag

	
def print_grid(grid) :
	print "Printitng"
	for item in grid : 
		print item #pretty print


read_grid(sys.stdin,sys.stdout)
print_grid(orig_grid)
#vert_grid = alter_vert(orig_grid)
print_grid(vert_grid)
diag_left = alterDiagLeft(orig_grid)
diag_right = alter_right(orig_grid)
print "left grid\n",print_grid(diag_left)
print "right grid\n",print_grid(diag_right)
print "Script Done"
