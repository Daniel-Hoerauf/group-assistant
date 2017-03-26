#!/usr/bin/env python
import sys
from weather import Weather

def main(args):
	print args
	# weather = Weather()

	# location = weather.lookup_by_location(args[1])
	# condition = location.forecast()[0]

	# if condition:
	# 	return condition['text'] + ' with high of ' + condition['high'] + ' and low of ' + condition['low']
	# else:
	# 	return "City not found. It's probably raining meatballs. Please try again."

if __name__ == '__main__':
    main(sys.argv)