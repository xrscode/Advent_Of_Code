# Function to access data:
def get_data(location):
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
      arr = [int(char) for char in d.read()]  
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
    
  
    f_stop_count = new_list.count('.')
    f_stop_arr = ['.' for i in range(f_stop_count)]

    iteration = 0
  
    while new_list[-len(f_stop_arr):] != f_stop_arr:  # Ensure the last part matches `f_stop_arr`
        iteration += 1
        print(f'Iteration number: {iteration}')
        for i, num in enumerate(new_list[:]):  # Use a copy to avoid issues with list modification
            # Find the last integer
            last_digit = [n for n in new_list[::-1] if isinstance(n, int)][0]
            last_index = len(new_list) - 1 - new_list[::-1].index(last_digit)

            if num == '.':
                # Replace the current '.' with the last digit
                new_list[i] = last_digit

                # Remove the last occurrence of the last digit
                new_list.pop(last_index)

                # Add a '.' to the end
                new_list.append('.')

                # Exit the loop early to re-evaluate the condition
                break

  
    sum = 0
    
    for i, x in enumerate(new_list):
        if isinstance(x, int):
            num = x * i
            if num > 0:
                sum += num
    
    
    return sum

# print(f'Sample data one: {compact([1, 2, 3, 4, 5])}')
# print(f'Sample data two: {compact(sample)}')
print(f'Part one answer: {compact(data)}')



    



