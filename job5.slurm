#!/bin/bash

#SBATCH --job-name=audioset
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jucha@cs.washington.edu

#SBATCH --account=cse
#SBATCH --partition=gpu-a40
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=10G
#SBATCH --gpus=0
#SBATCH --time=00-24:00:00 # Max runtime in DD-HH:MM:SS format.

#SBATCH --chdir=/gscratch/cse/jucha/audioset/
#SBATCH --export=all
#SBATCH --output=/gscratch/cse/jucha/audioset/5/output.txt # where STDOUT goes
#SBATCH --error=/gscratch/cse/jucha/audioset/5/err.txt # where STDERR goes

python3 check.py 4 5