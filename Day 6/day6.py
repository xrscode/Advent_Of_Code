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


pos = {'x': 0, 'y': 0}
chars = ['<', '>', 'v', '^']


# count = 0

# recorded_positions = []

# for y, row in enumerate(data):
#     for x, char in enumerate(row):
#         if char in  chars:
#             pos['x'] = x
#             pos['y'] = y
            
#             current = chars[chars.index(char)]
#             recorded_positions.append(pos.copy())  # Append a copy of `pos`
            
#             while 0 < pos['y'] < len(data) - 1 and 0 < pos['x'] < len(row):
#                 # UP:
#                 if current == '^':
                   
#                     # Next position: x + 0, y - 1:
#                     new_y = pos['y'] - 1
#                     # Check:
#                     if data[new_y][pos['x']] == '#':
                        
#                         current = '>'
                       
#                     else:
#                         pos['y'] = new_y
                       
#                         if pos not in recorded_positions:
#                             recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                
                
                
#                 # RIGHT
#                 if current == '>':
                   
#                     # Next position:  x + 1, y + 0
#                     new_x = pos['x'] + 1
#                     # Check:
#                     if data[pos['y']][new_x] == '#':
                       
#                         current = 'v'
                       
#                     else:
#                         pos['x'] = new_x
                       
#                         if pos not in recorded_positions:
#                             recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                
                
                
#                 # DOWN
#                 if current == 'v':
                   
#                     # Next position:  x + 0, y + 1
#                     new_y = pos['y'] + 1
#                     # Check:
#                     if data[new_y][pos['x']] == '#':
                        
#                         current = '<'
                      
#                     else:
#                         pos['y'] = new_y
                       
#                         if pos not in recorded_positions:
#                             recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                
                
#                 # LEFT
#                 if current == '<':
                   
#                     # Next position:  x -1 1, y - 1
#                     new_x = pos['x'] - 1
#                     # Check:
#                     if data[pos['y']][new_x] == '#':
                       
#                         current = '^'
                       
#                     else:
#                         pos['x'] = new_x
                       
#                         if pos not in recorded_positions:
#                             recorded_positions.append(pos.copy())  # Append a copy of `pos`

            


# pos_arr = []
# # First establish current positions of hashtags: 
# for y, row in enumerate(data):
#     for x, char in enumerate(row):
#         if char == '#':
#             pos = [x, y]
#             pos_arr.append(pos)


# # Function to generate possible possitions of left to right:
# def left_to_right(xy):
#     """
#     This function will generate an array that contains, 
#     all possible positions compatible with the co-ordinate
#     given.  It checks all possible positions moving in a left
#     to right direction.  It takes into account the right
#     boundary.
#     """
#     r_positions = []
#     # Look at all possible left to right positions:
#     # Establish Right Boundary:
#     rboundary = len(data[0])
#     # Return empty array if already at final position:
#     if xy[0] == rboundary:
#         return []
#     else:
#         # Generate all possible positions:
#         for i in range(xy[0] + 1, rboundary):
#             r_positions.append([i, xy[1]+1])
#         return r_positions

# def top_to_bottom(xy):
#     """
#     This function will generate an array that contains,
#     all possible possibitons compatible with the co-ordinate given. 
#     The positions checked will move from 'top to bottom'. 
#     It will take into account the boundary which is the final row
#     in data.
#     """
#     t_b_positions = []
#     bboundary = len(data)
    
#     if xy[1] == bboundary:
#         return []
#     else:
#         for i in range(xy[1] + 1, bboundary):
#             t_b_positions.append([xy[0] - 1, i])
#         return t_b_positions

# def right_to_left(xy):
#     rl_positions = []
#     left_boundary = 0
#     if xy[0] == left_boundary:
#         return []
#     else:
#         for i in range(0, xy[0]):
#             rl_positions.append([i, xy[1]])
#     return rl_positions


# def bottom_to_top(xy):
#     print('Starting positino is, ', xy)
#     pos = []
#     if xy[1] == 0:
#         return []
#     else:
#         for i in range(0, xy[1]):
#             a = [xy[0], i]
#             pos.append(a)
#     print(pos)
#     return pos

    
# for x in pos_arr[0]:
#     l_r = left_to_right(x)
#     t_b = top_to_bottom(x)
#     r_l = right_to_left(x)
#     b_t = bottom_to_top(x)
for line in data:
    print(line)

