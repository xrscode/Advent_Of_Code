import itertools
# Function to access data:
def get_data(location):
    arr = []
    # Open data and append to list:
    with open(f'{location}', 'r') as d:
        for x in d:
            n = x.strip().split(':')
            b = n[1].strip().split(' ')
            c = [int(x) for x in b]
            nl = [int(n[0]), c]
            arr.append(nl)
    
    return arr

# Read live data:
data = get_data('./data.txt')

import itertools

def evaluate_left_to_right(expression):
    """Evaluate a mathematical expression strictly from left to right, including `||` for concatenation."""
    tokens = expression.split()
    result = tokens[0]
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = tokens[i + 1]
        
        if operator == '+':
            result = str(int(result) + int(operand))
        elif operator == '-':
            result = str(int(result) - int(operand))
        elif operator == '*':
            result = str(int(result) * int(operand))
        elif operator == '/':
            result = str(int(result) / int(operand))
        elif operator == '||':
            result = result + operand  # Concatenate as strings
        else:
            raise ValueError(f"Unknown operator: {operator}")
    
    return int(result)

def generate_combinations(num, numbers):
    """Generate all possible combinations of `+`, `*`, and `||` for the given numbers."""
    total = 0
    symbols = ['+', '*', '||']
    combinations = list(itertools.product(symbols, repeat=len(numbers) - 1))
    
    for comb in combinations:
        expression = ''
        for i, number in enumerate(numbers):
            if i == len(numbers) - 1:
                expression += f'{number}'
            else:
                expression += f'{number} {comb[i]} '
        
        # Evaluate the expression
        record = evaluate_left_to_right(expression)
        
        # Check if it matches the target number
        if record == num:
            total += num
            return total  # Return early if a match is found
    
    return total




t = 0
for i, x in data:
    print('Current t value: ', t)
    t += generate_combinations(i, x)
print('Part 1 answer: ', t)