class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[0 for _i in range(m)] for _j in range(n)]

    def __getitem__(self, tuple):
        i, j = tuple
        return self.matrix[i][j]

    def __setitem__(self, tuple, value):
        i, j = tuple
        self.matrix[i][j] = value

    def __str__(self):
        return "\n".join(map(str, self.matrix))


if __name__ == '__main__':
    m = Matrix(3, 4)
    print(m[0, 1])
    m[0, 1] = 2
    print(m[0, 1])
    print(m)
