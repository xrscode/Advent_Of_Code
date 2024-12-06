import re

# Function to access data:
def get_data(location):
    lst = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for char in d:
            lst.append(char)
    
    return ''.join(lst)

live_data = get_data('./data.txt')
sample_text = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""



matches = re.findall("mul\((\d+),(\d+)\)", live_data)

total = 0

for x in matches:
   num = int(x[0]) * int(x[1])
   total += num

print('Part 1 total: ', total)


new_text = live_data.split("do()")



new_total = 0
for i, line in enumerate(new_text):
    if "don't()" not in line:
        new_match = matches = re.findall("mul\((\d+),(\d+)\)", line)
        for x in new_match:
        
            num = int(x[0]) * int(x[1])
            new_total += num
    else:
        new_split = line.split("don't()")[0]
        new_split_matches = re.findall("mul\((\d+),(\d+)\)", new_split)
        for x in new_split_matches:
            num = int(x[0]) * int(x[1])
            new_total += num

print('Part 2 total: ', new_total)

