from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        """Set up test client before each test."""
        self.client = app.test_client()
        app.config['TESTING'] = True
        
        
    def test_homepage(self):
        with self.client as client:
            response = client.get('/')
            self.assertIn('board', session)
            self.assertEqual(response.status_code, 200)
            
            
    def test_check_word(self):
        with self.client as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [['T', 'E', 'S', 'T'], ...]
            response = client.get('/check-word?word=test')
            self.assertEqual(response.json['result'], 'ok')
            
            
    def test_post_score(self):
        with self.client as client:
            response = client.post('/post-score', json={'score': 5})
            self.assertEqual(response.status_code, 200)
            self.assertIn('highscore', session)



