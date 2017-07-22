---
layout: post
title:  "LeetCode 348 - Design Tic Tac Toe"
date:   2017-07-16 00:15:02 -0400
categories: leetcode, Microsoft
---

# Design Tic Tac Toe

## 一刷

### 代码

类似dfs做法的版本
```java
public class TicTacToe {

    private int[][] board;
    
    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        board = new int[n][n];
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        board[row][col] = player;
        
        int[] xoffset = {0, 1, 1, 1};
        int[] yoffset = {1, 0, 1, -1};
        
        for(int i = 0; i < xoffset.length; i++){
            int resultNum = connectedNum(board, row, col, xoffset[i], yoffset[i]);

            if(resultNum == board.length){
                return player;
            }
        }

        
        return 0;
        
    }
    
    private int connectedNum(int[][] board, int row, int col, int xoffset, int yoffset){
        int connectedNum = 1;
        int rowTemp = row + xoffset;
        int colTemp = col + yoffset;
        while(rowTemp < board.length && colTemp < board[0].length 
              && rowTemp >= 0 && colTemp >= 0 && board[rowTemp][colTemp] == board[row][col]){
            connectedNum++;
            rowTemp += xoffset;
            colTemp += yoffset;
        }
        rowTemp = row - xoffset;
        colTemp = col - yoffset;
        while(rowTemp < board.length && colTemp < board[0].length && 
              rowTemp >= 0 && colTemp >= 0 && board[rowTemp][colTemp] == board[row][col]){
            connectedNum++;
            rowTemp -= xoffset;
            colTemp -= yoffset;
        }
        
        return connectedNum;
    }
    
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
```


leetcode discuss中O(1)时间复杂度的版本
```java
public class TicTacToe {
private int[] rows;
private int[] cols;
private int diagonal;
private int antiDiagonal;

/** Initialize your data structure here. */
public TicTacToe(int n) {
    rows = new int[n];
    cols = new int[n];
}

/** Player {player} makes a move at ({row}, {col}).
    @param row The row of the board.
    @param col The column of the board.
    @param player The player, can be either 1 or 2.
    @return The current winning condition, can be either:
            0: No one wins.
            1: Player 1 wins.
            2: Player 2 wins. */
public int move(int row, int col, int player) {
    int toAdd = player == 1 ? 1 : -1;
    
    rows[row] += toAdd;
    cols[col] += toAdd;
    if (row == col)
    {
        diagonal += toAdd;
    }
    
    if (col == (cols.length - row - 1))
    {
        antiDiagonal += toAdd;
    }
    
    int size = rows.length;
    if (Math.abs(rows[row]) == size ||
        Math.abs(cols[col]) == size ||
        Math.abs(diagonal) == size  ||
        Math.abs(antiDiagonal) == size)
    {
        return player;
    }
    
    return 0;
}
}
```

自己仿照的版本
```java
public class TicTacToe {

    private int[] rows;
    private int[] cols;
    private int diagnoal;
    private int antiDiagnoal;
    
    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        rows = new int[n];
        cols = new int[n];
        diagnoal = 0;
        antiDiagnoal = 0;
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int add = player == 1 ? 1 : -1;
        
        rows[row] += add;
        cols[col] += add;
        
        if(row == col){
            diagnoal += add;
        }
        
        if(row == cols.length - col - 1){
            antiDiagnoal += add;
        }
        
        int n = rows.length;
        
        if(Math.abs(rows[row]) == n || Math.abs(cols[col]) == n ||
          Math.abs(diagnoal) == n || Math.abs(antiDiagnoal) == n){
            return player;
        }
        
        return 0;
    }
    
    
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
```

### 笔记

最暴力的方法无疑就是先实例化一个int[][] board,然后设置一个checkWhoWin方法，每一次check都双层循环遍历一次整个二维数组检查有没有人赢，这样的move时间复杂度是O(n^2)的

进一步想，其实一个move之后，没有必要去检查整个数组，其实就只需要检查move所在的那一个点的行列和对角线总共四个方向就可以了，这样的move的时间复杂度是O(n)的。

这里自己的写法有些类似dfs遍历的写法，**只不过这里search是有方向的，所以不需要进行递归，只需要确定方向然后一直走到不连续或者尽头就可以**

其中要注意的是xoffset和yoffset的设置需要自己手动设置。并不是两层循环
for(int i = 0; i < board.length; i++){
    for(int j = 0; j < board[0].length; j++){
        ...
    }
}
当i和j为0时其实是没有方向的，而其实还会忽略1, -1这样的组合。所以对于遍历各个方向，应该自己手动枚举方向，然后配合**一层**循环来进行遍历。

而看了leetcode的discuss中的答案才发现还有更极简的做法: 因为我们关心的只是下完一步棋后有没有谁赢这个信息，而并不关心棋盘现在的各个位置上到底有没有子，有谁的子这个信息。所以我们可以进一步剔除掉冗余。

另外一个本题或者n x n的board需要注意的地方是:

长度为n的对角线只有两条，就是从[0,0]到[n - 1, n - 1]或者[0, n - 1]到[n - 1, 0]

其他斜着的方向就算是全连上了也不可能达到n个子相连。

而自己的程序中所有方向都是平等的，都会进行整个方向上的检查，所以会有不必要的冗余的检查。

leetcode中的版本的核心点在于:

由于不需要具体知道某个点是什么子，那么**只用一个int就能表示在某行或者某列上的势力情况**

所以，空间上来说只需要 n (row) + n (col) + 1(diagonal) + 1(antidiagonal)个空间就够了。

而对于move，只需要对于其所在的行和列的势力进行相应的加减，并且如果该move的点在两条对角线上的话，对对角线上的势力进行相应的加减。

最后判断是否某个"势力"完全占据了某一行或者某一列或者对角线即可。

这样move操作的时间复杂度能达到O(1)!
