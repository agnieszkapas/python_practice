
def my_sort(seq):
    flag = False

    def f(arg):
        nonlocal flag
        if arg in priority:
            flag = True
            return (0, arg)
        return (1, arg)

    seq.sort(key=f)
    return flag


def main():
    seq = [1, 2, 5, 6, 75, 5, 5, 6, 7, 8, 8, 9, 9, ]
    my_sort(seq, [6, 7])
    #print(seq)

    # if __name__ == '__main__':

main()