from dataclasses import dataclass


@dataclass()
class Node:
    children: list
    metadata: list
    value: int


def extract_node(data: list):
    node_count = data.pop(0)
    metadata_count = data.pop(0)
    children = [extract_node(data) for x in range(node_count)]
    metadata = [data.pop(0) for x in range(metadata_count)]

    value = 0
    if len(children) == 0:
        value = sum(metadata)
    else:
        for i in metadata:
            try:
                child = children[i-1]
                value += child.value
            except IndexError:
                pass

    return Node(children, metadata, value)


with open('input.txt') as f:
    data = f.read()

data = [int(d) for d in data.split()]

tree = extract_node(data)

print(tree)
print(tree.value)