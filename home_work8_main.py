import heapq


def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]


# набір кабелів, їх довжини, будуть як масив у вигляді цілих чисел
cabels = [3, 2, 1, 4]
print("Набір кабелів:", cabels)

# сортування кабелів
sorted_cabels = heap_sort(cabels)
print("Відсортованні кабеля:", sorted_cabels)

# всього
print("Мінімальна вартість з'єднання:", sum(sorted_cabels))
