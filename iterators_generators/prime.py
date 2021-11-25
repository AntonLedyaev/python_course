def primes():
    number = 2
    while True:
        is_prime = True
        divisor = 2
        while divisor ** 2 <= number:
            if number % divisor == 0:
                is_prime = False # non-trivial divisor
                break

            divisor += 1

        if is_prime:
            yield number

        number += 1


