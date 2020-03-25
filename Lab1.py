
def print_room(height, width):
    for h in range(height+1):
        for w in range(width+1):
            if h%height == 0 and w%width == 0: #wierzcholek
                print('*', end='')
            elif h%height == 0 and w%width == 0: #sciany gorne/dolne
                print('-', end='')
            elif h%height != 0 and w%width == 0: #sciany lewe/prawe
                print('|', end='')
            else:
                print('.', end='')
        print('')

def main():
    height = int(input('Give height: '))
    width = int(input('Give width: '))
    print_room(height+1, width+1)

#if __name__ == ' __main__':
main()
