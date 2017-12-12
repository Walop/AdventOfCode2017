def get_connected_set(node_list, initial):
    connected_set = set([initial])
    last_len = 0
    while len(connected_set) > last_len:
        last_len = len(connected_set)
        for node in connected_set.copy():
            for conn in node_list[node]:
                connected_set.add(conn)
    return connected_set

with open("input") as file:
    lines = [line.split(" <-> ")[1] for line in file.read().splitlines()]
    node_list = [map(lambda x: int(x), line.split(", ")) for line in lines]
    found_nodes = set()
    groups = 0
    for i in range(0, len(node_list)):
        if i not in found_nodes:
            connected_set = get_connected_set(node_list, i)
            found_nodes = found_nodes.union(connected_set)
            groups += 1
    print(groups)