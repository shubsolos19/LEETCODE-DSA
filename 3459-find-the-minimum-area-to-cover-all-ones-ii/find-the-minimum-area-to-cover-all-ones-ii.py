class Rectangle:
    def __init__(self,):
        self.min_i = float('inf')
        self.max_i = -float('inf')
        self.min_j = float('inf')
        self.max_j = -float('inf')
    
    def add_pt(self, i, j):
        self.min_i = min(self.min_i, i)
        self.max_i = max(self.max_i, i)
        self.min_j = min(self.min_j, j)
        self.max_j = max(self.max_j, j)
    
    def find_area(self,):
        return (self.max_i - self.min_i + 1) * (self.max_j - self.min_j + 1)

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # 3 line split
        def h_split(mat):
            min_area = float('inf')
            # first partition: [0, len(mat)-3]
            for i in range(len(mat)-2):
                # second partition [len(mat)-2, i+1]
                # third partition: [i+2, len(mat)-1]
                for j in range(i+2, len(mat)):
                    partitions = [Rectangle() for _ in range(3)]

                    for k in range(len(mat)):
                        for l in range(len(mat[k])):
                            if mat[k][l] != 1:
                                continue
                            if k <= i:
                                partitions[0].add_pt(k,l)
                            elif i+1 <= k < j:
                                partitions[1].add_pt(k,l)
                            else:
                                partitions[2].add_pt(k,l)

                    area = 0
                    for r in partitions:
                        partition_area = r.find_area()
                        if partition_area == 0:
                            area = float('inf')
                            break
                        area+=partition_area
                    min_area = min(min_area, area)
                
            return min_area

        # mouse split
        def m_split(mat):
            min_area = float('inf')
            # long line partition (top partition): [0, len(mat)-2]
            for i in range(len(mat)-1):
                # orthogonal short line partition
                # let j represent the largest index of left partition
                for j in range(len(mat[0])-1):
                    partitions = [Rectangle() for _ in range(3)]

                    for k in range(len(mat)):
                        for l in range(len(mat[k])):
                            if mat[k][l] != 1:
                                continue
                            if k <= i:
                                partitions[0].add_pt(k,l)
                            elif l <= j:
                                partitions[1].add_pt(k,l)
                            else:
                                partitions[2].add_pt(k,l)
                    
                    area = 0
                    for r in partitions:
                        partition_area = r.find_area()
                        if partition_area == 0:
                            area = float('inf')
                            break
                        area+=partition_area
                    min_area = min(min_area, area)
            
            return min_area
        
        min_area = float('inf')
        horizontal = h_split(grid)
        vertical = h_split(list(zip(*grid[::-1])))
        min_area = min(min_area, horizontal, vertical)

        curr_grid = grid
        for i in range(4):
            rot_area = m_split(curr_grid)
            min_area = min(min_area, rot_area)
            curr_grid = list(zip(*curr_grid[::-1]))
        
        return min_area