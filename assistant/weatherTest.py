#!/usr/bin/env python
import sys
from weather import Weather
weather = Weather()

location = weather.lookup_by_location(sys.argv[1])
condition = location.forecast()[0]

print condition['text'] + ' with high of ' + condition['high'] + ' and low of ' + condition['low']


