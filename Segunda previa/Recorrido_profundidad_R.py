def recursive_dfs(graph, source,path = []):

    if source not in path:
        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[source]:
            print(path)
            path = recursive_dfs(graph, neighbour, path)
    
    return path

if __name__ == "__main__":
    graph = {"A":["B","C", "D"],
            "B":["E"],
            "C":["F","G"],
            "D":["H"],
            "E":["I"],
            "F":["J"]}

    path = recursive_dfs(graph, "A")
    print(" ".join(path))