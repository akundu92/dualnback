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
        self.assertEqual(core.check_visual([1,1],True,1),1)
        self.assertEqual(core.check_visual([1, 1], None, 1), 2)
        self.assertEqual(core.check_visual([1, 2], True, 1), 3)
        self.assertEqual(core.check_visual([1, 2], None, 1), 4)

        self.assertEqual(core.check_visual([1, 2, 1], True, 2), 1)
        self.assertEqual(core.check_visual([1, 2, 1], None, 2), 2)
        self.assertEqual(core.check_visual([1, 2, 2], True, 2), 3)
        self.assertEqual(core.check_visual([1, 2, 2], None, 2), 4)

        self.assertEqual(core.check_visual([1, 2, 3, 1], True, 3), 1)
        self.assertEqual(core.check_visual([7, 8, 9, 7], None, 3), 2)
        self.assertEqual(core.check_visual([7, 8, 9, 10], True, 3), 3)
        self.assertEqual(core.check_visual([7, 8, 9, 10], None, 3), 4)





    #
    # def check_audio(self):

    #     pass
if __name__=='__main__':
    unittest.main()