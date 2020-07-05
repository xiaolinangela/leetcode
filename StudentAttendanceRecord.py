def record(s):
    count = 0
    for char in s:
        if char == 'A':
            count += 1
    return count < 2 and 'LLL' not in s


if __name__ == "__main__":
    s = 'LLAPL'
    print(record(s))
