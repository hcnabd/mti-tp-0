data_points = [10, 15, 20, 25, 30, 35]

print(sum(data_points))

count = 0
for num in data_points:
    if num > 20:
        count += 1
print(count)
