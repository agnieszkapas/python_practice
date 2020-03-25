def unique_elements(seq):
    buf = set()
    for el in list(seq): #utowrzona kopia listy
        if el in buf:
            seq.remove(el)
        else:
            buf.add(el)

def main():
    seq = [1,2,5,6,7,8,5,5,5,5,8,8,9]
    unique_elements(seq)
    print(seq)

main()