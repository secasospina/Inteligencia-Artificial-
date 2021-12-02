def bfs_non_recursive(graph, source, value):
    if source is None or source not in graph:
        return "Invalid input"
    
    if value is None or value not in graph:
        return "Invalid input"

    path = []
    stack = [source]
    s = None

    while(len(stack) != 0) and (s != value):
        s = stack.pop(0)

        if s not in path:
            path.append(s)

        if s not in graph:
            #leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)
    return " ".join(path)

if __name__ == "__main__":
    # Lista de Adyacencia
    graph = {"A":["B","C","D"],
    "B":["E"],
    "C":["F","G"],
    "D":["H"],
    "E":["I"],
    "F":["J"],
    }
    
    # Recorrido completo en amplitud del grafo
    DFS_path = bfs_non_recursive(graph, "A","G")
    print(DFS_path)