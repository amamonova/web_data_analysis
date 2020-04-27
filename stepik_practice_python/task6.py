def swap_letters(inp_string):
    res = ''
    for i in range(0, len(inp_string)-1, 2):
        res += inp_string[i+1]
        res += inp_string[i]
    return res


if __name__ == '__main__':
    inp_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        inp_lines.append(line)
    print([swap_letters(line) for line in inp_lines])
