"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count
import argparse

def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    parser_com = argparse.ArgumentParser(description="This program prints the number of lines in infile.")
    parser_com.add_argument("infile", help="Input file to count lines")
    args_main = parser_com.parse_args()
    main(args_main.infile)
