def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_number = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_number)
        return sequence

n = 10
result = fibonacci(n)
print(result)
