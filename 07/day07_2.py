import heapq
from collections import namedtuple

Edge = namedtuple('Edge', 'left right')


def process(num_elves: int, nodes, edges):
    workers = dict()
    nodes = set(nodes)
    order = []

    seconds = -1
    while len(order) != len(nodes):
        seconds += 1

        workers.update((node, timer - 1) for node, timer in workers.items())
        completed = sorted([node for node in workers if workers[node] == 0], reverse=True)
        for node in completed:
            print(f'{seconds:4}\t\tcompleted: {node}')
            del workers[node]
            order.append(node)

        dependents = {e.right for e in edges if e.left not in order}
        free_nodes = nodes - dependents - set(workers) - set(order)


        for node in heapq.nsmallest(num_elves - len(workers), free_nodes):
            print(f'{seconds:4}\t\tstarting work on {node}')
            workers[node] = ord(node) - 4

        print(f'{seconds:4}', workers, free_nodes, dependents, ''.join(order))

    print(''.join(order))




def main():
    with open('input.txt') as f:
        lines = f.readlines()

    dependencies = set()
    edges = set()
    for l in lines:
        l = l.split()
        left = l[1]
        right = l[7]

        dependencies.add(Edge(left, right))

        edges.add(left)
        edges.add(right)

    process(5, edges, dependencies)


if __name__ == '__main__':
    main()
