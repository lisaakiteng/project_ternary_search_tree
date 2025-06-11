# project_ternary_search_tree
This project is part of a data science course and involves implementation, testing, and benchmarking of Ternary Search Tree using Python and Git version control. 

## Code Overview

### Main Components

- `Ternary_Search_Tree_results.ipynb`: Contains the results and discussions on the implementation of the project
- `ternary_search_tree.py`: Contains the TernarySearchTree Class
- `insert_benchmark.py`: Script to run and time the insertion operation
- `search_benchmark.py`: Script to run and time the search operation
- `inserttestjob.slurm`: SLURM batch script to run the insert_benchmark 
- `searchtestjob.slurm`: SLURM batch script to run the search_benchmark
- `slurm_insert_results.out`: results for the insert_benchmark
- `slurm_search_results.out`: results for the search_benchmark

### HPC Usage

All benchmakring scripts were executed on an HPC (Vlaams Supercomputer Centrum) to benefit from faster execution and handling of repeated runs.


### Conclusion

The benchmark successfully demonstrates how TST performance changes with tree size, insertion and search sample sizes. The results and visualizations provide insight into the TST's scalability. 