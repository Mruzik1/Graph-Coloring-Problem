# file_path should a form of a path: "./file_name.txt" or "./containing_folder/file_name.txt"
# returns a list with connections between nodes
def read_example(file_path):
    with open(file_path) as fp:
        raw_connections = [i.split() for i in fp.read().split('\n') if len(i) != 0]
        return [[int(i[0]), int(i[1])] for i in raw_connections]


# gets a list from read_example as a parameter
# returns nodes (uses as a max colors count sometimes) and all node connections (as a dictionary)
def process_raw_connections(raw_connections):
    # set uses to remove duplicates
    nodes = list({i for sublist in raw_connections for i in sublist})
    connections = {i: [] for i in nodes}

    for i in raw_connections:
        connections[i[0]].append(i[1])
        connections[i[1]].append(i[0])

    # I forgot this one
    nodes.sort(key=lambda x: len(connections[x]), reverse=True)

    return nodes, connections


# finds a sequence of colors which are suitable for a node
# node_connections (list) - all nodes that are connected to a certain node
# already colored - a dictionary with already colored nodes
# colors - all possible colors
def find_color(node_connections, already_colored, colors):
    forbidden_colors = {already_colored[i] for i in node_connections}
    
    return min(set(colors)-forbidden_colors)


# colors a graph
def color_graph(nodes, connections):
    colored = {i: 0 for i in nodes}

    for i in nodes:
        colored[i] = find_color(connections[i], colored, nodes)
    
    return colored


# saves a graph to a certain file
def save_graph(file_path, colored_graph):
    with open(file_path, 'w') as fp:
        for i in sorted(colored_graph):
            fp.write(f'{i} {colored_graph[i]}\n')


# here we work with the functions
if __name__ == '__main__':
    raw_connections = read_example('./example3.txt')
    nodes, connections = process_raw_connections(raw_connections)
    colored_graph = color_graph(nodes, connections)
    
    save_graph('./result.txt', colored_graph)