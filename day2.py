import unittest

class Test(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_find_occur(self):
        self.assertEqual(find_occur('abcdef'), (False, False))
        self.assertEqual(find_occur('bababc'), (True, True))
        self.assertEqual(find_occur('abbcde'), (True, False))

    def test_how_diff(self):
        self.assertEqual(how_diff('', ''), (0, ''))
        self.assertEqual(how_diff('a', 'a'), (0, 'a'))
        self.assertEqual(how_diff('a', 'b'), (1, ''))
        self.assertEqual(how_diff('fghij', 'fguij'), (1, 'fgij'))
        self.assertEqual(how_diff('abcde', 'axcye'), (2, 'ace'))
    
    def test5(self):
        self.assertEqual(part_2(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']), 'fgij')

def find_occur(input):
    occur = {}
    for letter in input:
        if letter in occur:
            occur[letter] += 1
        else:
            occur[letter] = 1
    twice = False
    thrice = False
    for x in occur.items():
        if twice and thrice:
            break
        if x[1] == 2:
            twice = True
        elif x[1] == 3:
            thrice = True
    return twice, thrice

def how_diff(w1, w2):
    diff_count = 0
    non_diff_letters = ''
    for i, l in enumerate(w1):
        if l != w2[i]:
            diff_count += 1
        else:
            non_diff_letters += l
    return diff_count, non_diff_letters

def part_1(inputs):
    twice_count = 0
    thrice_count = 0
    for input in inputs:
        twice, thrice = find_occur(input)
        if twice: twice_count += 1
        if thrice: thrice_count += 1
    return twice_count * thrice_count

def part_2(inputs):
    for i, input in enumerate(inputs):
        for input2 in inputs[i+1:]:
            diff = how_diff(input, input2)
            if diff[0] == 1:
                return diff[1]

if __name__ == '__main__':
    # unittest.main()

    with open('day2_inputs.txt', 'r') as f:
        inputs = f.read().split('\n')

        out = part_1(inputs)
        print 'checksum is', 'not found' if out is None else out

        out = part_2(inputs)
        print 'diff letters are', 'not found' if out is None else out
