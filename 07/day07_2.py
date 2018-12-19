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


num_elves = 5
elves = [{'node': None, 'timer': 0} for i in range(num_elves)]
print(elves)

unprocessed_nodes = set(nodes)
node_order = []
global_timer = -1
while set(node_order) != nodes:
    global_timer += 1
    working_elves = filter(lambda x: x['node'] is not None, elves)
    for elf in sorted(working_elves, key=lambda x: x['node']):
        elf['timer'] -= 1
        if elf['timer'] > 0:
            continue

        node_order.append(elf['node'])
        elf['node'] = None
        dependencies = filter(lambda x: x.left in node_order, dependencies)

    dependent_nodes = {d.right for d in dependencies}
    free_nodes = sorted(unprocessed_nodes - dependent_nodes)

    available_elves = filter(lambda x: x['node'] is None, elves)
    for elf in available_elves:
        if len(free_nodes) == 0:
            continue
        node = free_nodes.pop()
        elf['node'] = node
        elf['timer'] = ord(node) - 64
        unprocessed_nodes.remove(node)
    print(global_timer, elves)

print(global_timer, ''.join(node_order))