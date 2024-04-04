import unittest
from classes import YoutubeData

class TestGetVideoStats(unittest.TestCase):

    def test_get_video_stats(self):
        youtubeData = YoutubeData()
        result = youtubeData.get_video_stats("0P1FGtdg8o8")

        if result:
            print(result)
            self.assertEqual(result["status"], "success")
        else:
            raise Exception("Getting video stats failed, result is None")