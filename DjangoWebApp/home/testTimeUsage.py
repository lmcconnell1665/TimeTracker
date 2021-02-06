# home/testTimeUsage.py

from django.test import TestCase
from home.models import timeUsage

class PostTestCase(TestCase):
    def testPost(self):
        post = timeUsage(   
                        id=1, 
                        activity="Meeting", 
                        startTime="2021-02-01 20:44:46-05",
                        endTime='2021-02-02 20:44:46-05',
                        duration='00:00:01',
                        note='This is a test activity',
                        tag='Client')

        self.assertEqual(post.id, 1)
        self.assertEqual(post.activity, "Meeting")
        self.assertEqual(post.startTime, "2021-02-01 20:44:46-05")
        self.assertEqual(post.endTime, "2021-02-02 20:44:46-05")
        self.assertEqual(post.duration, "00:00:01")
        self.assertEqual(post.note, "This is a test activity")
        self.assertEqual(post.tag, "Client")