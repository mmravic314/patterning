 # scl enable python27 'python extract_scores.py ./scores/ ~/peptideAmyloid/OsakaModels/ ~/peptideAmyloid/scoreDict.pkl '



import os, gzip, sys, cPickle as pic

pdbDir = sys.argv[2]

pklPath=sys.argv[3] 

scoresDict = {}

## look through directory of .cmap files
## with same path, find parameters, and look if score file present
## if score not found, place zeros; else, record actual score
## print paths, params, scores to cPickled hash:w


for i in os.listdir( sys.argv[1] ):
	path = os.path.join( sys.argv[1], i  )


	if i[-7:] != 'cmap.gz': continue

	modelID = i[:-8].split( '_' )[-1]
	scPath  = os.path.join( sys.argv[4], 'model_%s.sc' % ( modelID ) )
	pdbPath = os.path.join( sys.argv[2], 'model_%s.pdb.gz' % ( modelID )  )
	#print pdbPath
	
	# grab params
	with gzip.open( pdbPath, 'r' ) as file:
		for k in file:	
			params = [ float( j ) for j in  k.split()[2:8] ]
			break
	# grab score
	if not os.path.exists( scPath ):
		
		scoresDict[ modelID ] = ( ( 0, 0, 0 ), params )
		print modelID, (0,0,0), params, scPath 
		continue

	with open( scPath ) as file:
		for k in file:
			if k[0] == 't': continue
			scores = tuple( [ int( j ) for j in  k.split() ] )	
			print scores		                     
#	sys.exit()
	
	scoresDict[ modelID ] = ( scores, params )
	print modelID, scores, params

pic.dump( scoresDict , open( pklPath , 'wb' )  )
