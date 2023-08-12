import json

with open ("emojis.json") as f :
    data = json.load(f)

for emoji in data["faces"]:
    print(emoji["unicodeName"])

