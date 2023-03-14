# Jose Miguel Reyes
# CIS 3301
# Fibonacci Number Sequence

def get_fibonacci_number(position):
    if position <= 2:
        return 1
    return get_fibonacci_number(position-1) + get_fibonacci_number(position-2)

def get_fibonacci_number_sequence(number):
    return [get_fibonacci_number(i) for i in range(1, number+1)]

if __name__ == "__main__":
    pass