class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_vec(r: List[str]) -> bool:
            nums = "123456789"
            for s in r:
                if s == ".":
                    continue
                if s in nums:
                    nums = nums.replace(s, "", 1)
                    continue
                # if we get here, a condition failed
                return False

            return True
        
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
