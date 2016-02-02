# Look through many PDB files, parse for total score, packstat, & burried unsat
# marco mravic Jan 2016 degrado lab

# take input path, look for all dirs with input(\d+), parse and store data from rosetta outputs
# After compiled data. plot

import sys, os, re, numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

# python initScoreCheckRosy.py ~/peptideAmyloid/rosettaFixBB/

data = defaultdict(list)
# look through input dirs
for dirN in os.listdir( sys.argv[1] ):
	match = re.search( r'input(\d+)', dirN )
	if match:
		index = match.group(1)
	else:
		continue

	# look through all _outX.pdb 
	path = os.path.join( sys.argv[1] , dirN )
	for f in os.listdir( path ):


		match = re.search( r'input(\d+)_out(\d+)', f )
		if match:
			index, outC = int( match.group(1) ), int( match.group(2))
		else:
			continue


		if '_out' not in f:
			continue
		fPath = os.path.join( path, f )

		# parse PDB file
		inF = open( fPath, 'rU' )

		for i in inF:
			if i[:4] == 'pose': 
					# Score cap (bad designs) @ 200
				
				score 		= float( i.rstrip().split()[-1] )
				if score > 120:
					score = 120

			elif i[:4] == 'pack':
				packstat 	= float( i.split()[1] )

			elif i[:3] == 'uhb':
				uhb			= int( i.split()[1] )

			else:
				continue 


		#print index, outC, score, packstat, uhb
		data[index].append( ( outC, score, packstat, uhb ) )
		#data dirN, f, score, packstat, uhb

		inF.close()

#matrix = np.zeros( ( len(data.keys() ), 10 ) )
matrix 	= np.zeros( ( 10, 100 )  )
matrix2 = np.zeros( ( 10, 110 )  )
print matrix

lables = []
good = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
for x in np.arange( 1, 101 ):
	if x in good:
		lables.append( str(x) )
	else:
		lables.append( '' )

lables2 = []
for x in np.arange( 1, 111 ):
	if x in good:
		lables2.append( str(x + 100) )
	else:
		lables2.append( '' )


# once read, print summary and place in matrix for plotting

for ind, dSet in sorted( data.items() ):

	array = sorted(dSet)
	#print ind, min( [ x[1] for x in array ] ), round( np.std( [ x[1] for x in array ] ), 2 ), array
	for y in array:
		#print y, y[1]

		if ind > 100:
			xind = ind-100
			matrix2[y[0]-1][xind-1] = y[1]
		else:
			matrix[y[0]-1][ind-1] = y[1]


#print matrix
#print matrix[:100]

# plotting time

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(2, 2))

axes[0].boxplot( matrix, labels = lables, showfliers=False )
axes[0].set_xlabel('Design scaffold number', fontsize=24)
axes[0].set_ylabel('Rosette Energy Units (REU)', fontsize=24)
for tick in axes[0].yaxis.get_major_ticks():
	tick.label.set_fontsize(20)

axes[1].boxplot(matrix2 , labels = lables2, showfliers=False)
axes[1].set_xlabel('Design scaffold number', fontsize=24)
axes[1].set_ylabel('Rosette Energy Units (REU)', fontsize=24)
for tick in axes[1].yaxis.get_major_ticks():
	tick.label.set_fontsize(20)

plt.show()







