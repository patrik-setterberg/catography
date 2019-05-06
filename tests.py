from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User

TEST_USER = 'kharjo'
TEST_PASSWORD = 'meatball'
WRONG_PASSWORD = 'pasta'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username=TEST_USER)
        u.set_password(TEST_PASSWORD)
        self.assertFalse(u.check_password(WRONG_PASSWORD))
        self.assertTrue(u.check_password(TEST_PASSWORD))

if __name__ == '__main__':
    unittest.main(verbosity=2)
