# Function to access data:
def get_data(location):
    sentence = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for char in d:
            sentence.append(char.strip())
    
    return sentence

live_data = get_data('./data.txt')

sample_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

split_sample = sample_data.split('\n')

# Check sample first:
non_split = [x for x in split_sample]
split_arr = [[x for x in line] for line in split_sample]

total = 0

# Check Horizontal:
for x in non_split:
    forward = x.count('XMAS')
    backwards = x.count('SAMX')
    total += forward
    total += backwards


print(total)
