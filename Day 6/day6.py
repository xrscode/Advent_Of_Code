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
            
            current = chars[chars.index(char)]
            recorded_positions.append(pos.copy())  # Append a copy of `pos`
            



            while 0 < pos['y'] < len(data) - 1 and 0 < pos['x'] < len(row):
                # UP:
                if current == '^':
                   
                    # Next position: x + 0, y - 1:
                    new_y = pos['y'] - 1
                    # Check:
                    if data[new_y][pos['x']] == '#':
                        
                        current = '>'
                       
                    else:
                        pos['y'] = new_y
                       
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                
                
                
                # RIGHT
                if current == '>':
                   
                    # Next position:  x + 1, y + 0
                    new_x = pos['x'] + 1
                    # Check:
                    if data[pos['y']][new_x] == '#':
                       
                        current = 'v'
                       
                    else:
                        pos['x'] = new_x
                       
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                
                
                
                # DOWN
                if current == 'v':
                   
                    # Next position:  x + 0, y + 1
                    new_y = pos['y'] + 1
                    # Check:
                    if data[new_y][pos['x']] == '#':
                        
                        current = '<'
                      
                    else:
                        pos['y'] = new_y
                       
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`
                
                
                
                # LEFT
                if current == '<':
                   
                    # Next position:  x -1 1, y - 1
                    new_x = pos['x'] - 1
                    # Check:
                    if data[pos['y']][new_x] == '#':
                       
                        current = '^'
                       
                    else:
                        pos['x'] = new_x
                       
                        if pos not in recorded_positions:
                            recorded_positions.append(pos.copy())  # Append a copy of `pos`

            
print('Total count is: ', len(recorded_positions))
                





  