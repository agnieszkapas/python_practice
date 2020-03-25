def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        b = b++a
        a = b-a
        yield a


def main():
    for n in fibonacci(11):
        print(n)


if __name__ == "__main__":
    main()

