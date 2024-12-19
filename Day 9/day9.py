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
    
    def create_block(lst):
        perm_arr = []
        temp_arr = []
        current_num = None
        # Reverse the list and iterate through it:
        for i, x in enumerate(lst[::-1]):
            # if x is an integer:
            if isinstance(x, int):
                if current_num == None:
                    current_num = x
                    temp_arr.append(x)
                elif x == current_num:
                    temp_arr.append(x)
                elif x != current_num:
                    current_num = x
                    perm_arr.append(temp_arr)
                    temp_arr = [x]
        if temp_arr:
            perm_arr.append(temp_arr)
        return perm_arr
    block_list = create_block(num_list)
    print(new_list, block_list)

    # Create number indexes to make them easier to delete later:
    del_dict = {}
    for i, x in enumerate(new_list):
        if isinstance(x, int):
            if x not in del_dict:
                del_dict[x] = [i]
            else:
                del_dict[x].append(i)

    print('Numbers to delete, ', del_dict)

    index_tracked = []
    # Now iterate through new_list and determine the LENGTH of each space.
    for i, x in enumerate(new_list[:]):
        # use copy of new_list to maintain index integrity. 
        if x == '.':
            if i in index_tracked:
                # If index has already been tracked, ignore it.
                continue
            else:
                # Determine which indexes can be filled
                index_to_fill = []
                # Iterate through slice of list here:
                # Starting position should be equal to the index of x
                for iy, ix in enumerate(new_list[i:]):
                    if ix == '.':
                        index = i + iy
                        index_to_fill.append(index)
                        index_tracked.append(index)
                    else:
                        # MUST BREAK LOOP:
                        break
                print('index to fill; ', index_to_fill)
                space = len(index_to_fill)

                def viable():
                    return [x for x in block_list if len(x) <= len(index_to_fill)]
            

                while space and len(viable()) > 0:
                    print(space, 'Space')
                    for ry, rx in enumerate(block_list):
                        if len(rx) <= space:
                            space -= len(rx)
                            for r in range(len(rx)):
                                new_list[i + r] = rx[0]
                                index_to_fill.pop()
                            block_list.pop(ry)
                        else:
                            continue

                
        else:
            # Delete from block list if number:
            for ind, arr in enumerate(block_list):
                if arr[0] == x:
                    block_list.pop(ind)
                    break
    print(new_list)


        

    

# compact2(sample)
# compact2(data)
compact2(sample_two)
    
# 6200294120911 - Too low.


