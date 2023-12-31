"""ex_5_0.py"""


def line_count(infile):
    with open(infile, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print(line_count)


if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root
        
    data_directory_main = get_repository_root() / "data"
    line_count(data_directory_main / "ex_5_2-data.csv")
