def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return "Invalid input"

    path = []
    stack = [source]
    T_paths = []
    doub=[]
    iter=0

    while(len(stack) != 0):
        count=0
        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph: 
            T_paths.append(path)
            iter+=1
            path=[source]

            if doub:
                if T_paths[iter-1][1] == doub[0]:
                    path.append(doub.pop(0))
            #leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor[0])
            count+=1
            if count > 1 and s != "A":
                doub.append(s)

    return T_paths

def values(graph, paths):
    values = []
    for p in paths:
        #Miro todos los posibles caminos
        T_valu = []
        i=0
        for g in graph:
            for v in graph[g]:
                #Miro los costos de cada conexion entre nodos
                if (v[0] == p[1]) or (v[0] == p[2]):
                    T_valu.append(v[1])
                    i+=1
                    if i == 2:
                        #Guardo en values ([camino,costos,ganancia,valor_total])
                        values.append([p,T_valu,T_valu[0] - T_valu[1],T_valu[0] + T_valu[1]])               
    return values
                
def filter(graph, options, source):
    stack = []
    posib = []
    best = []

    for neighbor in graph[source]:
            stack.append(neighbor[0])
            
    for s in stack:
        count = 0
        for o in options:
            if o[0][1] == s:
                if o[2] > 0:
                    count += 1
                elif o[2] < 0:
                    count -= 1
        posib.append([s,count])

    max = posib[0][1]
    for p in posib:
        if p[1] > max:
            max = p[1]

    for p in posib:
        if p[1] == max:
            for o in options:
                if o[0][1] == p[0]:
                    best.append(o)
    
    return best    


if __name__ == "__main__":
    # Lista de Adyacencia
    graph = {"A":[["E",1],["D",6],["C",2],["B",4]],
    "B":[["G",1],["F",2]],
    "C":[["I",1],["H",3]],
    "D":[["J",7]],
    "E":[["M",6],["L",2],["K",4]]}

    # posibles rutas
    paths = dfs_non_recursive(graph, "A")
    print(paths)

    options = values(graph,paths)

    print("Posibles: ")
    for o in options:
        print("(Ruta, costo_nodos, ganancia, Costo_total): ",o)
    
    best_options=filter(graph, options, "A")

    print("Mejores caminos")
    for b in best_options:
        print(b)
