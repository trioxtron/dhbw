
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)


def main():
    fib(6)
    fib(12)

if __name__ == "__main__":
    main()
