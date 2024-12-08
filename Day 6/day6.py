sample = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
data = [row for row in sample.split('\n')]

# for line in data:
#     print(line)

pos = {'x': 0, 'y': 0}

chars = ['^', '>', 'v', '<']
current = ''

count = 0

recorded_positions = []

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char in  chars:
            pos['x'] = x
            pos['y'] = y
            print(f'Character found at co-ordinates: {pos}')
            current = chars[chars.index(char)]
            recorded_positions.append(pos)
            # pos moving:
            while 0 < pos['y'] < len(data) - 1 and 0 < pos['x'] < len(row):
                # UP:
                if current == '^':
                    print(recorded_positions)
                    # Next position: x + 0, y - 1:
                    new_y = pos['y'] - 1
                    # Check:
                    if data[new_y][pos['x']] == '#':
                        print('Block found!  Turning right!')
                        current = '>'
                        print(f'Current position is {pos}, Current character is: {current}')
                    else:
                        print('Moving forward!')
                        pos['y'] = new_y
                        count += 1
                    
                if current == '>':
                    print(recorded_positions)
                    # Next position:  x + 1, y + 0
                    new_x = pos['x'] + 1
                    # Check:
                    if data[pos['y']][new_x] == '#':
                        print('Block found!  Turning right!')
                        current = 'v'
                        print(f'Current position is {pos}, Current character is: {current}')
                    else:
                        count += 1
                        print('Moving forward!')
                        pos['x'] = new_x
                if current == 'v':
                    print(recorded_positions)
                    # Next position:  x + 0, y + 1
                    new_y = pos['y'] + 1
                    # Check:
                    if data[new_y][pos['x']] == '#':
                        print('Block found!  Turning right!')
                        current = '<'
                        print(f'Current position is {pos}, Current character is: {current}')
                    else:
                        count += 1
                        print('Moving forward!')
                        pos['y'] = new_y
                if current == '<':
                    print(recorded_positions)
                    # Next position:  x -1 1, y - 1
                    new_x = pos['x'] - 1
                    # Check:
                    if data[pos['y']][new_x] == '#':
                        print('Block found!  Turning right!')
                        current = '^'
                        print(f'Current position is {pos}, Current character is: {current}')
                    else:
                        count += 1
                        print('Moving forward!')
                        pos['x'] = new_x
            print('Total count is: ', count)
                





  