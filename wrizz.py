def is_prime(n):
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    
    factors = set()
    
    while n % 2 == 0:
        n //= 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    
    if n > 2:
        factors.add(n)
    return factors

def main():
    count = 0
    with open('liczby.txt', 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = prime_factors(number)
            
            if len(factors) == 3 and all(factor % 2 != 0 for factor in factors):
                count += 1
    print(f"liczb znajduje sie: {count}")

if __name__ == "__main__":
    main()
