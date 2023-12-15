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

    args = parser.parse_args()

    # Load data from the input file
    data = np.loadtxt(args.infile)

    # Calculate mean and standard deviation
    mean = np.mean(data)
    std = np.std(data)

    # Shift data to have a mean of 0 and scale to have a standard deviation of 1
    processed = (data - mean) / std

    # Save the processed output to the specified output file
    np.savetxt(args.outfile, processed)
