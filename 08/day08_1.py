from dataclasses import dataclass


@dataclass()
class Node:
    children: list
    metadata: list

metadata_sum = 0

def extract_node(data: list):
    global metadata_sum
    node_count = data.pop(0)
    metadata_count = data.pop(0)
    children = [extract_node(data) for x in range(node_count)]
    metadata = [data.pop(0) for x in range(metadata_count)]
    metadata_sum += sum(metadata)
    return Node(children, metadata)


with open('input.txt') as f:
    data = f.read()

data = [int(d) for d in data.split()]

nodes = extract_node(data)

print(nodes)
print(metadata_sum)