def toys(w):
    w.sort()
    containers=1
    limit=w[0]+4
    for weight in w:
        if weight > limit:
            containers += 1
            limit = weight + 4
    return containers
