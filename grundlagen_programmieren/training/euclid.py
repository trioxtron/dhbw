def euclid(a, b):
    if a % b == 0:
        return b
    else:
        return euclid(b, a % b)

if __name__ == "__main__":
    print(euclid(8, 20))
