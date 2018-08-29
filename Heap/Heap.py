class MinHeap:

    def __init__(self, size=100):
        self.max_amount_of_elements = size
        self.memory = [(None, None) for _ in range(self.max_amount_of_elements)]
        self.size = 0

    def __str__(self):
        res = ""
        for elem in self.memory:
            res = res + "priority: " + str(elem[0]) + ' - ' + str(elem[1]) + "\n"
        return res

    def insert(self, priority, element):

        def update():
            child_index = self.size - 1
            parent_index = (child_index - 1) >> 1
            if self.size > 1:
                while self.memory[parent_index] > self.memory[child_index]:
                    l_chld_ind = (parent_index << 1) + 1
                    r_chld_ind = l_chld_ind + 1
                    min_child_index = \
                        l_chld_ind \
                        if not l_chld_ind ^ (self.size - 1) or self.memory[l_chld_ind] < self.memory[r_chld_ind]\
                        else r_chld_ind
                    self.memory[min_child_index], self.memory[parent_index] = \
                        self.memory[parent_index], self.memory[min_child_index]
                    child_index = parent_index
                    parent_index = child_index >> 1

        if self.size < self.max_amount_of_elements:
            self.memory[self.size] = (priority, element)
            self.size += 1
            update()
        else:
            raise MemoryError("no more memory")

    def extract_min(self):

        min_priority = self.memory[0]
        last_el_ind = self.size - 1
        self.size -= 1

        parent_index = 0
        while parent_index != last_el_ind:
            l_chld_ind = (parent_index << 1) + 1
            r_chld_ind = l_chld_ind + 1
            if r_chld_ind <= self.size:
                if self.memory[l_chld_ind] <= self.memory[r_chld_ind] and self.memory[l_chld_ind] < self.memory[last_el_ind]:
                    min_child_index = l_chld_ind
                elif self.memory[r_chld_ind] < self.memory[l_chld_ind] and self.memory[r_chld_ind] < self.memory[last_el_ind]:
                    min_child_index = r_chld_ind
            else:
                min_child_index = last_el_ind

            self.memory[parent_index] = self.memory[min_child_index]
            parent_index = min_child_index

        self.memory[self.size] = (None, None)
        return min_priority


