class Heap:

    def __init__(self, size=100):
        self.max_amount_of_elements = size
        self.memory = [(None, None) for _ in range(self.max_amount_of_elements + 1)]
        self.size = 0

    def __str__(self):
        res = ""
        for elem in self.memory[1:]:
            res = res + "priority: " + str(elem[0]) + ' - ' + str(elem[1]) + "\n"
        return res

    def insert(self, priority, element):

        def update():
            child_index = self.size
            parent_index = child_index >> 1
            while parent_index > 0 and self.memory[parent_index] > self.memory[child_index]:
                l_child_index = parent_index << 1
                r_child_index = l_child_index + 1
                min_child_index = \
                    l_child_index \
                    if not l_child_index ^ self.size or self.memory[l_child_index] < self.memory[r_child_index]\
                    else r_child_index
                self.memory[min_child_index], self.memory[parent_index] = \
                    self.memory[parent_index], self.memory[min_child_index]
                child_index = parent_index
                parent_index = child_index >> 1

        if self.size < self.max_amount_of_elements:
            self.size += 1
            self.memory[self.size] = (priority, element)
            update()
        else:
            raise MemoryError("no more memory")

    def extract_min(self):
        pass

