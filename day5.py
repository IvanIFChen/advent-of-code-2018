from collections import defaultdict

def main(inputs):
    is_opp = lambda a, b: (a.isupper() and b == a.lower()) or (a.islower() and b == a.upper())
    stack = []
    for input in inputs:
        # check if there's a reaction
        if stack and is_opp(input, stack[-1]):
            stack.pop()
        else:
            stack.append(input)
    return len(stack)

def part2(inputs):
    import string
    import re

    diff_inputs = lambda l, inputs: re.sub('[{}{}]'.format(l, l.upper()), '', inputs)

    return min([main(diff_inputs(l, inputs)) for l in string.ascii_lowercase])

if __name__ == '__main__':

    with open('day5_inputs.txt', 'r') as f:
        inputs = f.read()
        print 'part 1: {}'.format(main(inputs))
        print 'part 2: {}'.format(part2(inputs))
        
