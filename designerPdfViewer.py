#!/bin/python3
import unittest

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max = 0;
    aOrd = ord('a');
    for letter in word:
        height = int(h[ord(letter) - aOrd])
        if height > max:
            max = height

    return max * len(word)

# Test cases
class DesignerPdfViewerTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(designerPdfViewer("1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5".split(), "abc"), 9)
    
    def test2(self):
        self.assertEqual(designerPdfViewer("1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7".split(), "zaba"), 28)
    
if __name__ == '__main__':
    unittest.main()
