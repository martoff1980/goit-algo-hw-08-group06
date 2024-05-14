import heapq


def merge_k_lists(lists, n=0, new_list=[]):
    while n != len(lists):
        new_list.extend(lists[n])
        return merge_k_lists(lists, n+1)

    result = heap_sort(new_list)
    return result


def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
