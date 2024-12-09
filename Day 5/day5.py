# Function to access data:
def get_data(location):
    arr = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for i, x in enumerate(d):
            arr.append(x)
    
    return arr

# Read live data:
live_data = get_data('./data.txt')

# Split list into two parts:
rules_arr = [record.strip().split('|') for record in live_data if '|' in record]
update_arr = [record.strip().split(',') for record in live_data if ',' in record]


# Part 1:
middle = 0
for record in update_arr:
    rec_arr = []
    for i, x in enumerate(record):
        if i == len(record) - 1:
            arr = [record[i - 1], record[i]]
            if arr in rules_arr:
                rec_arr.append(record[i])
        else:
            if [record[i], record[i + 1]] in rules_arr:
                rec_arr.append(record[i])
        if len(rec_arr) == len(record):
            middle_index = round((len(rec_arr) - 1) / 2)
            middle_value = int(rec_arr[middle_index])
            middle += middle_value
            

print(f'Answer for part one is: {middle}.')

# Part 2:
sample_rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""



sample_order = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# rules_arr = [record.split('|') for record in sample_rules.strip().split('\n')]
# update_arr = [record.split(',') for record in sample_order.split('\n')]
incorrect_arr = []
correct_arr = []

# First establish list of arrays that are incorrectly ordered.
for record in update_arr:
    for i, x in enumerate(record):
        if i == len(record) - 1:
            arr = [record[i - 1], record[i]]
            if arr not in rules_arr:
                if record not in incorrect_arr:
                    incorrect_arr.append(record)
        else:
            if [record[i], record[i + 1]] not in rules_arr:
                if record not in incorrect_arr:
                    incorrect_arr.append(record)

# Now put arrays into correct order.



def order(arr, order):
    # Set flag:
    incorrect = 1
    while incorrect > 0:
        for i, x in enumerate(arr):
            # Final value:
            if i == len(arr) - 1:
                check_arr = [arr[i - 1], arr[i]]
                # If check_arr in order, then correct order.
                if check_arr in order:
                    incorrect -= 1
                # If check_arr not in correct order, then swap.
                else:
                    incorrect += 1
                    arr[i] = check_arr[0]
                    arr[i + 1] = check_arr[1]
            
            # Remaining Values:
            else:
                check_arr = [arr[i], arr[i + 1]]
                # If check_arr in order, then correct order.
                if check_arr in order:
                    continue
                # If check_arr not in correct order, then swap.
                else:
                    incorrect += 1
                    arr[i] = check_arr[1]
                    arr[i + 1] = check_arr[0]
                    
    middle_index = round((len(arr) - 1) / 2)
    middle_value = int(arr[middle_index])
    return middle_value


p2 = 0

# Iterate through incorrect_arr and call ordering function:
for record in incorrect_arr:
    p2 += order(record, rules_arr)

print(f'The answer to part 2 is: {p2}')


