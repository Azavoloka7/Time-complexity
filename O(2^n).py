import itertools

def power_set(arr):
    n = len(arr)
    result = []
    for i in range(2**n):
        subset = [arr[j] for j in range(n) if (i & (1 << j))]
        result.append(subset)
    return result

arr = [1, 2, 3]
print(power_set(arr))  # Виводимо всі можливі підмножини списку
