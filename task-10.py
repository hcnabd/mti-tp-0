small_numbers = [10, 20, 30, 40, 50]

small_numbers[1] = 25
print(small_numbers)

small_numbers.append(60)
print(small_numbers)

small_numbers.insert(0, 5)
print(small_numbers)

small_numbers.remove(30)
print(small_numbers)

large_numbers = [100, 200, 300, 400, 500]

combined_list = small_numbers + large_numbers
print(combined_list)

print(30 in combined_list)

print(len(combined_list))

combined_list.sort(reverse=True)
print(combined_list)