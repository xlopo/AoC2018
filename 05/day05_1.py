def react_polymere(data: str):
    result = list(data)

    i = 0
    while i < len(result):
        if i < 0:
            i = 0

        c = result[i]
        n = result[i+1] if i < len(result)-1 else None

        if n is not None and c != n and c.lower() == n.lower():
            del result[i]
            del result[i]
            i -= 1
            continue

        i += 1

    result = ''.join(result)
    return result


def main():
    with open('input.txt') as f:
        data = f.read().strip()

    result = react_polymere(data)

    print(len(result))


if __name__ == '__main__':
    main()
