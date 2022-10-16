def solution(m, n, board):
    answer = 0
    blocks_to_be_removed = set()
    def mark_blocks_to_be_removed():
        def is_removable(r, c):
            return board[r][c] != " " and board[r][c] == board[r][c + 1] == board[r + 1][c] == board[r + 1][c + 1]
        for r in range(m - 1):
            for c in range(n - 1):
                if is_removable(r, c):
                    blocks_to_be_removed.update([(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)])
                    print(blocks_to_be_removed)
    def remove_blocks():
        for (r, c) in blocks_to_be_removed:
            board[r] = board[r][:c] + " " + board[r][c + 1:]
        print(board)

    def drop_blocks():
        for c in range(n):
            left_blocks = []
            for r in range(m - 1, -1, -1):
                print(f"{r}, {c}, {board[r]}")
                if board[r][c]:
                    left_blocks.append(board[r][c])
            i = 0
            for r in range(m - 1, -1, -1):
                board[r] = board[r][:c] + left_blocks[i] if left_blocks[i] else " " + board[r][c + 1:]
                i += 1

    while(True):
        mark_blocks_to_be_removed()
        if not blocks_to_be_removed:
            break
        remove_blocks()
        drop_blocks()
        answer += len(blocks_to_be_removed)
        blocks_to_be_removed.clear()
    return answer

if __name__ == '__main__':
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    solution(m,n,board)