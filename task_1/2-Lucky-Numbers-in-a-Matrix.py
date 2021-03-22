class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = set()
        max_col = set()
        for row in matrix:
            min_row.add(min(row))
        t_matrix = map(list, zip(*matrix))
        for col in t_matrix:
            max_col.add(max(col))
        return min_row.intersection(max_col)