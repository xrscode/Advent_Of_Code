# Function to access data:
def get_data(location):
    data = []

    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for line in d:
            lst = [int(x) for x in line.strip().split(' ')]
            data.append(lst)
    return data
        


# Function to check list:
def checkList(list):
    diff = []
    # Iterate through each item: e.g. 7, 6, 4, 2, 1
    for i, x in enumerate(list):
        # Determine last position: e.g. 1
        if i == len(list) - 1:
            pass
        else:
            temp_num = (x - list[i+1]) * -1
            diff.append(temp_num)
    
    # Analyse difference list:
    # Levels must ALL be increasing OR decreasing
    # Levels must differ by at least one and at most three.
    increase = all(x > 0 and x <= 3 for x in diff)
    decrease = all(x < 0 and x >= -3 for x in diff)
    
    if increase or decrease:
        return True
    
    return False


# Sample Data
sample_data = get_data('./sample.txt')
# Live Data
live_data = get_data('./data.txt')


# Check data:
def dampner(list):
    problems = 0
    success = 0

    if not checkList(list):
        print('Checking list: ', list)
        for i, x in enumerate(list):
            new_list = list[:i] + list[i+1:]
            if not checkList(new_list):
                problems += 1
            else:
                success += 1
    if success > 0:
        return True
    else:
        return False

            
safe = 0
unsafe = 0

# Iterate through data:
for x in live_data:
    if checkList(x):
        safe += 1
    else:
       if dampner(x):
           safe += 1
       else:
           unsafe += 1

print('Safe is: ', safe)
print('Unsafe is: ', unsafe)

        







