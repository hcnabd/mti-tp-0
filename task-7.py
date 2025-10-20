# Part 1: 
num = 101
while True:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        break
    num += 1
    
# Part 2:
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)