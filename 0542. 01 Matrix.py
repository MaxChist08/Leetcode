class NewElem:
    def __init__ (self, data = 0):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__ (self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_elem = NewElem(data)
        if self.head is None:
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem.prev = self.tail
            self.tail.next = new_elem
            self.tail = new_elem

    def remove(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            element = self.head.data
            self.head = None
            self.tail = None
        else:
            element = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
        return element

def update_matrix(mat):
    ans = list()
    used = list()
    for i in range(len(mat)):
        ans.append(list())
        used.append(list())
        for j in range(len(mat[0])):
            ans[-1].append(10000)
            used[-1].append(0)

    width_search = Queue()
    len_ws = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                width_search.insert((i, j, 0))
                used[i][j] = 1
                len_ws += 1

    while len_ws != 0:
        elem = width_search.remove()
        len_ws -= 1
        ans[elem[0]][elem[1]] = elem[2]
        if elem[0] > 0 and used[elem[0] - 1][elem[1]] == 0:
            width_search.insert((elem[0] - 1, elem[1], elem[2] + 1))
            used[elem[0] - 1][elem[1]] = 1
            len_ws += 1
        if elem[1] > 0 and used[elem[0]][elem[1] - 1] == 0:
            width_search.insert((elem[0], elem[1] - 1, elem[2] + 1))
            used[elem[0]][elem[1] - 1] = 1
            len_ws += 1
        if elem[0] < len(mat) - 1 and used[elem[0] + 1][elem[1]] == 0:
            width_search.insert((elem[0] + 1, elem[1], elem[2] + 1))
            used[elem[0] + 1][elem[1]] = 1
            len_ws += 1
        if elem[1] < len(mat[0]) - 1 and used[elem[0]][elem[1] + 1] == 0:
            width_search.insert((elem[0], elem[1] + 1, elem[2] + 1))
            used[elem[0]][elem[1] + 1] = 1
            len_ws += 1

    return ans
