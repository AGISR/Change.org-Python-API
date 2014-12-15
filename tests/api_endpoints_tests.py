"""
Note: All of these tests require that the API key and Secret be specified as environment
variables with the keys CHANGE_ORG_API_KEY and CHANGE_ORG_API_SECRET respectively
"""

import pytest
import change_org as c

def testGetPetitionIDEndpoint():
	"""
	Test to see if getting the ID of a petition works.
	The petition at 'https://www.change.org/p/the-supreme-court-of-missouri-take-the-case-of-michael-
	brown-popularly-dubbed-the-ferguson-case-to-the-missouri-supreme-court-with-ferguson-officer-
	darren-wilson-as-the-accused' will be used for this test. The correct response is 2297566.
	"""
	api = c.Api()
	petition_url = 'https://www.change.org/p/the-supreme-court-of-missouri-take-the-case-of-michael-brown-popularly-dubbed-the-ferguson-case-to-the-missouri-supreme-court-with-ferguson-officer-darren-wilson-as-the-accused'
	petition_id = api.getPetitionId(petition_url)
	assert petition_id == 2297566