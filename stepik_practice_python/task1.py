def get_int(start, error, end):
    print(start)
    while True:
        try:
            res = int(input())
            print(end)
            return res
        except:
            print(error)


if __name__ == '__main__':
    x = get_int('Input int number:', 'Wrong value. Input int number:',
                'Thank you.')