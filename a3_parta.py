#
#   Author: Nishit Gaurang Shah (ngshah3)
#
#   This is PART A of assignment 3
#   Tested using test_a3_parta.py
#   
#   Course : DAS456 NAA
#   Professor : Catherine Leung
#

class MinHeap:
    
    def __init__(self, arr=[]):
        self.heap = []
        for val in arr:
            self.insert(val)

    def insert(self, element):
        self.heap.append(element)
        self._bubble_up(len(self.heap) - 1)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def _bubble_up(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx >= 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._bubble_up(parent_idx)
            
    def _bubble_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        min_idx = idx
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
            min_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
            min_idx = right_child_idx
        if min_idx != idx:
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            self._bubble_down(min_idx)
