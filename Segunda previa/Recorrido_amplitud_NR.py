def bfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return "Invalid input"

    path = []
    stack = [source]
    while(len(stack) != 0):
        s = stack.pop(0)

        if s not in path:
            path.append(s)

        if s not in graph:
            #leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)
        print(path)
        print(stack)
    return " ".join(path)

if __name__ == "__main__":
    # Lista de Adyacencia
    graph = {"A":["B","C","D"],
    "B":["E"],
    "C":["F","G"],
    "D":["H"],
    "E":["I"],
    "F":["J"]}
    
    # Recorrido completo en amplitud del grafo
    BFS_path = bfs_non_recursive(graph, "A")
    print(BFS_path)