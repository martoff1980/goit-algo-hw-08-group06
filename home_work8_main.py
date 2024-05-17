import heapq


def heap_sort(iterable):
    # Створюємо мінімальну купу з усіх елементів ітерабельного об'єкта.
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    # Витягуємо елементи впорядковано, формуючи відсортований масив.
    return [heapq.heappop(h) for _ in range(len(h))]


def cabels_sorted_by_max(shortest_cabels, longest_cabels):
    sum_of_length = [0]
    h = [0]
    max_val = 0
    # виконуємо умову, що об'єднуємо буль-які 2 кабелі
    # конектемо кабеля з кожної групи
    for short in shortest_cabels:
        for long in longest_cabels:
            summ = short+long
            if summ >= max_val:
                index = sum_of_length.index(max_val)
                max_val = summ
                if index == -1:
                    sum_of_length.insert(0, summ)
                    h.insert(0, [short, long])
                else:
                    sum_of_length.insert(1, summ)
                    h.insert(1, [short, long])

            else:
                index = sum_of_length.index(summ)
                if index == -1:
                    sum_of_length.append(summ)
                    h.append([short, long])
                else:
                    sum_of_length.insert(index+1, summ)
                    h.insert(index+1, [short, long])

    sum_of_length.pop(0)
    h.pop(0)
    return h


def connection_by_min(cabels):
    for i in range(len(cabels), 0, -1):
        print(f"Крок {len(cabels)-i+1}:", cabels[i-1])


# набір кабелів, їх довжини, будуть як масив увигляді цілих чисел
cabels = [1, 5, 7, 9, 10, 8, 3, 11]
print("Набір кабелів:", cabels)

# сортування кабелів
sorted_cabels = heap_sort(cabels)
print("Відсортованні кабеля:", sorted_cabels)

# розбиваємо на дві групи
shortest_cabels = sorted_cabels[:len(sorted_cabels)//2]
print("Найкоротщі кабеля:", shortest_cabels)

longest_cabels = sorted_cabels[len(sorted_cabels)//2:]
print("Найдовщі кабеля:", longest_cabels)

result_by_max = cabels_sorted_by_max(shortest_cabels, longest_cabels)

connection_by_min(result_by_max)


# sum_of_length = [0]
# h = [0]
# max_val = 0
# виконуємо умову, що об'єднуємо буль-які 2 кабелі
# конектемо кабеля з кожної групи
# for short in shortest_cabels:
#     for long in longest_cabels:
#         summ = short+long
#         if summ >= max_val:
#             index = sum_of_length.index(max_val)
#             max_val = summ
#             if index == -1:
#                 sum_of_length.insert(0, summ)
#                 h.insert(0, [short, long])
#             else:
#                 sum_of_length.insert(1, summ)
#                 h.insert(1, [short, long])

#         else:
#             index = sum_of_length.index(summ)
#             if index == -1:
#                 sum_of_length.append(summ)
#                 h.append([short, long])
#             else:
#                 sum_of_length.insert(index+1, summ)
#                 h.insert(index+1, [short, long])

# sum_of_length.pop(0)
# print(sum_of_length)
# h.pop(0)
# print(h)

# for i in range(len(h), 0, -1):
#     print(i, h[i-1])
