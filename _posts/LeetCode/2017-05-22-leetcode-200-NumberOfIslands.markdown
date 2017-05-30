---
layout: post
title:  "LeetCode 200 - Number of Islands"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Number of Islands

## 一刷

### 代码

version(经过看思路自己写的version):
```java
public class Solution {
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */
    public int numIslands(boolean[][] grid) {
        // Write your code here
        int islandCount = 0;
        
        if(grid == null || grid.length == 0){
            return islandCount;
        }
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j]){
                    islandCount++;
                    dfs(grid, i, j);
                }
            }
        }
        
        return islandCount;
        
    }
    
    private void dfs(boolean[][] grid, int row, int col){
        if(row < 0 || row > grid.length - 1 || col < 0 || col > grid[0].length - 1){
            return;
        }
        
        if(!grid[row][col]){
            return;
        }
        
        grid[row][col] = false;
        dfs(grid, row - 1, col);
        dfs(grid, row + 1, col);
        dfs(grid, row, col - 1);
        dfs(grid, row, col + 1);
        
    }
}
```

### 笔记

此题乍一看的时候感觉应该是dfs来做，但又不知道该如何展开。因为要求总共有多少陆地，感觉又有点像union find的感觉。看了别人的思路后恍然大悟。

思路其实很简单，就是用两遍for循环遍历整个2d array，一旦碰上一个岛屿的"第一块陆地"，就利用dfs将该岛屿整个“炸沉”。这样的话，接下来的遍历过程中就再不会碰到该岛屿的任何陆地，所以一旦碰到一个陆地并将其炸沉，就将count++。这样最后就能找到所有岛屿。

注意dfs中有两种情况都需要返回：
(1)已经是水而不是陆地。
(2)越过了边界

本题dfs的关键就在于能想到是所有能延伸的方向就是：上下左右，四个方法。
一开始疑惑因为遍历的方向是从上往下，从左往右，是不是就只用dfs右和下两个方向就好了？
不是，如果没有左放下的话，那么：
010
110
就不能一次完全炸沉

如果没有右方向没有想到，但是试验了下，在某个大数据的情况下数目是不对的。

最后，本来想不明白的一点是count如何在dfs这个函数中动态地改变，如果用Java，就必须使用全局静态变量
public static int islandCount.

但是自己分析就会发现，count的计算不需要再dfs中完成。dfs只需要完成“碰到一块陆地，就炸成整个岛屿”这一个功能就可以了。count放在遍历的过程中统计。

注意，该题中用到的就是纯粹的dfs，而不是Backtracking，并没有回溯的过程。

---

## 二刷

### 代码

```java
public class Solution {
    public int numIslands(char[][] grid) {
        
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return 0;
        }
        
        int resultNum = 0;
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == '1'){
                    resultNum++;
                    dfsHelper(grid, i, j);
                }
            }
        }
        
        return resultNum;
    }
    
    private void dfsHelper(char[][] grid, int row, int col){
        if(row < 0 || row >= grid.length || col < 0 || col >= grid[0].length){
            return;
        }
        
        if(grid[row][col] == '0'){
            return;
        }
        
        grid[row][col] = '0';
        
        dfsHelper(grid, row + 1, col);
        dfsHelper(grid, row, col + 1);
        dfsHelper(grid, row - 1, col);
        dfsHelper(grid, row, col - 1);
        
    }
}
```


### 笔记
一刷的笔记已经非常的清楚了，所以二刷几乎没费什么劲。
主要的核心思想就是:二层for循环遍历整个matrix，对于每一块陆地，**利用dfs进行连环炸岛**。

要注意的是dfs中的判断的顺序：
(1)先判断当前这一块是岛屿还是水，是水的话就无需继续dfs下去了，return。
(2)如果是岛屿的话，在进行recursively的进一步dfs之前，就需要先把当前块炸沉，否则就会陷入死循环中。

最后就是一个小小细节，leetcode中的matrix是char的，'1'和'0'代表岛和水。但是lintCode中是用boolean来表示的。