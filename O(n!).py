import itertools

def permutations(arr):
    return list(itertools.permutations(arr))

arr = [1, 2, 3]
print(permutations(arr))  # Виводимо всі можливі перестановки списку
