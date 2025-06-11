#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:20:00

module purge
module load Python/3.11.5-GCCcore-13.2.0
module load matplotlib

time python insert_benchmark.py