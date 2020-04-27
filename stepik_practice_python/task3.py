if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [[] for _i in range(n)]
    for i in range(n):
        matrix[i].extend(list(map(int, input().split())))

    for line in list(zip(*matrix)):
        print(*line)