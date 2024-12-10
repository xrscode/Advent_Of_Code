# Function to access data:
def get_data(location):
    arr = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for i, x in enumerate(d):
            arr.append(x)
    
    return arr

# Read live data:
data = get_data('./data.txt')

# Sample data:
# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...""".split('\n')

chars = ['<', '>', 'v', '^']

def start(arr):
    for y, line in enumerate(arr):
        for x, char in enumerate(line):
            if char in chars:
                starting_position = [x, y]
                starting_direction = arr[y][x]
                return [starting_position, starting_direction]

s = start(data)[0]
d = start(data)[1]

def move(data, start, char):
    pos = {'x': start[0], 'y': start[1]}
    current = char
    recorded_positions = []
    block = []
    recorded_positions.append(pos.copy())
   
#    Iterate through each row of the data:
    for y, row in enumerate(data):
        # Iterate through each element:
        for x, char in enumerate(row):
            # Check that boundary has been respected:
            while 0 < pos['y'] < len(data) - 1 and 0 < pos['x'] < len(row) -1:
                
                # UP:
                if current == '^':
                    # Next position: x + 0, y - 1:
                    x = pos['x']
                    y = pos['y'] - 1
                    # Check:
                    if 0 <= y <= len(data) - 1 and 0 <= x <= len(row) -1 and data[y][x] == '#':
                        if [x, y, current] not in block:
                            block.append([x, y, current])
                            current = '>'
                        else:
                            print('Loop detected')
                            return 'Loop'
                    else:
                        pos['y'] = y
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                # RIGHT
                if current == '>':
                    # Next position:  x + 1, y + 0
                    x = pos['x'] + 1
                    y = pos['y']
                    # Check:
                    if 0 <= y <= len(data) - 1 and 0 <= x <= len(row) -1 and data[y][x] == '#':
                        if [x, y, current] not in block:
                            block.append([x, y, current])
                            current = 'v'
                        else:
                            print('Loop detected')
                            return 'Loop'
                    else:
                        pos['x'] = x
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                # DOWN
                if current == 'v':
                    # Next position:  x + 0, y + 1
                    x = pos['x']
                    y = pos['y'] + 1
                    # Check:
                    if 0 <= y <= len(data) - 1 and 0 <= x <= len(row) -1 and data[y][x] == '#':
                        if [x, y, current] not in block:
                            block.append([x, y, current])
                            current = '<'
                        else:
                            print('Loop detected')
                            return 'Loop'      
                    else:
                        pos['y'] = y
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                # LEFT
                if current == '<':
                    # Next position:  x -1 1, y - 1
                    x = pos['x'] - 1
                    y = pos['y']
                    # Check:
                    if 0 <= y <= len(data) - 1 and 0 <= x <= len(row) -1 and data[y][x] == '#':
                        if [x, y, current] not in block:
                            block.append([x, y, current])
                            current = '^'
                        else:
                            print('Loop detected')
                            return 'Loop'

                    else:
                        pos['x'] = x
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
    return {'Positions': len(recorded_positions), 'Block_Positions': block}

part_one = move(data, s, d)
print('The answer to part one is: ', part_one['Positions'])


new_data = []



# This Code will modify the original data and add a # where possible.
for y, row in enumerate(data):
    for x, col in enumerate(row):
        if data[y][x] != '#' and data[y][x] not in chars:
            # Create a deep copy of `data` to avoid modifying the original
            new_data_entry = [list(row) for row in data]
            # Change the current cell to '#'
            new_data_entry[y][x] = '#'
            # Append the modified copy to `new_data`
            new_data.append(new_data_entry)


# def check(y):
#     print('Checking data:\n')
#     print('X', ['0',   '1',   '2',   '3',   '4',   '5',   '6',   '7',   '8',   '9'])
#     for i, line in enumerate(new_data[y]):
#         print(i, line)
#     print('Result is:\n')
#     print(move(new_data[y], start(data)[0], start(data)[1]))
#     return 1


# loop_flag = 0

# for i, x in enumerate(new_data):
#     print(f'Currently on iteration: {i}/{len(new_data)}.  Loop counter at: ')
#     if move(x, start(data)[0], start(data)[1]) == 'Loop':
#         loop_flag += 1
#     else:
#         continue

# print(loop_flag)

import concurrent.futures

# Assuming `move`, `start`, and other related functions are defined elsewhere
def process_data(index, data, loop_flag_list):
    """Process a single item in `new_data`."""
    print(f'Currently on iteration: {index + 1}/{len(new_data)}')
    if move(data, start(data)[0], start(data)[1]) == 'Loop':
        loop_flag_list[index] = 1
    else:
        loop_flag_list[index] = 0

# Initialize `loop_flag` using a shared list
loop_flag = [0] * len(new_data)

# Use ThreadPoolExecutor for multithreading
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(process_data, i, x, loop_flag) 
        for i, x in enumerate(new_data)
    ]
    # Optionally wait for all futures to complete
    concurrent.futures.wait(futures)

# Summarize results
total_loops = sum(loop_flag)
print(f"Total loops detected: {total_loops}")
