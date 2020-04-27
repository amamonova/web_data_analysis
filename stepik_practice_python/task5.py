if __name__ == '__main__':
    inp = [int(x) for x in input().split()]
    n = len(inp)
    prefix = [inp[i] - inp[i+1] for i in range(n-1)]

    if sorted(prefix) == list(range(1, n-1)):
        print('Jolly')
    else:
        print('Not jolly')

    print(sorted(prefix))
    print(list(range(1, n)))