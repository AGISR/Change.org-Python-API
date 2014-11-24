import requests
import exceptions as apiExceptions
import os

class Api(object):
	"""
	This is the main Change.org API object, which encapsulates API methods
	"""
	def __init__(self, **args):
		"""
		Create a new Api object.
		Params:
			args: {dict} Dictionary of arugments, with key 'key', containing the change.org
				API key
		Raises:
			Exception:
		"""
		if len(args) > 0:
			try:
				self.__KEY = args['key']
			except:
				raise apiExcceptions.ApiInitializationError()
		else:
			key = os.environ.get('CHANGE_ORG_API_KEY')
			if key is not None:
				self.__KEY = key
			else:
				raise apiExceptions.ApiInitializationError()