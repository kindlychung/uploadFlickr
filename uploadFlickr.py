#!/usr/bin/python

# requires flickrapi
# install it by:
# sudo pip install flickrapi
import flickrapi
import subprocess
imgfile = "/tmp/scrotout.png"
subprocess.call(["scrot", "-s", imgfile])

api_key = ""
api_secret = ""
flickr = flickrapi.FlickrAPI(api_key, api_secret)
(token, frob) = flickr.get_token_part_one(perms="write")
flickr.get_token_part_two((token, frob))

def func(progress, done):
	if done:
		print "Done uploading"
	else:
		print "At %s%%" % progress

flickr.upload(filename=imgfile, callback=func)
