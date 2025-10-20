def state_key(grid):
    return tuple(tuple(row) for row in grid)

def detect_loop(seen, grid, turn):
    key = state_key(grid)
    if key in seen:
        start = seen[key]
        period = turn - start
        return True, start, period
    else:
        seen[key] = turn
        return False, None, None
    