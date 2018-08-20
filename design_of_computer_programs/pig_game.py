import random

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    p, me, you, pending = state
    return (other[p], you, me + pending, 0)


def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    p, me, you, pending = state
    if d == 1:
        state = (other[p], you, me + d, 0)
    else:
        state = (p, me, you, pending + d)
    return state

other = {1:0, 0:1} # mapping from player to other player

def test():
    assert hold((1, 10, 20, 7)) == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10)) == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'
print(roll((0, 5, 15, 10), 5))
print(test())

def hold_at(x):
    """Return a strategy that holds if and only if
    pending >= x or player reaches goal."""
    def strategy(state):
        p, me, you, pending = state
        if pending >= x or me + pending >= 50:
            return 'hold'
        else:
            return 'roll'
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy

goal = 50

def play_pig(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0)
    while True:
        p, me, you, pending = state
        if me >= goal:
            return strategies[p]
        elif you >= goal:
            return strategies[other[p]]
        elif strategies[p](state) == 'hold':
            state = hold(state)
        else:
            state = roll(state, next(dierolles))

def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

def test1():
    # ここでtupleをstateの引数へ渡してる？
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    assert hold_at(15)((0, 2, 30, 10))  == 'roll'
    assert hold_at(15)((0, 2, 30, 15))  == 'hold'
    return 'tests pass'

def test2():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests pass'

def test3():
    A, B = hold_at(50), clueless
    rolls = iter([6,6,6,6,6,6,6,6,2]) # <- Total:50
    assert play_pig(A, B, rolls) == A
    return 'test passes'
