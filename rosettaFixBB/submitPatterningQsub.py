#!/usr/bin/env python2

#$ -S /usr/bin/python
#$ -l mem_free=1G
#$ -l arch=linux-x64
#$ -l netapp=1G
#$ -l h_rt=00:05:00
#$ -cwd
#$ -j y
#$ -t 1-10


# submit fixed BB minimization jobs for de novo sequence design of 
# input di-helix recognition peptide on set amyloid interface
##
# Inputs for rosetta job

# -parser:script_vars cst_file=PATH comp_file=PATH

# 1) path 2 rosetta main
# 2) path to input dir ( auto-find: resfile, cst_file, structure )
# 3) path to XML script for protocol
# 4) residue composition score file path
import sys, os, subprocess as sp, re

# python submitPatterningJobs.py ~/binLocal/Rosetta/main/ ~/peptideAmyloid/rosettaFixBB/input1 ~/peptideAmyloid/rosettaFixBB/patterningFixedBB_Mravicmini.xml  ~/peptideAmyloid/rosettaFixBB/disfavour_polyLys.comp

#### INPUT NOTE: Due to author laziness,regex fails for '~/peptideAmyloid/rosettaFixBB/input1/' .... so leave this '/' out!!!

################## MAIN #######################
# Non-variable args
rosetta_database_path   = os.path.join( sys.argv[1] , 'database/' )
rosetta_scriptsEXE_path = os.path.join( sys.argv[1], 'source/bin/rosetta_scripts.linuxgccrelease' )
design_script_path      = sys.argv[3]
comp_path 				= sys.argv[4]

# Variable args
match = re.search( r'input(\d+)', os.path.basename( sys.argv[2] ) )
if match:
	index = match.group(1)
else:
	print 'PDB input directory syntax failure'
	sys.exit()

struc_path				= os.path.join( sys.argv[2], 'input%s.pdb' % (index) )
resfile_path            = os.path.join( sys.argv[2], 'input%s.resfile' % (index) )
cst_path				= os.path.join( sys.argv[2], 'input%s.cst' % (index) )
output_prefix			= os.path.dirname( sys.argv[2] ) + '/'

cmd = [
		rosetta_scriptsEXE_path,
		'-database', rosetta_database_path,
		'-parser:protocol', design_script_path,
		'-in:file:s', sys.argv[2],
		'-out:prefix', output_prefix,   
		'-out:suffix', '_out%d' & (os.environ["SGE_TASK_ID"]),                               
		'-out:no_nstruct_label',
		'-out:overwrite',
        '-packing:resfile', resfile_path,
		'-parser:script_vars', 'cst_file=%s' % ( cst_path ), 'comp_file=%s' % (comp_path), 

]

print
print cmd
print

sp.call( cmd )
