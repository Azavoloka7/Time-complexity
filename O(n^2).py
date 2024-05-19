def sum_of_pairs(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            total += arr[i] + arr[j]
    return total

arr = [1, 2, 3, 4, 5]
print(sum_of_pairs(arr))  # Виводимо суму всіх можливих пар елементів
