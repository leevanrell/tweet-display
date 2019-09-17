#!/usr/bin/env python

import twitter
import serial
import sys
from time import sleep

port = "/dev/ttyS0"
user = '@realDonaldTrump'

def displayTweet(tweet):
	with serial.Serial(port, 115200) as ser:
		ser.write(tweet)


def main():
	# check_tweet = api.GetUserTimeline(screen_name=user)[0].text
	# cur_tweet = ''
	# while True:
	# 	if check_tweet != cur_tweet:
	# 		cur_tweet = check_tweet
	# 		displayTweet(cur_tweet)
	# 	sleep(1)
	displayTweet(str.encode("Hello World"))


if __name__ == "__main__":
	try:
		with open('twitter.key', 'r') as f:
			api_key = f.readline().strip()
			api_secret = f.readline().strip()
			token_key = f.readline().strip()
			token_secret = f.readline().strip()
	except Exception as e:
		print(e)
		sys.exit(1)

	print('test')
	api = twitter.Api(
	    consumer_key=api_key,
	    consumer_secret=api_secret,
	    access_token_key=token_key,
	    access_token_secret=token_secret
	)

	try:
		with serial.Serial(port, 19200) as ser:
			ser.write(b'booting...')
	except Exception as e:
		print(e)
		sys.exit(1)

	try:
		main()
	except KeyboardInterrupt:
		print()
		sys.exit(0)