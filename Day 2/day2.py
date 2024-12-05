def day2():
    data = []

    # Open data and append to list:
    with open('./data.txt', 'r') as d:
        for line in d:
            lst = [int(x) for x in line.strip().split(' ')]
            data.append(lst)

    safe = 0
    unsafe = 0

    # Iterate through data:
    for x in data:
        diff = []
        for i, y in enumerate(x):
            if i + 1 == len(x):
                continue
            else:
                diff.append(y - x[i + 1])
        
        # Check for 0
        if 0 in diff:
            unsafe += 1
            continue
        
        # Check for values greater than 3 and less than -3
        if any(x > 3 for x in diff) or any(x < -3 for x in diff):
            unsafe += 1
            continue
      
        # Check values are either all positive or all neg:
        if all(x > 0 for x in diff) or all(x < 0 for x in diff):
            safe += 1
            continue
    
    print(f'Safe: {safe}, Unsafe: {unsafe}')

        





day2()