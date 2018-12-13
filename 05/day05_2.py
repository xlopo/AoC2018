def react_polymere(data: str, filter: list=None):
    result = list(data)

    i = 0
    while i < len(result):
        if i < 0:
            i = 0

        c = result[i]
        if c in filter:
            del result[i]
            i -= 1
            continue

        n = result[i+1] if i < len(result)-1 else None
        if n is not None and c != n and c.lower() == n.lower():
            del result[i]
            del result[i]
            i -= 1
            continue

        i += 1

    result = ''.join(result)
    return {'filter': filter, 'length': len(result), 'result': result}


def main():
    with open('input.txt') as f:
        data = f.read().strip()

    # data = 'dabAcCaCBAcCcaDA'

    filters = {c.lower() + c.upper() for c in set(data)}

    reactions = [react_polymere(data, filter=filter) for filter in sorted(filters)]

    print(min(reactions, key=lambda x: x['length']))


if __name__ == '__main__':
    main()
