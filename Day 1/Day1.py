# Advent of Code Day 1:
def day_one():
    data = []
    with open('data.txt', 'r') as d:
        for line in d:
            d_split = line.split(' ')
            data.append([d_split[0], d_split[3]])

    l1s = []
    l2s = []
    diff = []


    # Iterate through data
    for pair in data:
        l1 = int(pair[0])
        l2 = int(pair[1].strip())
        l1s.append(l1)
        l2s.append(l2)
   
    l1s.sort()
    l2s.sort()

    for i, x in enumerate(l1s):
        if x > l2s[i]:
            diff.append(x - l2s[i])
        elif x < l2s[i]:
            diff.append(l2s[i] - x)
        else:
            continue
    
    print(f'The total difference is: {sum(diff)}.')

    similarity = []

    for x in l1s:
        num = l2s.count(x)
        if num:
            similarity.append(x * num)
    
    print(f'The total similarity is: {sum(similarity)}.')
    
    
day_one()    
  
 




