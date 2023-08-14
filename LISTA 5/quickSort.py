def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Exemplo de uso
array = [5, 2, 9, 1, 7, 6, 3]
sorted_array = quick_sort(array)
print(sorted_array)
