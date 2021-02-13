import os
import json
from json import load

bookmarks_file = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Bookmarks'

def bookmarks():
	
	filename = "./Output/bookmarks.json"
	os.makedirs(os.path.dirname(filename), exist_ok=True)
	
	with open(bookmarks_file, encoding="utf8") as bookmarks:
		data = json.load(bookmarks)

	with open(filename, "w", encoding="utf8") as f:
		f.write(json.dumps(data['roots']))
