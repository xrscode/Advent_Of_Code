# Function to access data:
def get_data(location):
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
      arr = [int(char) for char in d.read()]  
    return arr

# Read live data:
data = get_data('./data.txt')
sample = [int(char) for char in '2333133121414131402']
sample_two = [int(char) for char in '1313165']


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
                # Append to spaces_dictionary the index position and number of spaces

    # Generate a list of all the numbers.
    num_list = [x for x in new_list[::-1] if isinstance(x, int)]
    # Turn them into 'blocks'.
    block_list = []  # Initialize block_list
    arr = []         # Initialize arr outside the loop
    current_num = None  # Initialize current_num to None

    for x in num_list:
        if x == current_num:  # If x matches the current number
            arr.append(x)     # Add x to the current block
        else:                 # If x is a new number
            if arr:           # If arr is not empty, save the previous block
                block_list.append(arr)
            arr = [x]         # Start a new block with the current number
            current_num = x   # Update the current number

    # After the loop, add the last block to block_list
    if arr:
        block_list.append(arr)
        

        


    stop_count = new_list.count('.')

    print(new_list, num_list, block_list)

    while block_list:
        for i, x in enumerate(new_list[:]):
            if isinstance(x, int):
                # Remove numbers from block_list
                for iy, ix in enumerate(block_list):
                    if block_list[iy][0] == x:
                        block_list.pop(iy)
            elif x == '.':
                # Determine how many '.' in front:
                count = 1
                for y in new_list[i- 1:]:
                    if y == '.':
                        count += 1
                    else:
                        count = 1
                        break
                    print('There is a space of; ', count)

        #         # Now determine if there are any possible blocks to move:
        #         for iy, y in enumerate(block_list):
        #             # Block must be less than or equal to the value of count:
        #             if len(y) <= count:
        #                 num = y[0]
        #                 # Add the numbers to the spaces:
        #                 for c in range(0, len(y)):
        #                     # Add the value.
        #                     new_list[i+c] = num
        #                     # Now find the last instance of num and remove.
        #                     for ix, x in enumerate(new_list[::-1]):
        #                         index_offset = len(new_list) - ix - 1
        #                         if x == num:
        #                             new_list[index_offset] = '.'
        #                 block_list.pop(iy)

        # sum = 0
        # for i, x in enumerate(new_list):
        #     if isinstance(x, int):
        #         sum += i * x
        #     else:
        #         break

        # print(sum)
        # return sum
    

# compact2(sample)
# compact2(data)
compact2(sample_two)
    
# 6200294120911 - Too low.


