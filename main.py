from node import Node
from search import StackFrontier, QueueFrontier, PriorityFrontier
from board import KnightBoard


def reconstruct_solution(board, node):
    actions = []
    cells = []

    while node.parent is not None:
        actions.append(node.action)
        cells.append(node.state)
        node = node.parent

    cells.append(node.state)
    actions.reverse()
    cells.reverse()

    board.solution = (actions, cells)


def solve_bfs(board, start, goal):
    board.num_explored = 0
    board.solution = None
    board.explored = set()

    start_node = Node(state=start, parent=None, action=None, cost=0)
    frontier = QueueFrontier()
    frontier.add(start_node)

    while True:
        if frontier.empty():
            raise Exception("No solution found.")

        node = frontier.remove()
        board.num_explored += 1

        if node.state == goal:
            reconstruct_solution(board, node)
            return

        board.explored.add(node.state)

        for action, state in board.neighbors(node.state):
            if not frontier.contains_state(state) and state not in board.explored:
                child = Node(
                    state=state,
                    parent=node,
                    action=action,
                    cost=node.cost + 1
                )
                frontier.add(child)


def solve_dfs(board, start, goal):
    board.num_explored = 0
    board.solution = None
    board.explored = set()

    start_node = Node(state=start, parent=None, action=None, cost=0)
    frontier = StackFrontier()
    frontier.add(start_node)

    while True:
        if frontier.empty():
            raise Exception("No solution found.")

        node = frontier.remove()
        board.num_explored += 1

        if node.state == goal:
            reconstruct_solution(board, node)
            return

        board.explored.add(node.state)

        for action, state in board.neighbors(node.state):
            if not frontier.contains_state(state) and state not in board.explored:
                child = Node(
                    state=state,
                    parent=node,
                    action=action,
                    cost=node.cost + 1
                )
                frontier.add(child)


def solve_astar(board, start, goal):
    board.num_explored = 0
    board.solution = None

    start_node = Node(state=start, parent=None, action=None, cost=0)
    frontier = PriorityFrontier()
    frontier.add(start_node, priority=board.heuristic(start, goal))

    best_cost = {start: 0}

    while True:
        if frontier.empty():
            raise Exception("No solution found.")

        node = frontier.remove()
        board.num_explored += 1

        if node.state == goal:
            reconstruct_solution(board, node)
            return

        for action, state in board.neighbors(node.state):
            new_cost = node.cost + 1

            if state not in best_cost or new_cost < best_cost[state]:
                best_cost[state] = new_cost
                child = Node(
                    state=state,
                    parent=node,
                    action=action,
                    cost=new_cost
                )
                priority = new_cost + board.heuristic(state, goal)
                frontier.add(child, priority=priority)


def print_path(board):
    if board.solution is None:
        print("No solution stored.")
        return

    actions, cells = board.solution

    print("\nPath:")
    print(" -> ".join(board.coords_to_notation(cell) for cell in cells))

    print("\nMoves:")
    for i, action in enumerate(actions, start=1):
        print(f"{i}. {action}")

    print(f"\nMoves required: {len(actions)}")
    print(f"States explored: {board.num_explored}")


def main():
    board = KnightBoard(size=8)

    print("Knight Shortest Path Solver")
    print("Enter squares like a1, b3, h8\n")

    start_input = input("Start square: ").strip()
    goal_input = input("Goal square: ").strip()
    algorithm = input("Algorithm (bfs/dfs/astar): ").strip().lower()

    if algorithm not in {"bfs", "dfs", "astar"}:
        print("Invalid algorithm. Defaulting to bfs.")
        algorithm = "bfs"

    try:
        start = board.notation_to_coords(start_input)
        goal = board.notation_to_coords(goal_input)
    except ValueError as e:
        print(f"Input error: {e}")
        return

    if start == goal:
        print("\nStart and goal are the same square.")
        print(f"Path: {start_input.lower()}")
        print("Moves required: 0")
        return

    try:
        if algorithm == "bfs":
            solve_bfs(board, start, goal)
        elif algorithm == "dfs":
            solve_dfs(board, start, goal)
        else:
            solve_astar(board, start, goal)
    except Exception as e:
        print(f"Solver error: {e}")
        return

    print_path(board)
    board.print_board_with_path()


if __name__ == "__main__":
    main()