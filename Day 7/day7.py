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

def evaluate_left_to_right(expression):
    """Evaluate a mathematical expression strictly from left to right."""
    # Split the expression into tokens
    tokens = expression.split()
    # Start with the first number
    result = int(tokens[0])
    
    # Iterate through the tokens pairwise (operator, operand)
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        else:
            raise ValueError(f"Unknown operator: {operator}")
    return result



def generate_combinations(num, numbers):
    total = 0
    """Generate all possible combinations of `+` and `*` for length `n`."""
    symbols = ['+', '*']
    combinations =  list(itertools.product(symbols, repeat=len(numbers)- 1))
    for i, x in enumerate(combinations):
        expression = ''
        for i, y in enumerate(numbers):
            if i == len(numbers) - 1:
                expression += f' {str(numbers[i])}'
            elif i == 0:
                expression += f'{str(numbers[i])} {str(x[i])}'
            else:
                expression += f' {str(numbers[i])} {str(x[i])}'
        record = evaluate_left_to_right(expression)
        
        if record == num:
            total += num
            return total

    return total
    



# print(generate_combinations(3267, [81, 40, 27]))


t = 0
for i, x in data:
    t += generate_combinations(i, x)
print('Part 1 answer: ', {t})