import util
import json
with open("src/test.json","r") as f:
    dict=json.load(f)
story=util.Story(dict,True)
story.start()