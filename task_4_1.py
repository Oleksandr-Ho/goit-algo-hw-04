import timeit
import random

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Insertion Sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# __________________________________________


data_small = [random.randint(0, 1_000) for _ in range(100)]
data_medium = [random.randint(0, 10_000) for _ in range(1_000)]
data_large = [random.randint(0, 100_000) for _ in range(10_000)]

ts_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=10)
ts_merge = timeit.timeit(lambda: merge_sort(data_small), number=10)
ts_timsorted = timeit.timeit(lambda: sorted(data_small), number=10)
ts_timsort = timeit.timeit(lambda: data_small[:].sort(), number=10)

tm_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=10)
tm_merge = timeit.timeit(lambda: merge_sort(data_medium), number=10)
tm_timsorted = timeit.timeit(lambda: sorted(data_medium), number=10)
tm_timsort = timeit.timeit(lambda: data_medium[:].sort(), number=10)

tl_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=10)
tl_merge = timeit.timeit(lambda: merge_sort(data_large), number=10)
tl_timsorted = timeit.timeit(lambda: sorted(data_large), number=10)
tl_timsort = timeit.timeit(lambda: data_large[:].sort(), number=10)

print(f"| {'Algorithm':<20} | {'Small':<20} | {'Medium':<20} | {'Large':<20} |")
print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
print(f"| {'Insertion Sort':<20} | {ts_insertion:20.5f} | {tm_insertion:20.5f} | {tl_insertion:20.5f} |")
print(f"| {'Merge Sort':<20} | {ts_merge:20.5f} | {tm_merge:20.5f} | {tl_merge:20.5f} |")
print(f"| {'Timsorted':<20} | {ts_timsorted:20.5f} | {tm_timsorted:20.5f} | {tl_timsorted:20.5f} |")
print(f"| {'Timsort':<20} | {ts_timsort:20.5f} | {tm_timsort:20.5f} | {tl_timsort:20.5f} |")