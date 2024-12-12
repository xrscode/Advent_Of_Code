# Function to access data:
def get_data(location):
    arr = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for line in d:
            arr.append(line)
    
    return arr

# Read live data:
data = get_data('./data.txt')

print(data)