"""
Note: All of these tests require that the API key and Secret be specified as environment
variables with the keys CHANGE_ORG_API_KEY and CHANGE_ORG_API_SECRET respectively
"""

import pytest
import change_org as c
import json

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

def testGetSinglePetitionById():
	"""
	Test to see if getting pettition details for a single petition by ID works correctly.
	The petition to be tested will be the same one as the test case above (id: 2297756), by
	comparing the response from the API to the actual response.
	Note: Signature count has been removed from comparison as it changes continuously
	"""
	expected_response = """
	{"petition_id":2297566,"title":"The Supreme Court of Missouri: Take the case of Michael Brown, popularly dubbed the 'Ferguson Case', to the Missouri Supreme Court, with Ferguson Officer Darren Wilson as the accused.","status":"open","url":"https://api.change.org/p/the-supreme-court-of-missouri-take-the-case-of-michael-brown-popularly-dubbed-the-ferguson-case-to-the-missouri-supreme-court-with-ferguson-officer-darren-wilson-as-the-accused","overview":"<p>The case of Michael Brown, more often known as the 'Ferguson Case', has received national attention since Michael Brown was shot at least six times, including twice in the head, by Ferguson Officer Darren Wilson. Multiple eyewitness accounts, as well as video footage, contradict statements released by the Ferguson Police Department claiming that the murder was justified. Many media accounts attempted to paint Michael Brown as a 'thug' as a way to justify his murder- Michael Brown was an 18 year old Black boy. This case was brought to the Ferguson Grand Jury, and it was reported on Monday, November 24th, that there would be no indictment of Darren Wilson. Darren Wilson's escaping of indictment, despite the fact that he murdered a teenager, was unjustly decided. This case must be brought to a higher level of court, where a higher level of justice can be fought for.</p>","targets":[{"name":"The Supreme Court of Missouri","type":"custom"}],"letter_body":"Take the case of Michael Brown, popularly dubbed the 'Ferguson Case', to the Missouri Supreme Court, with Ferguson Officer Darren Wilson as the accused.","signature_count":156301,"image_url":"//d22r54gnmuhwmk.cloudfront.net/photos/8/ay/qo/xXaYqoNsmxVzgab-556x313-cropped.jpg","category":"Criminal Justice","goal":200000,"created_at":"2014-11-25T02:37:07Z","end_at":"2015-11-25T23:59:59Z","creator_name":"Katherine Na","creator_url":"https://api.change.org/u/186820136","organization_name":null,"organization_url":null}
	"""
	converted_expected = json.loads(expected_response)
	converted_expected.pop('signature_count', None)
	api = c.Api()
	output = api.getSinglePetitionById(2297566)
	output.pop('signature_count', None)
	assert converted_expected == output