# Knight shortest Path to Spot on Chess Board project (AI search project using content from Harvard's CS50 Intro to AI)

# Knight Shortest Path (AI Search Project)

- Built this project to apply core ideas from classical AI, specifically how to model real-world problems as search problems
- The goal is to compute the minimum number of moves a chess knight needs to travel between two squares
- Focused on designing a clean, generalizable solution rather than just solving the problem itself

---

## What I Focused On

- Built this project to strengthen my understanding of algorithmic problem solving and search
- Emphasis on:
  - structuring problems in a way a computer can reason about
  - separating logic from environment
  - understanding tradeoffs between different approaches
- Instead of jumping straight into machine learning, I focused on the **foundations that many ML systems rely on**, such as search and optimization

---

## Problem Formulation

- This problem is modeled as a **search problem**

- Key components:
  - **State**
    - A square on the chessboard represented as `(row, column)`

  - **Initial State**
    - The starting square provided by the user

  - **Goal State**
    - The target square the knight must reach

  - **Actions**
    - All valid knight moves (8 possible transitions)

  - **Transition Model**
    - Applying a move results in a new state

  - **State Space**
    - All reachable squares on the board

  - **Goal Test**
    - Check if the current state equals the target square

  - **Path Cost**
    - Number of moves taken (each move has equal cost)

---

## Algorithms Implemented

### Breadth First Search (BFS)

- Explores the search space level by level
- Guarantees the **shortest path** because all moves have equal cost
- Ensures optimality
- Used as the primary solver

### Depth First Search (DFS)

- Explores deeper nodes first before backtracking
- May find a solution faster in some cases
- Does **not guarantee optimality**
- Included to compare behavior and understand tradeoffs

### A\* Search

- Expands the node with the lowest estimated total cost `f(n) = g(n) + h(n)`
- Uses path cost so far plus a heuristic estimate of distance remaining
- Demonstrates informed search and more efficient exploration

---

## Key Design Decisions

- Structured the project into separate components:
  - search logic
  - environment (board representation)
  - node abstraction

- Implemented a **Node class** tracks:
  - current state
  - parent node
  - action taken

- Used a **frontier + explored set** approach:
  - avoids revisiting states
  - prevents infinite loops
  - improves efficiency

- Designed the system so the **search algorithm is independent of the environment**
  - allows reuse for:
    - mazes
    - graphs
    - routing problems
    - game state exploration

---

## Output and Visualization

- The program outputs:
  - sequence of moves
  - number of moves required
  - number of states explored

- Includes a visual chessboard where:
  - each square in the path is labeled with its step number
  - helps visualize how the algorithm navigates the state space

---

## Example Run

```
Start square: a1
Goal square: h8
Algorithm (bfs/dfs): bfs
```

Output:

```
Moves required: 6
States explored: 34
```

Board visualization:

```
    a  b  c  d  e  f  g  h
8  .. .. .. .. .. .. ..  6
7  .. .. .. .. .. ..  5 ..
6  .. .. .. .. .. .. .. ..
5  .. ..  2 .. .. .. .. ..
4  .. .. .. .. .. .. .. ..
3  ..  1 .. .. .. .. .. ..
2  .. .. .. .. .. .. .. ..
1   0 .. .. .. .. .. .. ..

0 = start
6 = goal
```

---

## Why This Project Matters

- While not a machine learning model, this project focuses on something equally important:
  - **how to explore and optimize over a large space of possibilities**

- Many ML systems rely heavily on:
  - search
  - optimization
  - decision trees
  - state exploration

- This project builds intuition for:
  - avoiding redundant computation
  - balancing speed vs optimality
  - designing efficient traversal strategies

- Reinforces that strong ML engineers:
  - understand algorithms deeply
  - can model problems clearly
  - think about tradeoffs and performance

---

## What I Learned

- How to translate a real-world problem into a formal search problem
- Differences between BFS and DFS in practice
- Importance of tracking explored states
- How to structure code for modularity and reuse
- How to reason about performance in terms of:
  - states explored
  - optimality
  - computational efficiency

---

## Possible Improvements

- Implement A\* search with heuristics
- Support custom board sizes (NxN)
- Add obstacles for more complex environments
- Build a graphical UI instead of terminal output
- Benchmark algorithm performance more formally

---

enter:

- start square (e.g., `a1`)
- goal square (e.g., `h8`)
- algorithm (`bfs` or `dfs`)

---

## Author

Michael McNeill

## Notes

- Some implementation details and structure were refined with the help of AI tools for learning purposes
