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

  
    def optimized_sort(new_list, f_stop_arr):
        iteration = 0
        target_len = len(f_stop_arr)

        while new_list[-target_len:] != f_stop_arr:  # Ensure the last part matches `f_stop_arr`
            iteration += 1
            print(f'Iteration number: {iteration}')

            # Find the last integer in the list once per iteration
            try:
                last_digit = next(n for n in reversed(new_list) if isinstance(n, int))
            except StopIteration:
                raise ValueError("No integers found in the list.")

            for i, num in enumerate(new_list):
                if num == '.':
                    # Replace the current '.' with the last digit
                    new_list[i] = last_digit

                    # Remove the last occurrence of the last digit (optimize search)
                    last_index = len(new_list) - 1 - new_list[::-1].index(last_digit)
                    new_list.pop(last_index)

                    # Add a '.' to the end
                    new_list.append('.')

                    # Exit the loop after a single replacement
                    break
    

        return new_list
    
    optimized_sort(new_list, f_stop_arr)

  
    sum = 0
    
    for i, x in enumerate(new_list):
        if isinstance(x, int):
            num = x * i
            if num > 0:
                sum += num
    
    
    return sum

# print(f'Part one answer: {compact(data)}')



# PART 2:
def compact2(files):
    new_list = []
    flag = 0
    spaces_dict = {}
    values_dict = {}

    # CONVERSION:
    # Convert a number like; 2333133121414131402 into 00...111...2...333.44.5555.6666.777.888899. 
    # Iterate over data.
    for i, x in enumerate(files):
        # If first value or even value of i, append flag to new_list.
        if i == 0 or i % 2 == 0:
            # If i == 0 and val is 2, this will append 0 0 to new_list
            for val in range(x):
                new_list.append(flag)
                # Append the index position and length of values:
                values_dict[f'{i}'] = {'value': flag, 'length': x}
            flag += 1
        else:
            # If i is odd, append a '.'.  
            for val in range(x):
                new_list.append('.')
                # Append to spaces_dictionary the index position and number of spaces:
                
    # Initialize dictionary to store sequences of dots
    spaces_dict = {}
    index_arr = []

    # Determine spaces:
    for i, x in enumerate(new_list):
        if x == '.':
            index_arr.append(i)  # Track indices of dots
            # If it's the last element in the list, save the sequence
            if i == len(new_list) - 1:
                spaces_dict[index_arr[0]] = {'total_space': len(index_arr), 'num_arr': []}
        elif isinstance(x, int) and index_arr:
            # Save the sequence when transitioning from dots to a number
            spaces_dict[index_arr[0]] = {'total_space': len(index_arr), 'num_arr': []}
            index_arr = []  # Reset index array
    index_arr = []

    # Print value dictionary:
    for value in values_dict:
        print(f'Index position: {value}.  Value is: {values_dict[value]}')

    # Print spaces dictionary:
    for value in spaces_dict:
        print(f'Space found at index position: {value}.  The total space is: {spaces_dict[value]}')

    for space in spaces_dict:
        space_to_fill = spaces_dict[space]['total_space']
        arr = spaces_dict[space]['num_arr']
        while len(arr) < space_to_fill:
            possible_nums = []
            for value in values_dict:
                if values_dict[value]['length'] <= space_to_fill:
                    possible_nums.append(values_dict[value])
            for i in range(possible_nums[-1]['length']):
                arr.append(possible_nums[-1]['value'])
            del(values_dict[value])
        print(spaces_dict)


            











          
            


   
   


        



    
  

  
    pass

compact2(sample)
# compact2(data)
    



