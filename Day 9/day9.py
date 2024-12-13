# Function to access data:
def get_data(location):
    
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        arr = [[int(char) for char in line] for line in d]
    return arr

# Read live data:
data = get_data('./data.txt')
sample = [int(char) for char in '2333133121414131402']

def compact(files):
    new_list = []
    flag = 0

    # CONVERSION:
    # Convert a number like; 2333133121414131402 into 00...111...2...333.44.5555.6666.777.888899. 
    # Iterate over data.
    for i, x in enumerate(files):
        # If first value or even value of i, append flag to new_list.
        if i == 0 or i % 2 == 0:
            # If i == 0 and val is 2, this will append 0 0 to new_list
            for val in range(x):
                new_list.append(flag)
            flag += 1
        else:
            # If i is odd, append a '.'.  
            for val in range(x):
                new_list.append('.')
    

    
    # Count number of full stops.
    full_stops = new_list.count('.')
    # Create an array of said number of fullstops.  Used for comparison later:
    full_stop_arr = ['.' for i in range(full_stops)]

    # SORT
    temp_list = []

    # First sort to get full stops in correct position.
    while new_list[-full_stops:] != full_stop_arr:  # Keep sorting until end of list looks like full_stop_arr
        for i, x in enumerate(new_list[:]):  # Use a copy of `new_list` to avoid issues
            if x == '.':
                new_list.pop(i)          # Remove the current '.'
                new_list.append('.')     # Add it to the end
                temp_list.append(new_list[:])  # Store a snapshot of the current state
                break  # Restart the loop to prevent index missalignment
    
    new_temp = []
    # Now sort arrays in temp list to change number positions
    for i, line in enumerate(temp_list):
        full_stops = i + 1  # Define full_stops as the iteration count plus 1
        # Get the slice of the list that corresponds to the "numbers" you want to move
        numbers = line[len(line) - full_stops * 2: len(line) - full_stops]
        
        # Remove the selected slice from the list (use del to remove a slice)
        del line[len(line) - full_stops * 2: len(line) - full_stops]
        
        # Insert the numbers at the desired position in the list (at index i)
        line.insert(0, numbers)  # Use * to unpack the list of numbers
        
        # Append the modified line to new_temp
        new_temp.append(line)

    # Output the results for verification
    for line in new_temp:
        print(line)
      

compact(sample)

# STOP:
# len(line) - full_stops


    



