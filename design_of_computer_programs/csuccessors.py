def mc_problem2(start=(3,3,1,0,0,0), goal=None):
    if goal is None:
        goal = (0,0,0) + start[:3]
    return shortest_path_search(start, csuccessors, all_gone)

def all_gone(state): return state[:3] == (0,0,0)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    # import pdb; pdb.set_trace()
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return False

def is_goal(state):
    if state == 8:
        return True
    else:
        return False


def successors(state):
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors

def csuccessors(state):
    M1, C1, B1, M2, C2, B2 = state
    ## Check for state with no successors
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    if B1 > 0:
        items += [(sub(state, delta), a + '->')
                  for delta, a in deltas.items()]
    if B2 > 0:
        items += [(sub(state, delta), '<-' + a)
                  for delta, a in deltas.items()]

    return dict(items)

deltas = {
    (2, 0, 1,   -2, 0, -1): 'MM',
    (0, 2, 1,   0, -2, -1): 'CC',
    (1, 1, 1,   -1, -1, -1): 'MC',
    (1, 0, 1,   -1, 0, -1): 'M',
    (0, 1, 1,   0, -1, -1): 'C',
}

def add(X, Y):
    "add two vectors, X and Y"
    return tuple(x+y for x,y in zip(X,Y))

def sub(X, Y):
    "add two vectors, X and Y"
    return tuple(x-y for x,y in zip(X,Y))