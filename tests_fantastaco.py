import os
import unittest
from app import app
from app import decide

class ProjectTests(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	# test loading home page success
	def test_index_page(self):
	    response = self.app.get('/', follow_redirects=True)
	    self.assertEqual(response.status_code, 200)

	# test loading tweets page success
	def test_tweets_page(self):
	    response = self.app.get('/tweets', follow_redirects=True)
	    self.assertEqual(response.status_code, 200)

	# test loading gif page success
	def test_gif_page(self):
		response = self.app.get('/gif', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	# test decide.py random returns index within range
	def test_random_index(self):
		index = decide.random_index()
		self.assertTrue(0 <= index and index < len(decide.decisions))

if __name__ == "__main__":
	unittest.main()