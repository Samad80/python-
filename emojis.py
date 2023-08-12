import json

emojis ='''
{
    "faces":[
        {
        "slug": "grinning-face",
        "character": "😀",
        "unicodeName": "grinning face",
        "codePoint": "1F600",
        "group": "smileys-emotion",
        "subGroup": "face-smiling"
        },
        {
        "slug": "grinning-face-with-big-eyes",
        "character": "😃",
        "unicodeName": "grinning face with big eyes",
        "codePoint": "1F603",
        "group": "smileys-emotion",
        "subGroup": "face-smiling"
        }
    ]
}
'''

data = json.loads(emojis)
print (data)
