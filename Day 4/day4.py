# Function to access data:
def get_data(location):
    sentence = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for char in d:
            sentence.append(char.strip())
    
    return sentence

# Read live data:
live_data = get_data('./data.txt')
# live_data = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""


# Create Array from live data:
live_arr = [[x for x in line] for line in live_data]


XMAS = 0

# 2586 too high.

# Ensure boundaries implemented correctly:
for iy, row in enumerate(live_arr):
    for ix, column in enumerate(row):
        if column == 'X':  # Found 'X', start checking in different directions
            
            # 1. Check Vertical (X: 0, Y: -1): 2
            if iy - 3 >= 0:  # Make sure there are 3 rows above
                string = f'{live_arr[iy][ix]}{live_arr[iy - 1][ix]}{live_arr[iy - 2][ix]}{live_arr[iy - 3][ix]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 2. Check Top Right (X: 1, Y: -1): 4
            if iy - 3 >= 0 and ix + 3 < len(row):  # Ensure we don't go out of bounds
                string = f'{live_arr[iy][ix]}{live_arr[iy - 1][ix + 1]}{live_arr[iy - 2][ix + 2]}{live_arr[iy - 3][ix + 3]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 3. Check Right (X: 1, Y:0): 3
            if ix + 3 < len(row):  # Ensure there are 3 more columns to the right
                string = f'{live_arr[iy][ix]}{live_arr[iy][ix + 1]}{live_arr[iy][ix + 2]}{live_arr[iy][ix + 3]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 4. Check Bottom Right (X: 1, Y: 1): 1
            if iy + 3 < len(live_arr) and ix + 3 < len(row):  # Ensure there are 3 more rows and columns
                string = f'{live_arr[iy][ix]}{live_arr[iy + 1][ix + 1]}{live_arr[iy + 2][ix + 2]}{live_arr[iy + 3][ix + 3]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 5. Check Downward (X: 0, Y: 1): 1
            if iy + 3 < len(live_arr):  # Ensure there are 3 more rows below
                string = f'{live_arr[iy][ix]}{live_arr[iy + 1][ix]}{live_arr[iy + 2][ix]}{live_arr[iy + 3][ix]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 6. Check Bottom Left (X: -1, Y: 1): 1
            if iy + 3 < len(live_arr) and ix - 3 >= 0:  # Ensure there are 3 rows below and 3 columns to the left
                string = f'{live_arr[iy][ix]}{live_arr[iy + 1][ix - 1]}{live_arr[iy + 2][ix - 2]}{live_arr[iy + 3][ix - 3]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 7. Check Left (X: -1, Y:0): 2
            if ix - 3 >= 0:  # Ensure there are 3 columns to the left
                string = f'{live_arr[iy][ix]}{live_arr[iy][ix - 1]}{live_arr[iy][ix - 2]}{live_arr[iy][ix - 3]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1

            # 8. Check Top Left (X: -1, Y: -1): 
            if ix - 3 >= 0 and iy - 3 >= 0:  # Ensure there are 3 rows above and 3 columns to the left
                string = f'{live_arr[iy][ix]}{live_arr[iy - 1][ix - 1]}{live_arr[iy - 2][ix - 2]}{live_arr[iy - 3][ix - 3]}'
                if string == 'XMAS' or string == 'SAMX':
                    XMAS += 1



        

# Check total count:
print(f'XMAS appears: {XMAS} times.')


