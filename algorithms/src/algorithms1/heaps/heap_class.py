class BinaryHeap:
    def __init__(self):
        self._heap = []

    # insert item to end of heap
    # then correct its position
    def insert(self,item):
        self._heap.append(item)
        self.correct_item_post(node_position=len(self._heap)-1)
        # self._perc_up(len(self._heap)-1)

    def correct_item_post(self,node_position):
        # new node position
        child_position = node_position

        # when do we stop? we stop looping until new node is below its parent - ie for min heap. the reverse for max heap
        parent_position = (child_position-1)//2
        while self._heap[parent_position]>self._heap[child_position] and parent_position>=0:
            # swap values
            self._heap[parent_position],self._heap[child_position] = self._heap[child_position],self._heap[parent_position]

            child_position = parent_position
            parent_position = (child_position-1)//2

    def delete(self):
        # get the min value
        min_value = self._heap[0]

        # swap first and last element
        self._heap[0] = self._heap[len(self._heap)-1]
        # pop the last element
        self._heap.pop()

        # correct list to look at heap
        self.correct_heap(parent_position=0)
        return min_value

    def correct_heap(self,parent_position):

        # compute child node positions
        lcp = 2*parent_position + 1
        rcp = 2*parent_position + 2
        print("lcp,rcp",lcp,rcp)
        heap_size = len(self._heap)
        # get minimum value btw child nodes
        if lcp < heap_size and rcp< heap_size:
            child_position = lcp if self._heap[lcp] == min(self._heap[lcp],self._heap[rcp]) else rcp
        elif lcp > heap_size and rcp<heap_size:
            child_position = rcp
        elif lcp < heap_size and rcp>heap_size:
            child_position = lcp
        else:
            child_position = None
        # print("parent",parent_position, self._heap[parent_position])
        # print("child",child_position, self._heap[child_position])
        if child_position is not None:
            if self._heap[parent_position]>self._heap[child_position]:
                # swap parent and child
                self._heap[parent_position],self._heap[child_position] = self._heap[child_position],self._heap[parent_position]
                # rerun function on the new parent position
                self.correct_heap(child_position)

    def heapify(self, my_new_list):
        self._heap = my_new_list[:] ## creates a new copy.
        index_2_work = len(self._heap)//2-1
        while index_2_work>=0:
            self.correct_heap(index_2_work)
            index_2_work-=1

test1 = BinaryHeap()
test1._heap = [5,9,11,14,18,19,21,33,17,27]

test1.insert(7)

test1.insert(18)
test1._heap


test1.delete()


test1.heapify([9,6,5,2,3])
test1._heap