
print("Hello, welcome to the prime number checker!")

list_prime_numbers = []
for i in range(0, 50):
    is_prime = True
    for j in range(1, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
       list_prime_numbers.append(i)


print(f"Here is a list of prime numbers between 2 and 50: {list_prime_numbers}")
