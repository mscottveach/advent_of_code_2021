from graph_tools import Graph


def dfs(g, previous_node, current_node, end_node, path_so_far):
    count = 0
    if current_node == end_node:
        print('End node found from ', previous_node, path_so_far)
        return 1
    children = g.successors(current_node)
    #print(current_node, ' -> ', children)
    path_so_far.append(current_node)
    print(path_so_far)
    for node in children:
        if (node.isupper()) | (node not in path_so_far):
            count += dfs(g, current_node, node, end_node, path_so_far.copy())

    return count

def dfs_doubleup(g, special_node, previous_node, current_node, end_node, path_so_far):
    count = 0
    if current_node == end_node:
        if path_so_far.count(special_node) == 2:
            print('End node found from ', previous_node, path_so_far)
            return 1
        else:
            return 0
    children = g.successors(current_node)
    #print(current_node, ' -> ', children)
    path_so_far.append(current_node)
    print(path_so_far)
    for node in children:
        if (node.isupper()) | (node not in path_so_far) | ((node == special_node) & (path_so_far.count(node) <= 1)):
            count += dfs_doubleup(g, special_node, current_node, node, end_node, path_so_far.copy())

    return count

def build_graph():
    g = Graph(directed=True)
    path_so_start = []

    with open('12-1-input.txt') as f:
        line = f.readline()
        while line:
            u,v = (line.strip()).split('-')
            if (u != 'end') & (v != 'start'):
                g.add_edge(u, v)
            if (v != 'end') & (u != 'start'):
                g.add_edge(v, u)
            line = f.readline()

        print(g)
        paths = dfs(g, '', 'start', 'end', path_so_start)
        print(paths)

        vertices = g.vertices()
        for vertex in vertices:
            if vertex.islower():
                paths += dfs_doubleup(g, vertex, '', 'start', 'end', path_so_start)
        print(paths)

if __name__ == '__main__':
    build_graph()