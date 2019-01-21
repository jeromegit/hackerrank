import unittest

def print_rangoli(size):
    width  = ((size-1)*2*2)+1
    height = (size*2)-1
    # Create a line with all letters needed for the size
    # and make it into an list
    letters = list([chr(c) for c in range(ord('a'), ord('a')+size + 1)])

    # Initialize the 2D matrix with '-'
    matrix = [['-']*width for i in range(height)]

    # Start in the middle of the matrix and propagate like a wave in a pond
    middleRow = size-1
    middleCol = (size-1)*2
    for row in range(0, size):
        middle = 0
        for letterIndex in range(row, size): # note the row as starting value for the range
            letter  = letters[letterIndex]
            # Populate the letter into the 4 quadrants SW, SE, NW, NE
            matrix[middleRow + row][middleCol + middle*2] = letter
            matrix[middleRow + row][middleCol - middle*2] = letter

            matrix[middleRow - row][middleCol + middle*2] = letter
            matrix[middleRow - row][middleCol - middle*2] = letter

            middle += 1

    result = ''
    for row in matrix:
        result += ''.join(row)+"\n"

    return result

# Test cases
class RangoliTest(unittest.TestCase):
    def test_with_1(self):
        self.assertEqual(print_rangoli(1), "a\n")

    def test_with_2(self):
        self.assertEqual(print_rangoli(2),
"""
--b--
b-a-b
--b--
""".lstrip())

    def test_with_3(self):
        self.assertEqual(print_rangoli(3),
"""
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
""".lstrip())

    def test_with_4(self):
        self.assertEqual(print_rangoli(4),
"""
------d------
----d-c-d----
--d-c-b-c-d--
d-c-b-a-b-c-d
--d-c-b-c-d--
----d-c-d----
------d------
""".lstrip())
        
if __name__ == '__main__':
    unittest.main()
