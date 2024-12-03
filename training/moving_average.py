def movingAverage(x, win=3):
    for i in range(len(x) - win + 1):
        print(sum(x[i:i+win]) / win)

def main():
    x = [2.4, 4.3, 2.3, 2.5, 9.4, 3.4, 6.4, 2.9, 2.3, 6.7, 3.3, 9.4, 8.4, 2.3]

    movingAverage(x)


if __name__ == "__main__":
    main()
