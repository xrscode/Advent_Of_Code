import itertools

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

# Diagram to help visualise concept:
for i, line in enumerate(sample_data):
    print(i, line.strip())

def antinode(data):
    
    # Create boundary check function:
    def boundary(x, y):
        # X must be less than length of row:
        if x >= 0 and x <= len(data[0]) - 1:
            # Y must be less than lenght of data set:
            if y >= 0 and y <= len(data) - 1:
                return True
        return False
    
    # Store found antennaes in location dictionary:
    locations = {}
    antinodes = []

    # Iterate through data to find antennaes:
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if data[y][x] == 'a' and data[y][x] != '#':
                char = data[y][x]
                print('Antennae found at: ', x, y)
                if char not in locations:
                    locations[char] = [[x, y]]
                else:
                    locations[char].append([x, y])
    
    # Iterate through atennae locations:
    for antennae in locations:
        # Generate list of all possible combinations:
        combinations = list(itertools.product(locations[antennae], repeat=len(locations[antennae])))
        
       
       # Iterate through pairs of combinations to make comparisons:
        for i, x in enumerate(combinations):

            # Check not comparing same values:
            if x[0] != x[1]:
                # Establish Antenna Locations:
                ant_1 = [x[0][0], x[0][1]]
                ant_2 = [x[1][0], x[1][1]]
                

                """
                HORIZONTAL
                Establish which antenane is 'ahead':  Has a greater y value. 
                Then work out the x - distance and y - distance between two antennaes.
                Then work out possible antinode positions. 
                """
                if ant_1[0] != ant_2[0] and ant_1[1] != ant_2[1]:
                    x_dis = ant_1[0] - ant_2[0]
                    y_dis = ant_1[1] - ant_2[1]
                    print('X distance: ', x_dis, 'Y distance: ', y_dis)

                 
                    ant_n_one = [ant_1[0] + x_dis, ant_1[1] + y_dis]
                    if boundary(ant_n_one[0], ant_n_one[1]) and ant_n_one not in antinodes:
                            antinodes.append(ant_n_one)
                 
                    ant_n_two = [ant_2[0] + x_dis, ant_2[1] - y_dis]
                    if boundary(ant_n_two[0], ant_n_two[1]) and ant_n_two not in antinodes:
                            antinodes.append(ant_n_two)


               
        
                
                # Check Vertical: y 0, x 1
                # Check Horizontal: y1, x 0
            
           
    print(antinodes)
    return antinodes


# Run function with sample data:
antinode(sample_data)