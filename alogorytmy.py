
#zlozonosc O(1):
def stala(n):
    steps = 0
    result = n + 100  
    steps += 1
    return steps


#zlozonosc O(n):
def liniowa(n):
    steps = 0
    total = 0
    for i in range(n): 
        total += i
        steps += 1
    return steps


#zlozonosc O(n^2):
def kwadratowa(n):
    steps = 0
    total = 0
    for i in range(n): 
        for j in range(n):
            total += i + 10*j
            steps += 1
    return steps


def run_algorithms():
    sizes = [10, 1000, 10000]  
    algorithms = [stala, liniowa, kwadratowa]
    results = {}

    for algorithm in algorithms:
        results[algorithm.__name__] = []
        for size in sizes:
            steps = algorithm(size)
            results[algorithm.__name__].append((size, steps))
    print(results)
    return results

run_algorithms()


#zlozonosc wykladnicza O(a^n) -- przyklad: obliczanie m-tej liczby ciagu fibonacciego
    #przeskalowano wartosci m={10, 20, 35}

stepsf = 0
m = 10
def fibonacci_with_counter(m):
    global stepsf
    stepsf += 1  
    if m <= 1:
        return m
    return fibonacci_with_counter(m - 1) + fibonacci_with_counter(m - 2)


result = fibonacci_with_counter(m)

print(f"m: {m})")
print(f"Liczba kroków: {stepsf}")

stepsf = 0
mm = 20
def fibonacci_with_counter(mm):
    global stepsf
    stepsf += 1  
    if mm <= 1:
        return mm
    return fibonacci_with_counter(mm - 1) + fibonacci_with_counter(mm - 2)


result = fibonacci_with_counter(mm)

print(f"m: {mm})")
print(f"Liczba kroków: {stepsf}")

stepsf = 0
mmm=35
def fibonacci_with_counter(mmm):
    global stepsf
    stepsf += 1  
    if mmm <= 1:
        return mmm
    return fibonacci_with_counter(mmm - 1) + fibonacci_with_counter(mmm - 2)


result = fibonacci_with_counter(mmm)

print(f"m: {mmm})")
print(f"Liczba kroków: {stepsf}")