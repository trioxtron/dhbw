def isPrime(n):
    if n <= 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return i
    return True

def main():
    n = input("Enter a number: ")
    print(isPrime(int(n)))

if __name__ == "__main__":
    main()
