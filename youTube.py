#Class to retrieve information from YouTube using Google's API
import urllib.request
import json
import time

class YouTube:
	def __init__(self,Youtube_Channel_ID,Google_API_key):
		self.channel_id = Youtube_Channel_ID
		self.APIkey = Google_API_key

	#Retrieving the total number of views the channel has
	def get_view_count(self):
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+self.channel_id+"&key="+self.APIkey).read()
		views = json.loads(data)["items"][0]["statistics"]["viewCount"]
		result = "You have " +views+ " views"
		return result

	#Retrieving the total number of subscribers the channel has 
	def get_sub_count(self):
		data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+self.channel_id+"&key="+self.APIkey).read()
		subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
		result = "You have " +subs+ " subscribers"
		return result
