#!/usr/bin/env python2.7

#$ -S /usr/bin/python
#$ -l mem_free=1G
#$ -l arch=linux-x64
#$ -l netapp=1G
#$ -l h_rt=00:05:00
#$ -cwd
#$ -j y
#$ -o /netapp/home/mmravic/peptideAmyloid/rosettaFixBB/logfiles/
#$ -t 1-2
import os

test 	= str(os.environ['SGE_TASK_ID'] )

outFile = open( 'testOut%s.txt' % (test) , 'w')
outFile.write( 'Hello World' )
