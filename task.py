import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для тестування алгоритмів
def test_sorting_algorithms():
    # Різні розміри масивів для тестування
    sizes = [1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"Array size: {size}")

        arr_copy = arr.copy()
        time = timeit.timeit(lambda: merge_sort(arr_copy), number=1)
        print(f"Merge Sort: {time:.6f} seconds")

        arr_copy = arr.copy()
        time = timeit.timeit(lambda: insertion_sort(arr_copy), number=1)
        print(f"Insertion Sort: {time:.6f} seconds")

        arr_copy = arr.copy()
        time = timeit.timeit(lambda: sorted(arr_copy), number=1)
        print(f"Timsort (sorted): {time:.6f} seconds")
        print()

# Запуск тестування
test_sorting_algorithms()