def prime_num(n):

    if n == 2:
        return False

    if n % 2 == 0 or n <= 1:
        return False

    sq_root = int(n**0.5) + 1
    for divider in range(3, sq_root, 2):
        if n % divider == 0:
            return False
    return True


def main():
    # a. map i filter
    list(map(print, filter(prime_num, range(50))))

    # b. list comprehension
    num_list = list(range(50))
    print([number for number in num_list if prime_num(number)])


if __name__ == "__main__":
    main()

