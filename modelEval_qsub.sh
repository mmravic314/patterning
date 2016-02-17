#!/bin/bash

#$ -S /bin/bash
#$ -l mem_free=16G
#$ -l arch=linux-x64
#$ -l netapp=1G
#$ -l h_rt=00:25:00
#$ -cwd
#$ -j y
#$ -o /netapp/home/mmravic/peptideAmyloid/logfiles/

### Know task from number of length of list file or number of pdb's in directory... hardcode in
#$ -t 1 

### example command line on cluster(SGE): qsub ../modelEval_qsub.sh list.txt

# make array of all input pdb paths in list file (input argument 1, one path per line)
# link paths to task ID, and submit each as separate job
tasks=(0)
while read -r line
	do 
	tasks=(${tasks[*]} $line)
done < $1
inputPath="${tasks[$SGE_TASK_ID]}"
echo '~/binLocal/termanal/runPept.py --p $inputPath --o ~/peptideAmyloid/OsakaModels/ --v'

scl enable python27 'python ~/binLocal/termanal/runPept.py --p $inputPath --o ~/peptideAmyloid/OsakaModels/ --v'

