# submit fixed BB minimization jobs for de novo sequence design of 
# input di-helix recognition peptide on set amyloid interface
##
# Inputs for rosetta job

# -parser:script_vars cst_file=PATH comp_file=PATH

# 1) path 2 rosetta main
# 2) path to input structure
# 3) path to XML script for protocol
# 4) resfile path
# 5) atom restraint coordinate path
# 6) residue composition score file path
import sys, os, subprocess as sp

# python submitPatterningJobs.py ~/binLocal/Rosetta/main/ ~/peptideAmyloid/rosettaFixBB/input1/input1.pdb ~/peptideAmyloid/rosettaFixBB/patterningFixedBB_Mravic.xml  ~/peptideAmyloid/rosettaFixBB/input1/input1.resfile ~/peptideAmyloid/rosettaFixBB/input1/input1.cst ~/peptideAmyloid/rosettaFixBB/disfavour_polyLys.comp


# Variable args
rosetta_database_path   = os.path.join( sys.argv[1] , 'database/' )
rosetta_scriptsEXE_path = os.path.join( sys.argv[1], 'source/bin/rosetta_scripts.linuxgccrelease' )
design_script_path      = sys.argv[3]
resfile_path            = sys.argv[4]
cst_path				= sys.argv[5]
comp_path 				= sys.argv[6]
output_prefix			= os.path.dirname( sys.argv[2] ) + '/'

cmd = [
		rosetta_scriptsEXE_path,
		'-database', rosetta_database_path,
		'-parser:protocol', design_script_path,
		'-in:file:s', sys.argv[2],
		'-out:prefix', output_prefix,   
		'-out:suffix', '_out',                               
		'-out:no_nstruct_label',
		'-out:overwrite',
        '-packing:resfile', resfile_path,
		'-parser:script_vars', 'cst_file=%s' % ( cst_path ), 'comp_file=%s' % (comp_path), 

]

print
print cmd
print

sp.call( cmd )
