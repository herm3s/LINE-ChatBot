# -*- coding: utf-8 -*-

"""
This is the file place to setting the application before you try to run it!
"""

class Settings:
	def __init__(self):
		# -> Main setting.
		# Your authentication token.
		self.AUTH_TOKEN = "r0AE+qmwBHCFStfXuZIaO8HzNHnF2eJ3O4zOQIzzAqJ1nmEV1XJXnmbP++ei7yRQBujrR48im+iuMUD7kGyOagWaDhQwq2TIuOqR2UIW+L6EoSHC2VGxAFnm4syPBpDhWitZM0FSe249Z1EN3xxqMgdB04t89/1O/w1cDnyilFU=" 
		
		# -> Youtube video downloader setting.
		# Integrate with your site url + the path for saving the downloaded videos.
		self.SITE_URL = "http://yoursite.com/DIRECTORY" #your address site to see the saved videos, eg: http://site.com/videos/.
		self.SITE_PATH = "YOUR_PATH" #path/directory to save the videos, eg: /home/user/public_html/videos/.
		
		# -> Welcome Message when you are accepted the invite groups.
		self.WELCOME_MESSAGE = '\
		สวัสดี ประชาชน ลุงตู่มาแว้ว'
		
		# -> Auto reply setting.
		# Replacing "simi" words to another words.
		self.REPLACEMENT_CALL = "Mbot Jinak"

		# -> Not Important setting.
		# Have another account? you can set it for your secondary account, it will called you/the others account as a boss.
		self.HERE_IAM_YOUR_BOSS = "0xffa" 
