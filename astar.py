class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp_puz[x1][y1], temp_puz[x2][y2] = temp_puz[x2][y2], temp_puz[x1][y1]
            return temp_puz
        else:
            return None

    def copy(self, root):
        return [list(row) for row in root]

    def find(self, puz, x):
        for i in range(len(puz)):
            for j in range(len(puz)):
                if puz[i][j] == x:
                    return i, j

class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puz = []
        for _ in range(self.n):
            temp = input().split()
            puz.append(temp)
        return puz

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        return sum(1 for i in range(self.n) for j in range(self.n) if start[i][j] != goal[i][j] and start[i][j] != '_')

    def process(self):
        print("Enter the initial state matrix \n")
        start = [['_', '2', '3'], ['1', '4', '5'], ['7', '8', '6']]
        print("\nInitial State:")
        for row in start:
            print(" ".join(row))

        goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']]
        print("\nGoal State:")
        for row in goal:
            print(" ".join(row))

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("\nCurrent State:")
            for i in cur.data:
                print(" ".join(i))
            if self.h(cur.data, goal) == 0:
                print("\nGoal State Reached!")
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval)


puz = Puzzle(3)
puz.process()
