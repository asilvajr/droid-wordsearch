#!/usr/bin/python
import sys
# python basic_func.py < WordGrid.txt
WordList=['ALCOHOL','BEER','BYE','COMPUTERS','COOKIES','ELECTTRONIC',
	'FUCK','GOODGAME','HELLO','HIPPIE','HIPSTER','LOVE','SEX','TELE']

def read_grid(r,grid) :
	print "inCreate"
	orig_grid = []
	line = r.readline()
	while line != "" :
		orig_grid.append(line.split())
		line = r.readline()
	return orig_grid
def alter_vert(grid):
	print "inAlterVert"
	return zip(*grid) #alters the view for it to be vertical
	#return zip (*grid[::-1]) 


def alter_left(grid) :
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
	# row_size + col_size - 1 => num_of_rows
        for i in xrange(col_size,0,-1) :
                lst=[]
		for j in xrange(col_size,i-1,-1):
	#		print i," ",j
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


def merge_characters(grid):
	lst=[]
	for item in grid:
		lst.append(''.join(item))
	return lst

orig_grid=read_grid(sys.stdin,sys.stdout)
#print_grid(orig_grid)
vert_grid = alter_vert(orig_grid)
#print_grid(vert_grid)
left_grid = alter_left(orig_grid)
right_grid = alter_right(orig_grid)
print "left grid\n",print_grid(left_grid)
print "right grid\n",print_grid(right_grid)
def find_word(word):
	global orig_grid
	std_strs = merge_characters(orig_grid)
	ver_strs = merge_characters(vert_grid)
	left_strs = merge_characters(left_grid)
	right_strs = merge_characters(right_grid)
	for string in (std_strs + ver_strs + left_strs + right_strs):
		result = word.find(string)
		if result > -1:
			return True
	return False
def find_words():
	global WordList
	lst=[]
	for word in WordList:
		lst.append(find_word(word))
	return lst
#print "Strings",print_grid(merge_characters(orig_grid))
#print "Strings",print_grid(merge_characters(vert_grid))
#print "Strings",print_grid(merge_characters(left_grid))
#print "Strings",print_grid(merge_characters(right_grid))
print "Results: ",print_grid(find_words())
print "Done!"
