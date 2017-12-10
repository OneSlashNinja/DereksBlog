---
layout: post
title:  "leetcode 329 - Longest Increasing Path In A Matrix"
date:   2017-12-09 23:33:54.317330
categories: leetcode, Google
---

# Longest Increasing Path In A Matrix

## 一刷

### 代码

暴力Backtracking
```java
class Solution {
    
    private int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return 0;
        }
        
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        
        int longest = 0;
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                longest = Math.max(longest, dfsHelper(matrix, i, j, Integer.MIN_VALUE, visited));
            }
        }
        
        return longest;
    }
    
    private boolean isInBoard(int[][] matrix, int x, int y){
        if(x < 0 || x >= matrix.length || y < 0 || y >= matrix[0].length){
            return false;
        }
        return true;
    }
    
    private int dfsHelper(int[][] matrix, int x, int y, int lastNum, boolean[][] visited){
        if(!isInBoard(matrix, x, y) || visited[x][y] || matrix[x][y] <= lastNum){
            return 0;
        }
        //注意visited是指当前元素是否被visited，所以写在for循环外面，而不是里面
        visited[x][y] = true;
        
        int longest = 0;
        for(int i = 0; i < dirs.length; i++){
            int nx = x + dirs[i][0];
            int ny = y + dirs[i][1];
            
            int result = dfsHelper(matrix, nx, ny, matrix[x][y], visited);
            longest = Math.max(longest, result);
        }
        visited[x][y] = false;
        
        return longest + 1;
    }
}
```

使用memorization的Backtracking
```java
class Solution {
    
    private int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return 0;
        }
        
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        //cache[i][j]存储的是，从(i,j)点出发能够找到的longest path
        int[][] cache = new int[matrix.length][matrix[0].length];
        for(int[] elem : cache){
            Arrays.fill(elem, -1);
        }
        
        int longest = 0;
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                longest = Math.max(longest, dfsHelper(matrix, i, j, Integer.MIN_VALUE, visited, cache));
            }
        }
        
        return longest;
    }
    
    private boolean isInBoard(int[][] matrix, int x, int y){
        if(x < 0 || x >= matrix.length || y < 0 || y >= matrix[0].length){
            return false;
        }
        return true;
    }
    
    private int dfsHelper(int[][] matrix, int x, int y, int lastNum, boolean[][] visited, int[][] cache){
        if(!isInBoard(matrix, x, y) || visited[x][y] || matrix[x][y] <= lastNum){
            return 0;
        }
        
        if(cache[x][y] != -1){
            return cache[x][y];
        }
        
        //注意visited是指当前元素是否被visited，所以写在for循环外面，而不是里面
        visited[x][y] = true;
        
        int longest = 0;
        for(int i = 0; i < dirs.length; i++){
            int nx = x + dirs[i][0];
            int ny = y + dirs[i][1];
            
            int result = dfsHelper(matrix, nx, ny, matrix[x][y], visited, cache);
            longest = Math.max(longest, result);
        }
        visited[x][y] = false;
        
        //visited需要回溯，而cache不需要
        cache[x][y] = longest + 1;
        return longest + 1;
    }
}
```

改进版: 其实本题不需要visited, 并且cache也可以初始化为0版本
```java
class Solution {
    
    private int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return 0;
        }

        //cache[i][j]存储的是，从(i,j)点出发能够找到的longest path
        int[][] cache = new int[matrix.length][matrix[0].length];
        
        int longest = 0;
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                longest = Math.max(longest, dfsHelper(matrix, i, j, Integer.MIN_VALUE, cache));
            }
        }
        
        return longest;
    }
    
    private boolean isInBoard(int[][] matrix, int x, int y){
        if(x < 0 || x >= matrix.length || y < 0 || y >= matrix[0].length){
            return false;
        }
        return true;
    }
    
    private int dfsHelper(int[][] matrix, int x, int y, int lastNum, int[][] cache){

        //如果当前点的大小小于或者等于lastNum，那么就不满足要求了，返回0即可
        if(!isInBoard(matrix, x, y) || matrix[x][y] <= lastNum){
            return 0;
        }
        
        if(cache[x][y] != 0){
            return cache[x][y];
        }
        
        int longest = 0;
        for(int i = 0; i < dirs.length; i++){
            int nx = x + dirs[i][0];
            int ny = y + dirs[i][1];
            
            int result = dfsHelper(matrix, nx, ny, matrix[x][y], cache);
            longest = Math.max(longest, result);
        }
        
        cache[x][y] = longest + 1;
        return longest + 1;
    }
}
```

### 笔记

单看暴力backtracking版本的话，其实本题和**word search**可谓是非常非常相似(具体见word search的代码)。
都是在一个matrix里搜索符合某个条件的串，使用的整个代码的结构也是非常相似:
**主函数中遍历matrix中的每个位置，对每个位置都调用backtrackingHelper，最后汇总所有结果。**

但是本题和word search又有两个小细节非常不同，而这两个个小细节就是为什么该题能进一步优化的原因。

第一个细节就是，对于word search，**参数中有个index，来指示当前是在检测word中的哪一个字符。而这说明问题和其子问题是有层级之分的**，
**而该问题则没有这种层级之间的区别，所以每个问题和其子问题都是相对独立的，这也就是为什么可以cache某个问题以备其他问题复用**

第二个细节是后来发现的，就是该题其实visited也是不需要的，所以该题完全是无状态的，每个位置的结果不会再因为其他状态而变化，这也就是为什么该题能重复利用每个位置的计算结果

**而cache[i][j]中存储的就是从(i,j)点出发能够找到的longest path**

最后，看题解后发现需要注意的可以改进的两点是：
(1) 其实是不需要visited这个数组的，一开始使用visited是觉得需要避免"吃到自己的贪吃蛇"这种情况，但是思考后会发现**某个点是天然不会被重复visit的**，因为一个增序的序列肯定是不会返回到其中某个数字然后形成循环的，否则longest的长度就会是无限长了。
(2) 一开始觉得应该使用-1来代表"未计算"状态，但是cache[i][j]其实初始化为0即可，0因为不会被使用到(实际的值至少是1)，所以可以相当于模拟"未计算"状态

而该题如果暴力，时间复杂度是:O(2^(m+n)) （还是不清楚怎么算的），但是worst case出现在:

```
1 2 3 . . . n
2 3 . . .   n+1
3 . . .     n+2
.           .
.           .
.           .
m m+1 . . . n+m-1
```

而如果是使用了memorization，那么每个点就只会计算一次，所以直接时间复杂度降为:O(m*n)

使用memorization的版本的空间是O(m*n),被cache所占。

而不是用memorization的版本的空间注意也是**O(m*n)**:
```
Space complexity : O(mn)O(mn). For each DFS we need O(h)O(h) space used by the system stack, where hh is the maximum depth of the recursion. In the worst case, O(h) = O(mn)O(h)=O(mn).
```

这就是为什么递归太多会stackoverflow。

这题虽然因为记忆化稍微有点难度，但感觉还是够不上Hard。如果这题是Hard，那么让身为medium的Can I win情何以堪。

参考:
[leetcode solution - Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solution/)