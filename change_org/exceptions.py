class ApiValidationError(Exception):
	"""
	Exception class for an error to be thrown fi the API key and/or secret cannot be validated
	with the REST API
	"""
	def __str__(self):
		return 'Could not verify API key and/or API secret'

class ApiInitializationError(Exception):
	"""
	Exception class for an error to be thrown if the API module cannot be initialized
	"""
	def __str__(self):
		return 'Could not initailize change.org API module. Check API key and secret are properly passed through'