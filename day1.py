import unittest

class Test(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test1(self):
        self.assertEqual(main(['+1', '-1']), 0)
    
    def test2(self):
        self.assertEqual(main(['+3', '+3', '+4', '-2', '-4']), 10)
    
    def test3(self):
        self.assertEqual(main(['-6', '+3', '+8', '+5', '-6']), 5)
    
    def test4(self):
        self.assertEqual(main(['+7', '+7', '-2', '-7', '-4']), 14)

def main(inputs):
    out = 0
    occur = set([0])
    while True:
        for input in inputs:
            try:
                operator = input[0]
                number = int(input[1:])
                if operator is '-':
                    out -= number
                if operator is '+':
                    out += number
                if out in occur:
                    return out
                else:
                    occur.add(out)
            except:
                continue

if __name__ == '__main__':
    # unittest.main()

    with open('day1_inputs.txt', 'r') as f:
        inputs = f.read().split('\n')
        out = main(inputs)
        print 'first dup is', 'not found' if out is None else out
    