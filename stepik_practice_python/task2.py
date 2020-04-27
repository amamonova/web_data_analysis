from collections import Counter


def length_statistics(str):
    words = str.split(' ')
    lens = [len(w) for w in words]
    for pair in sorted(Counter(lens).items(), key=lambda i: i[0]):
        print(f'{pair[0]}: {pair[1]}')


if __name__ == '__main__':
    length_statistics('Beautiful is better than ugly. '
                      'Explicit is better than implicit.')
