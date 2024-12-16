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
        print(f'VALUE_DICT: Index position: {value}.  Value is: {values_dict[value]}')

    # Print spaces dictionary:
    for value in spaces_dict:
        print(f'SPACE_DICT: Space found at index position: {value}.  The total space is: {spaces_dict[value]}')




   

        # Iterate through each space in the spaces_dict
    for space_key in spaces_dict:
        space = spaces_dict[space_key]
        remaining_space = spaces_dict[space_key]['total_space'] - len(spaces_dict[space_key]['num_arr'])
        viable_numbers = True

        # There MUST be viable numbers and space remaining in the array:
        while remaining_space > 0 and viable_numbers:
            # Create numbers array to store viable numbers:
            viable_num_arr = []

            # Iterate through value dictionary and add to viable_num_arr:
            for value in list(values_dict):  # Use list() to avoid modifying dict while iterating
                if values_dict[value]['length'] <= remaining_space:
                    viable_num_arr.append([value, values_dict[value]])

            # Check that there are viable numbers:
            if len(viable_num_arr) == 0:
                print(f"No more viable numbers for space {space_key}. Remaining space: {remaining_space}")
                viable_numbers = False
                break

            # Select the best viable number (e.g., the largest that fits):
            best_number = viable_num_arr[-1]  # Select the last number in viable_num_arr
            val = best_number[1]['value']
            quantity = best_number[1]['length']

            # Add the number to the num_arr in spaces_dict
            spaces_dict[space_key]['num_arr'].extend([val] * quantity)

            # Update remaining_space
            remaining_space -= quantity

            # Remove or update the value in values_dict
            values_dict[best_number[0]]['length'] -= quantity
            if values_dict[best_number[0]]['length'] <= 0:
                del values_dict[best_number[0]]  # Remove completely if used up

    
    print(spaces_dict)

    for key, value in spaces_dict.items():
        index = key
        arr = value['num_arr']
        
        # Map elements from `arr` to `new_list` starting at `index`
        for i, x in enumerate(arr):
            new_list[index + i] = x

    # Clean up `new_list` by removing duplicates of `arr` beyond the valid range
    valid_range = max(key + len(value['num_arr']) for key, value in spaces_dict.items())
    new_list = [
        y for c, y in enumerate(new_list)
        if c <= valid_range or y not in [value['num_arr'] for value in spaces_dict.values()]
]
           
            
        
    
    print(new_list)

   


        

            


            











          
            


   
   


        



    
  

  
    pass

compact2(sample)
# compact2(data)
    



