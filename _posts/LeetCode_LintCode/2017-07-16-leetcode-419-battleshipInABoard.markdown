---
layout: post
title:  "LeetCode 419 - Battleships in a Board"
date:   2017-07-16 00:15:02 -0400
categories: leetcode, Microsoft
---

# Battleships in a Board

## 一刷

### 代码

根据number of islands想到的版本
```java
public class Solution {
    public int countBattleships(char[][] board) {
        
        if(board == null || board.length == 0 || board[0].length == 0){
            return 0;
        }
        
        int num = 0;
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 'X'){
                    num++;
                    markBattleShip(board, i, j);
                }
            }
        }
        
        return num;
        
    }
    
    private void markBattleShip(char[][] board, int row, int col){
        
        board[row][col] = '.';
        
        while(row + 1 < board.length && board[row + 1][col] == 'X'){
            board[row + 1][col] = '.';
            row++;
        }
        
        while(col + 1 < board[0].length && board[row][col + 1] == 'X'){
            board[row][col + 1] = '.';
            col++;
        }
        
    }
}
```

自己的，利用不能相邻条件更简单的版本
```java
public class Solution {
    public int countBattleships(char[][] board) {
        
        if(board == null || board.length == 0 || board[0].length == 0){
            return 0;
        }
        
        int num = 0;
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 'X'){
                    
                    if((i == 0 || board[i - 1][j] != 'X') && (j == 0 || board[i][j - 1] != 'X')){
                        num++;
                    }
                    
                }
            }
        }
        
        return num;
        
    }
}
```

leetcode discuss中和上一个版本思路一样，但是写法更清晰不容易出错的版本
```java

    public int countBattleships(char[][] board) {
        int m = board.length;
        if (m==0) return 0;
        int n = board[0].length;
        
        int count=0;
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == '.') continue;
                if (i > 0 && board[i-1][j] == 'X') continue;
                if (j > 0 && board[i][j-1] == 'X') continue;
                count++;
            }
        }
        
        return count;
    }
```

### 笔记

首先感觉这题和number of islands很像，肯定能用dfs解决。但是仔细一想，battle ship只可能是横着的或者竖着的，所以其实都不用递归，一个直接while循环就可以。就有了自己的第一个版本

因为题目中说`Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?`
所以就用了和number of islands同样的思路，这次从炸岛变成炸船，把已经处理过的部分变成'.'即可。

如果没有只是用O(1) extra memory的要求并且不能动原board的话，就需要一个boolean[][] visited来进行记录。


然后看了网上的分析后发现其实这题的关键条件就在于**两个battleship不会相邻，横竖都不会**，那么也就是说，每个battleship的"头"的左边和上边都肯定不会是X。所以我们只要去数battleship的头就可以了。

leetcode的版本比自己巧妙的地方是:
筛去不合理的条件，剩下的就是"船头"。
而自己的思路是直接找出是船头的条件。


