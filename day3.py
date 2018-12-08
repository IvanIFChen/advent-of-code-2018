import unittest

class Test(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_parser(self):
        self.assertEqual(parser('#1 @ 82,901: 26x12'), (1, 82, 901, 26, 12))

    def test_calc_points(self):
        self.assertEqual(calc_points(0, 0, 0, 0), [])
        self.assertEqual(calc_points(0, 0, 1, 1), [(0, 0)])
        self.assertEqual(calc_points(0, 0, 2, 1), [(0, 0), (1, 0)])
        self.assertEqual(calc_points(0, 0, 2, 3), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])


def main(inputs):
    total_points = set([])
    overlapped_points = set([])

    for input in inputs:
        id, x, y, width, height = parser(input)
        for point in calc_points(x, y, width, height):
            if point in total_points:
                overlapped_points.add(point)
            else:
                total_points.add(point)
    
    found_id = -1
    # now that overlapped_points are populated, we can now iterate through all of them again to find an id with no overlapped points
    for input in inputs:
        id, x, y, width, height = parser(input)
        points = calc_points(x, y, width, height)
        num_overlap = 0
        for i, point in enumerate(points):
            if point in overlapped_points:
                num_overlap += 1
            if i == len(points)-1:
                # last element, check if this is THE ONE (does not have any overlap with anything else)
                if num_overlap == 0:
                    found_id = id
    return len(overlapped_points), found_id

def parser(input):
    import re
    r = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', input)
    id, x, y, width, height = (int(r.group(i)) for i in range(1, 6))
    return id, x, y, width, height

def calc_points(x, y, width, height):
    points = []
    for pos_x in range(x, x+width):
        for pos_y in range(y, y+height):
            points.append((pos_x, pos_y))
    return points

if __name__ == '__main__':
    # unittest.main()

    with open('day3_inputs.txt', 'r') as f:
        inputs = f.read().split('\n')

        num_overlap, found_id = main(inputs)
        print 'num of overlap is', 'not found' if num_overlap is None else num_overlap
        print 'id of square does not overlap with anyone else is', 'not found' if found_id is None else found_id
        
