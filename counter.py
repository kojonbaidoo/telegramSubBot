import urllib.request
import json
import time

class YouTube:
	def __init__(self):
		self.channel_id = "Channel ID goes here"
		self.APIkey = "Google API KEY goes here"

	def get_view_count(self):
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+self.channel_id+"&key="+self.APIkey).read()
		views = json.loads(data)["items"][0]["statistics"]["viewCount"]
		result = "You have " +views+ " views"
		return result

	def get_sub_count(self):
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+self.channel_id+"&key="+self.APIkey).read()
		subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
		result = "You have " +subs+ " subscribers"
		return result
