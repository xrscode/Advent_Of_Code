import itertools
import re

# Function to access data:
def get_data(location):
    arr = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for line in d:
            arr.append(line.strip())
    
    return arr

# Read live data:
data = get_data('./data.txt')

# Read live data:
live_data = get_data('./data.txt')
live_data.reverse()
sample_data = get_data('./sample.txt')
sample_two = get_data('./sample2.txt')

# Diagram to help visualise concept:
for i, line in enumerate(sample_data):
    print(i, line.strip())

def antinode(data):
    # Pattern to match single lowercase or upper case letter or digit.
    pattern = r'^[a-zA-Z0-9]$'

    # Create boundary check function:
    def boundary(x, y):
        # X must be less than length of row:
        if x >= 0 and x <= len(data[0]) - 1:
            # Y must be less than length of data set:
            if y >= 0 and y <= len(data) - 1:
                return True
        return False
    
    # Store found antennaes in location dictionary:
    locations = {}
    antinodes = []

    # Iterate through data to find antennaes:
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            char = data[y][x]

            if re.match(pattern, char):
                if char not in locations:
                    locations[char] = [[x, y]]
                else:
                    locations[char].append([x, y])

    
    # Iterate through atennae locations:
    for antennae in locations:
        # Generate list of all possible combinations:
        combinations = list(itertools.combinations(locations[antennae], 2))

        
       
       # Iterate through pairs of combinations to make comparisons:
        for i, x in enumerate(combinations):

            
            # Establish Antenna Locations:
            ant_1 = [x[0][0], x[0][1]]
            ant_2 = [x[1][0], x[1][1]]
            
            
            # Determine distances:
            x_dis = ant_1[0] - ant_2[0]
            y_dis = ant_1[1] - ant_2[1]
            

            # Determine largest/smallest x value. 
            if x_dis <= 0:
                lrgX = ant_2[0]
                smlX = ant_1[0]
            else:
                lrgX = ant_1[0]
                smlX = ant_2[0]


            # Determine largest/smallest y value.
            if y_dis <= 0:
                lrgY = ant_2[1]
                smlY = ant_1[1]
            else:
                lrgY = ant_1[1]
                smlY = ant_2[1]



            # Make displacement positive if negative.
            x_dis = x_dis if x_dis >= 0 else x_dis * - 1
            y_dis = y_dis if y_dis >= 0 else y_dis * - 1


            
            # Start calculating antinodes:
            # First calculate next x value:
            if ant_1[0] == lrgX:
                v1 = ant_1[0] + x_dis
            else:
                v1 = ant_1[0] - x_dis
            
            # Calculate next y value:
            if ant_1[1] == lrgY:
                v2 = ant_1[1] + y_dis
            else:
                v2 = ant_1[1] - y_dis
            
            if ant_2[0] == lrgX:
                v3 = ant_2[0] + x_dis
            else:
                v3 = ant_2[0] - x_dis
            if ant_2[1] == lrgY:
                v4 = ant_2[1] + y_dis
            else:
                v4 = ant_2[1] - y_dis


            # Find new Antinode values:
            ant_n_one = [v1, v2]
            ant_n_two = [v3, v4]


            # Check that antinodes are within boundary:
            if boundary(ant_n_one[0], ant_n_one[1]) and ant_n_one not in antinodes:
                    antinodes.append(ant_n_one)
            if boundary(ant_n_two[0], ant_n_two[1]) and ant_n_two not in antinodes:
                    antinodes.append(ant_n_two)

            
           
    return len(antinodes)


print(f'The answer to part one is: {antinode(data)}')


string = """##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
""".split('\n')
antinode(string)

