# coding=utf8

'''
    test the profile module.
'''
import sys, os
from os.path import realpath, dirname
from os.path import join as path_join
sys.path.insert(
    0,
    realpath(path_join(dirname(__file__), '../'))
)

import unittest

from models import Profile
from prphoto import mongo

from bson import ObjectId


class TestProfile(unittest.TestCase):
    fake_user_id = ObjectId()

    def setUp(self):
        mongo.db.users.insert({'_id': self.fake_user_id, 'username': 'foo'})

    def tearDown(self):
        mongo.db.users.remove({'_id': self.fake_user_id})
    
    def testUpdateProfile(self):
        self.assertEqual({}, Profile.update_profile(self.fake_user_id, **{'bla': 'bar'}))


if __name__ == '__main__':
    unittest.main()
