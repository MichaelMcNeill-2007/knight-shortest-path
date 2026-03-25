import heapq


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        return self.frontier.pop()


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")

        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node


class PriorityFrontier:
    def __init__(self):
        self.frontier = []
        self.counter = 0

    def add(self, node, priority):
        heapq.heappush(self.frontier, (priority, self.counter, node))
        self.counter += 1

    def contains_state(self, state):
        return any(item[2].state == state for item in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        _, _, node = heapq.heappop(self.frontier)
        return node