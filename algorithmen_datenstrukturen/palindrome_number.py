def isPalindrome(x: int) -> bool:
    copy = x
    reverse = 0

    while copy > 0:
        reverse = reverse * 10 + (copy % 10)
        copy = copy // 10
    
    return x == reverse


def main():
    x = 121
    print(isPalindrome(x))  # Output: True

    x = -121
    print(isPalindrome(x))  # Output: False

    x = 10
    print(isPalindrome(x))  # Output: False

    x = 12321
    print(isPalindrome(x))  # Output: True

    x = 0
    print(isPalindrome(x))  # Output: True

if __name__ == "__main__":
    main()
