#!/usr/bin/env python3
# coding=<utf-8>

import unittest
from coder import Coder


class TestCoder(unittest.TestCase):
    def test_base64_decode(self):
        test_string = ('aHR0cHM6Ly93d3cueW91dHViZS'
                       '5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==')
        test_value = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        self.assertEqual(Coder().base64_decode(test_string), test_value)

    def test_base64_encode(self):
        test_string = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        test_value = ('aHR0cHM6Ly93d3cueW91dHViZS'
                      '5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==')
        self.assertEqual(Coder().base64_encode(test_string), test_value)

    def test_url_decode(self):
        test_string = ('https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%80%D0%'
                       'B8%D0%BB%D0%BB%D0%B8%D1%86%D0%B0')
        test_value = 'https://ru.wikipedia.org/wiki/Кириллица'
        self.assertEqual(Coder().url_decode(test_string), test_value)

    def test_url_encode(self):
        test_string = 'https://ru.wikipedia.org/wiki/Кириллица'
        test_value = ('https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%80%D0%'
                      'B8%D0%BB%D0%BB%D0%B8%D1%86%D0%B0')
        self.assertEqual(Coder().url_encode(test_string), test_value)

    def test_image_base64_encode(self):
        image = 'One_black_Pixel.png'
        test_value = ('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAAXNSR0I'
                      'Ars4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqG'
                      'QAAAAMSURBVBhXY2BgYAAAAAQAAVzN/2kAAAAASUVORK5CYII=')
        self.assertEqual(Coder().image_base64_encode(image), test_value)


if __name__ == '__main__':
    unittest.main()
