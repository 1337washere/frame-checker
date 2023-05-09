import argparse
import requests
from termcolor import colored
parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f',
                    help='Specify the path to the file containing URLs',
                    type=str
                    )

args = parser.parse_args()
if args.file:
    with open(args.file, 'r') as f:
        contents = f.read()
        file_as_list = contents.splitlines()
        for line in file_as_list:
            if 'X-Frame-Options' in requests.get(line).headers:
                print(colored(line, " IS SAFE!", "green"))
            else:
                print(colored(line, " IS VULNERABLE!", "red"))
