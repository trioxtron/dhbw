def collatz_sequence(n, alpha, beta):
    org_n = n
    sequence = set()
    for i in range(100000):  # Limit iterations to prevent infinite loops
        if i == 100000:
            print(f"Reached iteration limit for starting number {org_n}.")
            break

        if n in sequence:
            return org_n
        sequence.add(n)

        if n == 1:
            print(f"Reached 1 for starting number {org_n} after {i} iterations.")
            break
        elif n % 2 == 0:
            n = n // 2 
        else:
            n = n * alpha + beta



if __name__ == "__main__":
    collatz_sequence(27, 3, 1)


    nums_with_cycle = []
    for number in range(1, 21):
        res = collatz_sequence(number, 3, 1)

        if res:
            nums_with_cycle.append(res)

    print("Numbers that lead to a cycle with alpha=3 and beta=7:", nums_with_cycle)
