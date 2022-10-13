import re

text = "I only want to return https://zoom.us/j/room_number."
match = re.search("https://zoom.us/j/", text)

if match is not None:
    print(match.group(0))