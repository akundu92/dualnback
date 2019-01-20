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
        self.assertEqual(core.check_visual([1, 1], False, 1), 2)
        self.assertEqual(core.check_visual([1, 2], True, 1), 3)
        self.assertEqual(core.check_visual([1, 2], False, 1), 4)

        self.assertEqual(core.check_visual([1, 2, 1], True, 2), 1)
        self.assertEqual(core.check_visual([1, 2, 1], False, 2), 2)
        self.assertEqual(core.check_visual([1, 2, 2], True, 2), 3)
        self.assertEqual(core.check_visual([1, 2, 2], False, 2), 4)

        self.assertEqual(core.check_visual([1, 2, 3, 1], True, 3), 1)
        self.assertEqual(core.check_visual([7, 8, 9, 7], False, 3), 2)
        self.assertEqual(core.check_visual([7, 8, 9, 10], True, 3), 3)
        self.assertEqual(core.check_visual([7, 8, 9, 10], False, 3), 4)

        self.assertEqual(core.check_visual([1, 2, 3, 4, 1], True, 4), 1)
        self.assertEqual(core.check_visual([7, 8, 9, 4, 7], False, 4), 2)
        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], True, 4), 3)
        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], False, 4), 4)

        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], False, 4), 4)

        self.assertEqual(core.check_visual([1, 1], True, 34), 3)
        self.assertEqual(core.check_visual([1, 1], False, 34), 4)

        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], False, 5), 4)
        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], True, 5), 3)

        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], False, 6), 4)
        self.assertEqual(core.check_visual([7, 8, 9, 10, 2], True, 6), 3)

        self.assertEqual(core.check_visual([7, 8, 9, 10, 7], False, 4), 2)
        self.assertEqual(core.check_visual([7, 8, 9, 10, 7], True, 4), 1)


        with self.assertRaises(TypeError):
            core.check_visual(3, False, 4)

        with self.assertRaises(TypeError):
            core.check_visual([1,2,3], 'dang', 4)

        with self.assertRaises(ValueError):
            core.check_visual([7, 8, 9, 7], False, -1)













    #
    # def check_audio(self):

    #     pass
if __name__=='__main__':
    unittest.main()