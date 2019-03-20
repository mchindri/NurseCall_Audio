import logging, sys

logging.basicConfig(stream = sys.stderr, level = logging.DEBUG)

DEBUG = 0

if DEBUG == 1:
	def P(x):
		logging.debug(x)
else:
	def P(x):
		a = x
