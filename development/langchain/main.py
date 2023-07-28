# File: main.py

# Imports
import timeit
import argparse



if __name__ == '__main__':
    # Get parser
    parser = argparse.ArgumentParser()

    # Add argument 'input'
    parser.add_argument('input', type = 'str')
    
    # Get argument(s)
    args = parser.parse_args()

    # Start time
    timeit.default_timer()

