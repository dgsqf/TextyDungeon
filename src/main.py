import util
import json
import argparse
parser = argparse.ArgumentParser(description='start an adventure')
parser.add_argument('file', type=str,
                    help='path to json file')

args = parser.parse_args()
try:
    with open(args.file, "r") as f:
        dict = json.load(f)
    story = util.Story(dict, False)
    story.start()
except FileNotFoundError:
    print("file not found error please enter in an existing file")
