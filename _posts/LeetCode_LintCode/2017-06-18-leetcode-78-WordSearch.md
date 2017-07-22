---
layout: post
title:  "LeetCode 78 - word search"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Microsoft, Amazon
---

# Word Search

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

```java
public class Solution {
    public boolean exist(char[][] board, String word) {
        
        if(board == null || board.length == 0 || word == null){
            return false;
        }
        
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(backtracking(board, word, i, j, 0)){
                    return true;
                }
            }
        }
        
        return false;
        
    }
    
    private boolean backtracking(char[][] board, String word, int row, int col, int index){
        
        if(row < 0 || row > board.length - 1 || col < 0 || col > board[0].length - 1){
            return false;
        }
        
        if(index > word.length() - 1){
            return false;
        }
        
        if(board[row][col] != word.charAt(index)){
            return false;
        }
        
        if(index == word.length() - 1){
            return true;
        }
        
        char temp = board[row][col];
        board[row][col] = '#';
        
        if(backtracking(board, word, row + 1, col, index + 1) || 
        backtracking(board, word, row, col + 1, index + 1) ||
        backtracking(board, word, row - 1, col, index + 1) ||
        backtracking(board, word, row, col - 1, index + 1)
            ){
            return true;
        }
        
        board[row][col] = temp;
        
        return false;
    }
}
```


### 笔记

0. 在解这题的时候一定要问清楚两个问题:(1)是否可以重复使用字符？(2)是方向确定了就不能再改了吗 (3)有哪几个方向?

(1)如果可以重复使用字符，那甚至就不是Backtracking了，就是纯无状态的dfs，
程序中对于
```java
char temp = board[row][col];
        board[row][col] = '#';
...

board[row][col] = temp;
```

就不需要了

而如果可以随意走的话则需要知道哪些地方已经被走过了，而其实可以巧妙地将被走过的地方设置成"#"这样的特殊字符，等回溯的时候再换回来即可，这个思路是来自于
<http://www.programcreek.com/2014/06/leetcode-word-search-java/>

(2)确定方向就不能改了的话程序就会简化很多，完全就不是dfs了，几层循环就能解决。见<http://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/>

(3) 如果方向很多，比如8个方向，可以使用两个一维数组配合表示方向，再配合一个for循环来循环8次即可。

1. 这题属于Backtracking中少见的需要返回值的，这是因为该问题只问了是否有存在的情况，使用返回值可以有效剪枝，如果问具体所有的情况，那返回值就会没用。

2. 注意这回因为要以所有的二维数组中的字符为起点，所以在主method中就需要双重循环，来调用backtraking方法。

3. 注意边界条件的检查中还需要判断index是否超过了word的长度
