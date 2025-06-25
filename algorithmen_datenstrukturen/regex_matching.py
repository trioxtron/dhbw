def isMatch(s: str, p: str) -> bool:
    hold = ""
    result = s 
    for i in range(len(s)):
        if hold == "" and i >= len(p):
            return False
        elif p[i] == "*":
            hold = p[i-1]
            result = s[i:]
        elif p[i] == ".":
            result = s[i:]
        
        if p[i] == s[i] or hold == s[i]:
            result = s[i:]

    print("This is your s: ", s)    

    if len(result) == 0:
        return True

    return False

def main():
    # Test cases
    test_cases = [
        ("aa", "a"),      # False
        ("aa", "a*"),     # True
#       ("ab", ".*"),     # True
#       ("aab", "c*a*b"), # True
#       ("mississippi", "mis*is*p*."), # False
#       ("", ".*"),       # True
#       ("abc", "a.c"),   # True
#       ("abc", "a*c"),   # False
    ]
    for s, p in test_cases:
        print(f"Testing with s = '{s}' and p = '{p}'")
        print(f"Length of s: {len(s)}")
        print(f"Length of p: {len(p)}")
        result = isMatch(s, p)
        print(f"isMatch({s}, {p}) = {result}")

if __name__ == "__main__":
    main()
