class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[][] squares = new HashSet[3][3]; // key is row / 3 and column / 3
        
        for (int c = 0; c < 9; c++) {
            cols[c] = new HashSet<>();
        }

        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                squares[r][c] = new HashSet<>();
            }
        }

        for (int r = 0; r < 9; r++) {
            rows[r] = new HashSet<>();
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                if (rows[r].contains(board[r][c]) || cols[c].contains(board[r][c]) || squares[r / 3][c / 3].contains(board[r][c])) {
                    return false;
                }

                rows[r].add(board[r][c]);
                cols[c].add(board[r][c]);
                squares[r / 3][c / 3].add(board[r][c]);

            }
        }
        return true;
    }
}
