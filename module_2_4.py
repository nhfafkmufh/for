numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in range(len(numbers)-1):
    i = i + 1
    is_prime = True
    for j in range(i):
        if numbers[i] % numbers[j] == 0 and numbers[j] != 1:
            is_prime = False
    if is_prime == True:
        Primes.append(numbers[i])
    else:
        Not_Primes.append(numbers[i])
print(Primes)
print(Not_Primes)
