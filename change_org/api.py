import requests
import exceptions as ex
import os

class Api(object):
	"""
	This is the main Change.org API module, which encapsulates API methods
	"""

	def __init__(self, **kwagrs):
		"""
		Creates a new Api object. The API key and secret are passed through as arguments to this
		constructor, or can alternatively be set as environment variables, CHANGE_ORG_API_KEY
		and CHANGE_ORG_API_SECRET for the API key and secret respectively
		Args:
			kwagrs: {dict} Dictionary of arugments, with keys 'key' and 'secret', containing the change.org API key and secret
		Raises:
			ApiInitializationError: Thrown if API key and secret are not passed through correctly
		"""
		api_key = self.__checkEnvironmentAndDict(kwagrs, 'key', 'CHANGE_ORG_API_KEY')
		api_secret = self.__checkEnvironmentAndDict(kwagrs, 'secret', 'CHANGE_ORG_API_SECRET')
		if api_key.get('exists') and api_secret.get('exists'):
			self.__KEY = api_key.get('value')
			self.__SECRET = api_secret.get('value')
		else:
			raise ex.ApiInitializationError

	def __checkEnvironmentAndDict(self, candidateDict, dictKey, osKey):
		"""
		Function to check if a specific key is present in a dictionary, and if a variable is
		present as an environment variable
		Args:
			candidateDict: {dict} Dictionary in which the key is to be searched for
			dictKey: {str} Key to be searched for in the dictionary
			osKey: {str} Key of desired environment variable
		Returns:
			A dict with keys 'exists' and 'value', where exists is a boolean (true if the value
			exists in either the dictionary or the environment variables or both, false if not) and
			where 'value' is the value retrieved from the dictionary or environment variables for the
			specified keys (if it exists, an empty string is returned if not). Note: if both
			environment and dictionary values are present, the value from the dictionary is returned
		"""
		if dictKey in candidateDict:
			return {'exists': True, 'value': candidateDict.get(candidateDict)}
		else:
			candidateKey = os.environ.get(osKey)
			if candidateKey is not None:
				return {'exists': True, 'value': candidateKey}
			else:
				return {'exists': False, 'value': ''}