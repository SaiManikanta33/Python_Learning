        #Command-line Arguments with argparse
    #Instead of asking users for input every time,pass values directly
    #       Trough the terminal
"""import argparse
parser = argparse.ArgumentParser(description="Simaple Calculator")
parser.add_argument("--name",help="Enter your name")
args = parser.parse_args()
print(f"Hello, {args.name}")"""

    #Multiple Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--host")
parser.add_argument("--port",type=int)
args = parser.parse_args()
print(args.host)
print(args.port)