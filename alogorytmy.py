import time

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
            #start_time = time.time()
            steps = algorithm(size)
            #duration = time.time() - start_time
            results[algorithm.__name__].append((size, steps)) #,duration))
    print(results)
    return results

run_algorithms()
