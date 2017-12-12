with open("input") as file:
    lines = [line.split(" <-> ")[1] for line in file.read().splitlines()]
    node_list = [map(lambda x: int(x), line.split(", ")) for line in lines]
    connected_set = set([0])
    last_len = 0
    while len(connected_set) > last_len:
        last_len = len(connected_set)
        for node in connected_set.copy():
            for conn in node_list[node]:
                connected_set.add(conn)
    print(len(connected_set))