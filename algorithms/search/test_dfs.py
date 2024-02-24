from algorithms.search.dfs import dfs_stack

def test_dfs_stack():
    # Test case 1: Graph with 3 vertices
    graph1 = {
        'A': {'B', 'C'},
        'B': {'A', 'C'},
        'C': {'A', 'B'}
    }
    start1 = 'A'
    expected1 = {'A', 'B', 'C'}
    assert dfs_stack(graph1, start1) == expected1

    # Test case 2: Graph with 4 vertices
    graph2 = {
        'A': {'B', 'C'},
        'B': {'A', 'C', 'D'},
        'C': {'A', 'B'},
        'D': {'B'}
    }
    start2 = 'A'
    expected2 = {'A', 'B', 'C', 'D'}
    assert dfs_stack(graph2, start2) == expected2

    # Test case 3: Graph with 5 vertices
    graph3 = {
        'A': {'B', 'C'},
        'B': {'A', 'C', 'D'},
        'C': {'A', 'B'},
        'D': {'B', 'E'},
        'E': {'D'}
    }
    start3 = 'A'
    expected3 = {'A', 'B', 'C', 'D', 'E'}
    assert dfs_stack(graph3, start3) == expected3

    print("All test cases pass")

test_dfs_stack()
