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

part_one = [record.strip().split('|') for record in live_data if '|' in record]
part_two = [record.strip().split(',') for record in live_data if ',' in record]

print(part_two)

