import numpy as np

def main():
    chessboard = np.zeros((8, 8))

    chessboard[1::2, 0::2] = 1
    chessboard[0::2, 1::2] = 1


    chessboard = np.pad(chessboard, 1, mode='constant', constant_values=2)

    print(chessboard)
    print("\n")



if __name__ == "__main__":
    main()
