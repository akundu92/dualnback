import unittest
from dualnback import core


class CoreTests(unittest.TestCase):
    def test_visual_generator(self):
        self.assertIn(core.visual_generator(), (1, 2, 3, 4, 5, 6))

    def test_audio_generator(self):
        t = tuple(i for i in range(1, 26))
        self.assertIn(core.audio_generator(), t)
    #
    def test_check_visual(self):
        self.assertEqual(core.check_visual([1,1],True,1))
    #
    # def check_audio(self):
    #     pass
if __name__=='__main__':
    unittest.main()