def block(data):
    recorded_positions = []
    block = []
    block_flag = 0
    new_block = []

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char in  chars:
                pos['x'] = x
                pos['y'] = y
                
                current = chars[chars.index(char)]
                recorded_positions.append(pos.copy())  # Append a copy of `pos`

                while 0 < pos['y'] < len(data) - 1 and 0 < pos['x'] < len(row):
                    # Check that 3 blocks have been encountered:
                    # If they have, then an obstacle could be placed.
                    if len(block) > 2:
                        if current == '<':
                            # If moving in left direction after third block:
                            x = block[len(block)- 3][0] - 1
                            y = block[len(block) - 1][1] - 1
                            potential_blocker = [x, y]
                            
                            # Check that potential_blocker can be placed.
                            if 0 < y < len(data) - 1 and 0 < x < len(row) and data[y][x] != '#':
                                if potential_blocker not in new_block:
                                    new_block.append(potential_blocker)
                               
                                
                        if current == 'v':
                                # If moving in down direction after third block:
                            x = block[len(block)-1][0] - 1
                            y = block[len(block)-3][1] + 1
                            potential_blocker = [x, y]
                            
                            # Check that potential_blocker can be placed.
                            if 0 < y < len(data) - 1 and 0 < x < len(row) and data[y][x] != '#':
                                if potential_blocker not in new_block:
                                    new_block.append(potential_blocker)
                               
                        
                        
                        if current == '>':
                            # If moving in down direction after third block:
                            x = block[len(block)-3][0] + 1
                            y = block[len(block)-1][1] - 1
                            potential_blocker = [x, y]
                            # Check that potential_blocker can be placed.
                            if 0 < y < len(data) - 1 and 0 < x < len(row) and data[y][x] != '#':
                                if potential_blocker not in new_block:
                                    new_block.append(potential_blocker)
                        
                        
                        if current == '^':
                            
                            # If moving in up direction after third block:
                            x = block[len(block)-1][0] + 1
                            y = block[len(block)-3][1] - 1
                            potential_blocker = [x, y]
                            # Check that potential_blocker can be placed.
                            if 0 < y < len(data) - 1 and 0 < x < len(row) and data[y][x] != '#' :
                                if potential_blocker not in new_block:
                                    new_block.append(potential_blocker)
                                
                       
                        
                    
                    
                    # UP:
                    if current == '^':
                        # Next position: x + 0, y - 1:
                        new_y = pos['y'] - 1
                        x = pos['x']
                        y = new_y
                        # Check:
                        if data[new_y][pos['x']] == '#':
                            block.append([x, y])
                            current = '>'
                            block_flag += 1
                        else:
                            pos['y'] = new_y
                            if pos not in recorded_positions:
                                recorded_positions.append(pos.copy())  # Append a copy of `pos`
                    
                    
                    
                    
                    # RIGHT
                    if current == '>':
                        # Next position:  x + 1, y + 0
                        new_x = pos['x'] + 1
                        x = new_x
                        y = pos['y']
                        # Check:
                        if data[pos['y']][new_x] == '#':
                            block_flag += 1
                            block.append([x, y])
                            current = 'v'
                        else:
                            pos['x'] = new_x
                            if pos not in recorded_positions:
                                recorded_positions.append(pos.copy())  # Append a copy of `pos`
                    
                    
                    
                    
                    # DOWN
                    if current == 'v':
                        # Next position:  x + 0, y + 1
                        new_y = pos['y'] + 1
                        x = pos['x']
                        y = new_y
                        # Check:
                        if data[new_y][pos['x']] == '#':
                            block.append([x, y])
                            block_flag += 1
                            current = '<'
                        else:
                            pos['y'] = new_y
                            if pos not in recorded_positions:
                                recorded_positions.append(pos.copy())  # Append a copy of `pos`
                    
                    
                    
                    # LEFT
                    if current == '<':
                        # Next position:  x -1 1, y - 1
                        new_x = pos['x'] - 1
                        x = new_x
                        y = pos['y']
                        # Check:
                        if data[pos['y']][new_x] == '#':
                            [[new_x, pos['y']]]
                            block_flag += 1
                            block.append([x, y])
                            current = '^'
                        else:
                            pos['x'] = new_x
                            if pos not in recorded_positions:
                                recorded_positions.append(pos.copy())  # Append a copy of `pos`
       
    
    print(new_block)
    return len(new_block)

print(block(data))
# 156 too low.

# For Sample blocks at:
"""
Option one: [3, 6] - Confirmed.

[9, 5] - DOES NOT WORK

Option two: [6, 7] - Confirmed. 

Option four: [1, 8] - Confirmed.

[8, 3]

Option three: [7, 7] - Confirmed.
"""

[7, 9 ]
[3, 8]