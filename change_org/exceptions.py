class ApiValidationError(Exception):
	"""
	Exception class for an error to be thrown fi the API key cannot be validated
	with the REST API
	"""
	def __str__(self):
		return 'Could not verify API token'

class ApiInitializationError(Exception):
	"""
	Exception class for an error to be thrown if the API class cannot be initialized
	correctly.
	"""
	def __str__(self):
		return 'Could not initailize change.org API correctly. Check API key is properly passed through'