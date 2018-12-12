from collections import defaultdict

def main(inputs):
    inputs.sort(key=lambda x: parser(x)[0])

    sleep_count = defaultdict(int)
    sleep_times = defaultdict(int)
    curr_guard = None
    asleep_on = None

    for input in inputs:
        date, action, id = parser(input)

        if id is not '':
            curr_guard = id
        else:
            if action == 'falls':
                asleep_on = date.minute
            elif action == 'wakes':
                sleep_count[curr_guard] += date.minute - asleep_on
                for i in range(asleep_on, date.minute):
                    sleep_times['{}_{}'.format(curr_guard, i)] += 1
                asleep_on = None
            else:
                raise Exception('Invalid action: {}'.format(action))

    # finding the guad the slept the most

    top_id = None
    max_count = -1

    for id, value in sleep_count.items():
        if value > max_count:
            top_id, max_count = id, value

    # finding the minute that the guard slept the most

    top_minute = None
    max_count = -1

    for key, value in sleep_times.items():
        id, minute = key.split('_')
        if id == top_id and value > max_count:
            top_minute, max_count = minute, value

    print 'part 1: {}'.format(int(top_id) * int(top_minute))

    # (part 2) Of all guards, which guard is most frequently asleep on the same minute?

    top = (None, None)
    max_count = -1
    
    for guard_minute, sleep_count in sleep_times.items():
        guard_id, minute = guard_minute.split('_')
        if sleep_count > max_count:
            top = (guard_id, minute)
            max_count = sleep_count
    print 'part 2: {}'.format(int(top[0]) * int(top[1]))


def parser(input):
    import re
    from datetime import datetime
    r = re.findall(r'\[(.+)\] (\w+) #?(\d+)?', input)
    date, action, id = (x for x in r[0])
    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    return date, action, id

if __name__ == '__main__':

    with open('day4_inputs.txt', 'r') as f:
        inputs = f.read().split('\n')
        main(inputs)
        
