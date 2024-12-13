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
    for i, x in enumerate(files):
        if i == 0 or i % 2 == 0:
            for val in range(x):
                new_list.append(flag)
            flag += 1
        else:
            for val in range(x):
                new_list.append('.')

    full_stops = new_list.count('.')
    
    temp_list = []

    for i in range(full_stops):
        copy_arr = []
        for i, x in enumerate(new_list):
            if x == '.':
                copy_arr.append(new_list[0:i - 1])
                copy_arr.append('.')
            else:
                copy_arr.append(x)
        temp_list.append(copy_arr)
    print(temp_list)


    # temp_list = []

    # while new_list[-full_stops:]:  # Loop while the last `full_stops` elements exist
    #     for i, x in enumerate(new_list[:]):  # Use a copy of `new_list` to avoid issues
    #         if x == '.':
    #             new_list.pop(i)          # Remove the current '.'
    #             new_list.append('.')     # Add it to the end
    #             temp_list.append(new_list)  # Store a snapshot of the current state
    #             break  # Restart the loop to prevent index misalignment


                
    

print(compact(sample))