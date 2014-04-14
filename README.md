uploadFlickr
============

Take a screenshot and upload to flickr, very naive
and very simple, no options, no arguments, just download
the python script, fill in the api key and secret,
and run. It will take a screenshot
and save it as a temporary file, then upload to flickr.

#Prerequsites:
1. You need a api key and api secret, google for "flickr api key".
2. You need the flickrapi python package, install it by

		sudo pip install flickrapi

3. Edit the python script and fill in line 11 and 12:

		api_key = ""
		api_secret = ""

