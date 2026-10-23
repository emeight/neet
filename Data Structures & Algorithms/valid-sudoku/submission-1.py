class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_vec(r: List[str]) -> bool:
            # check for duplicates in set
            digits = [x for x in vec if x != "."]
            return len(digits) == len(set(digits))
        
        # consolidate all rows, cols, boxes into vecs
        vecs = []
        vecs.extend(board)

        cols = [list(col) for col in zip(*board)]
        vecs.extend(cols)

        boxes = []
        for r1 in [0, 3, 6]:
            for c1 in [0, 3, 6]:
                box = [val for row in board[r1:r1+3] for val in row[c1:c1+3]]
                boxes.append(box)
        vecs.extend(boxes)

        for vec in vecs:
            if not is_valid_vec(vec):
                return False
        return True
