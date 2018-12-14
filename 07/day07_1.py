from collections import namedtuple

Node = namedtuple('Node', 'left right')

with open('input.txt') as f:
    lines = f.readlines()

dependencies = set()
nodes = set()
for l in lines:
    l = l.split()
    left = l[1]
    right = l[7]

    dependencies.add(Node(left, right))

    nodes.add(left)
    nodes.add(right)


node_order = []
while len(nodes) > 0:
    dependent_nodes = {d.right for d in dependencies}
    free_node = sorted(nodes - dependent_nodes)[0]
    nodes.remove(free_node)
    node_order.append(free_node)
    dependencies = set(filter(lambda x: x.left != free_node, dependencies))


print(''.join(node_order))