
def earliest_ancestor(ancestors, starting_node):
    s = []
    s.append(starting_node)
    v = set()

    children = []
    for ancestor in ancestors:
        children.append(ancestor[1])
    if starting_node not in children:
        return -1

    while len(s) > 0:
        node = s.pop()
        if node not in v:
            v.add(node)
            for ancestor in ancestors:
                if ancestor[1] == node:
                    s.append(ancestor[0])
    return node