import random 


def calcMean(grades):
    sum = 0
    for key in grades:
        sum += grades[key]
    return sum / len(grades)


def removeNames(names, grades):
    for name in names:
        if name in grades:
            del grades[name]
    return grades


def main():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kevin', 'Larry', 'Mallory', 'Nancy', 'Oscar', 'Peggy', 'Quentin', 'Romeo', 'Sybil', 'Trent', 'Ursula', 'Victor', 'Walter', 'Xavier', 'Yvonne', 'Zelda']
    grades = {}

    for i in range(len(names)):
        grades[names[i]] = random.randint(1, 6)

    print(calcMean(grades))
    newDict = removeNames(['Alice', 'Bob', 'Charlie'], grades)
    print(calcMean(newDict))

if __name__ == '__main__':
    main()
