def main():

    file = open("test_file.txt", "rt")
    data = file.read()
    words = data.split()

    print('Number of words in test file is :', len(words))

if __name__ == "__main__":
    main()

