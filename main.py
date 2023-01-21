upper_no = int(input('enter the upper limit')) + 1  # upper limit of the range of numbers in which you want to find primes
non_prime = True  # to keep track if a number was divisible by any non 1 integer
primes = [2]  # we have to keep 2 for starters, so the inner loop can start
for i in range(2,upper_no):
    if non_prime == False:
        primes.append(c)
    non_prime = False  # resetting
    for prime in primes:
        c = i  # to keep track of the iteration that came right before i
        if i % prime == 0:
            non_prime = True
            break  # if a number is divisible by any non 1 integer break loop as it is a confirmed non prime number
print(*primes)
