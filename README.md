# RHHH Reproduction
Reproduction of results from the "Constant Time Updates in Hierarchical Heavy Hitters" paper, ACM SIGCOMM 2017, by Ran Ben Basat, Gil Einziger, Roy Friedman, Marcelo Caggiani Luizelli, and Erez Waisbard.

/******************************************************************************************************************************/

This repo is forked from the authors' main repository, which contains open source implementations of their randomized hierarchical heavy-hitters algorithms, implemented by Ran Ben Basat (sran[at]cs.technion.ac.il) in 2017.

Austin Poore and I (Lecheng Fan) added additional code to parse all the output and plot the results. We wanted to recreate Figures 2, 3, 4 and 5 from the original paper.

The code here contains the implementation of the original authors' RHHH and 10-RHHH algorithms, and our parsing and plotting scripts.
For the algorithms we compared to (Partial Ancestry and Full Ancestry), please refer to Thomas Steinke's implementation (http://people.seas.harvard.edu/~tsteinke/hhh/).

## Reproducing Figures 2, 3 and 4

1. Run `make all` in the top level directory to compile all the executables.
2. Navigate to the folder named after the trace that you want to run it on. For example, the `chicago2015/` folder will reproduce results using anonymized packet trace data collected in Chicago in 2015. 
3. Note that you'll need CAIDA credentials (http://www.caida.org/data/passive/passive_dataset_request.xml) in order to download the packet traces. Once you've received them, type in your shell `export CAIDA_USERNAME=[your username] && export CAIDA_PASSWORD=[your password]`.
4. Run the "error_experiments" script. It'll produce two files: trace_chicago2015_10RandHHH2D_output.txt and trace_chicago2015_RandHHH2D_output.txt, corresponding to 10-RHHH and RHHH, respectively.
5. Run `python plot_graph.py` to produce accuracy error rate (Figure 2), coverage error rate (Figure 3) and false positives rate (Figure 4) graphs.

## Reproducing Figure 5
Make sure that your CAIDA crendentials have been set as env variables.

If you want to start from scratch:
1. `cd figure5`
2. `bash runme`
3. `vepstime.png` is the resulting plot

If you want to run it with data already collected from the Chicago2016 trace:
1. Run `python make_plot.py`

## Using our implementation of RHHH and 10RHHH
We implemented our own versions of RHHH and 10RHHH (for 1D bytes) using the pseudocode in their paper. Follow these steps to make plots using our own implementations.
1. `make all` in the top level directory
2. Navigate to the trace folder, eg `chicago2016`
3. Run `error_experiment_repro.sh` to run it with our binaries (repro_RandHHH and repro_10RandHHH)
4. Open `plot_graph.py` in an editor and change the filename for rhhh_results to `trace_chicago2015_repro_RandHHH_output.txt` and 10_rhhh_results to `trace_chicago2015_repro_10RandHHH_output.txt`
5. `python plot_graph.py`
