import requests
import os

class Api(object):
	def __init__(self, **args):
		if len(args) > 0:
			try:
				self.__KEY = args['key']
			except:
				self.__raiseException("Invalid initialization parameters. See documentation for more information.")
		else:
			key = os.environ.get('CHANGE_ORG_API_KEY')
			if key is not None:
				self.__KEY = key
			else:
				self.__raiseException("Invalid initialization parameters. See documentation for more information.")

	def __raiseException(self, description):
		raise Exception(description)