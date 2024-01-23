import timeit

# Simple Approach for GCD of two numbers
def Simple(a, b):
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    return result

# Euclid algorithm (recursive)
def Euclid_recursiv(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a == b:
        return a

    if a > b:
        return Euclid_recursiv(a - b, b)
    return Euclid_recursiv(a, b - a)

# Iterative implementation of the Euclid algorithm
def Euclid_iterativ(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    return a

# Dictionary to store execution times for each algorithm
execution_times = {
    'Simple': [],
    'Euclid_recursiv': [],
    'Euclid_iterativ': []
}

# Measure the execution time for each algorithm
for algorithm in [Simple, Euclid_recursiv, Euclid_iterativ]:
    print(f"Running {algorithm.__name__}")
    a = 98
    b = 56
    for i in range(10):
        execution_time = timeit.timeit(f"{algorithm.__name__}({a}, {b})", globals=globals(), number=1000)
        execution_times[algorithm.__name__].append(execution_time)
        print(f"{algorithm.__name__}({a}, {b})\nIteration {i + 1}\nExecution Time: {execution_time:.6f} seconds\nNumbers: a={a} b={b}\n")
        a += 1
        b += 1
    print()

# Compare execution times
for algorithm in execution_times:
    avg_time = sum(execution_times[algorithm]) / len(execution_times[algorithm])
    print(f"Average execution time for {algorithm}: {avg_time:.6f} seconds")

fastest_algorithm = min(execution_times, key=lambda algorithm: sum(execution_times[algorithm]))
print(f"The fastest algorithm is {fastest_algorithm}.")
