""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")
    parser.add_argument("infile", help="Input filename for the data file that needs to be processed.")
    parser.add_argument("outfile", help="Output filename.")

    args_file = parser.parse_args()
    data_main = np.loadtxt(args_file.infile)
    mean_dt = np.mean(data_main)
    std_dt = np.std(data_main)
    processed = (data_main - mean_dt) / std_dt
    np.savetxt(args.outfile, processed)
