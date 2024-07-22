import unittest

import scrape

class TestRSSMethod(unittest.TestCase):
    def test_One(self):
        self.assertEqual(scrape.getrss("https://www.youtube.com/@SawFinMath"),'"https://www.youtube.com/feeds/videos.xml?channel_id=UCcbu9qaBn3MNFYr96mbg72w"')