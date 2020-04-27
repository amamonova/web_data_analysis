if __name__ == '__main__':
    str1 = sum([ord(x) for x in input().lower()])
    str2 = sum([ord(x) for x in input().lower()])

    if str1 == str2:
        print('True')
    else:
        print('False')
