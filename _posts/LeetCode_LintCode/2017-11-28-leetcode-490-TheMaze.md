---
layout: post
title:  "leetcode 490 - The Maze"
date:   2017-11-28 22:03:34.261711
categories: leetcode, Google
---

# The Maze

## 一刷

### 代码

自己写的accepted但比较别扭的
```java
class Solution {
    
    private int[] xDirect = {0, 0, -1, 1};
    private int[] yDirect = {1, -1, 0, 0};
    
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        
        boolean canReachEnd = false;
        
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        
        for(int i = 0; i < 4; i++){
            canReachEnd = canReachEnd || dfsHelper(maze, start[0], start[1], i, destination, visited);
        }
        
        return canReachEnd;
    }
    
    private boolean isValidBlock(int[][] maze, int x, int y){
        if(x >= maze.length || x < 0 || y >= maze[0].length || y < 0 || maze[x][y] == 1){
            return false;
        }
        return true;
    }
    
    private boolean dfsHelper(int[][] maze, int x, int y, int directIndex, int[] destination, boolean[][] visited){
        
        if(!isValidBlock(maze, x, y)){
            return false;
        }
        
        if(isValidBlock(maze, x + xDirect[directIndex], y + yDirect[directIndex])){
            return dfsHelper(maze, x + xDirect[directIndex], y + yDirect[directIndex], directIndex, destination, visited);
        }
        
        //这里到了停下来的状态，此时才可以检查是否为终点，此检查不可放前面
        if(x == destination[0] && y == destination[1]){
            return true;
        }
        
        //这里进行visited的检查，是因为visited应该只检查能"停下来"的位置
        if(visited[x][y]){
            return false;
        }
        visited[x][y] = true;
        
        boolean reachDest = false;
        
        for(int i = 0; i < 4; i++){
            if(i != directIndex){
                reachDest = reachDest || dfsHelper(maze, x + xDirect[i], y + yDirect[i], i, destination, visited);
            }
        }
        
        return reachDest;
    }
}
```

根据题解中使用while循环的dfs版本，自己改进写的dfs版本
```java
class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        return dfsHelper(maze, start[0], start[1], destination, visited);
    }
    
    private boolean isValidPos(int[][] maze, int m, int n){
        if(m < 0 || m >= maze.length || n < 0 || n >= maze[0].length || maze[m][n] == 1){
            return false;
        }
        return true;
    }
    
    //感觉还是使用分开的横竖两个坐标m, n来表示一个点方便点，如果是使用int[]，则在recursion的时候还需要new int[] {x, y}
    private boolean dfsHelper(int[][] maze, int m, int n, int[] destination, boolean[][] visited){
        
        //一般情况下这种对于matrix里面dfs搜索的第一步是先看是否越界或者有效，但是这题中其实对于无效的情况并不会trigger进一步的recursion
        //所以这一步检查不做也可以通过，不过写上也是无害的
        // if(!isValidPos(maze, m, n)){
        //     return false;
        // }
        
        if(visited[m][n]){
            return false;
        }
        //记得在进行进一步的recursio前，需要先mark为访问过
        //并且可以看出本题是纯dfs而不是recursion，并不需要在函数结束前进行visited[m][n] = false;的回溯
        visited[m][n] = true;
        
        //找到目标了
        if(m == destination[0] && n == destination[1]){
            return true;
        }
        
        boolean canReachEnd = false;
        
        //这里可以用上下左右四个变量，也可以用两个变量，如 mOffset和nOffset，但是注意如果用两个变量需要在每次recursion完之后reset该变量为0
        int u = m, d = m, l = n, r = n;
        
        while(isValidPos(maze, u, n)){
            u++;
        }
        //注意，因为跳出while循环后，u会在第一个无效的位置，所以需要"退一步"海阔天空
        canReachEnd = canReachEnd || dfsHelper(maze, u - 1, n, destination, visited);
        
        while(isValidPos(maze, d, n)){
            d--;
        }
        canReachEnd = canReachEnd || dfsHelper(maze, d + 1, n, destination, visited);
        
        while(isValidPos(maze, m, r)){
            r++;
        }
        canReachEnd = canReachEnd || dfsHelper(maze, m, r - 1, destination, visited);
        
        while(isValidPos(maze, m, l)){
            l--;
        }
        canReachEnd = canReachEnd || dfsHelper(maze, m, l + 1, destination, visited);
        
        return canReachEnd;
    }
}
```

同样的思路自己写的bfs的版本
```java
class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        
        if(maze == null || maze[0] == null || start == null || destination == null){
            return false;
        }
        
        //bfs的版本并不像dfs一样需要一个dfsHelper，bfs的版本只需要借助一个额外的queue就可以
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        queue.offer(start);
        //注意这里不能像题解一样直接先设置visited[start[0]][start[1]] = true;
        //否则直接进入while循环就退出来了
        
        while(queue.size() > 0){
            int[] current = queue.poll();
            if(visited[current[0]][current[1]]){
                continue;
            }
            visited[current[0]][current[1]] = true;
            
            if(current[0] == destination[0] && current[1] == destination[1]){
                return true;
            }
            
            int u = current[0], d = current[0], l = current[1], r = current[1];
            
            while(isValid(maze, u, current[1])){
                u++;
            }
            queue.offer(new int[] {u - 1, current[1]});
            
            while(isValid(maze, d, current[1])){
                d--;
            }
            //相比题解的版本，自己的版本会有可能把current自己压回到queue里去，不过由于visited已经设置成了true，所以会直接跳过
            queue.offer(new int[] {d + 1, current[1]});
            
            while(isValid(maze, current[0], l)){
                l--;
            }
            queue.offer(new int[] {current[0], l + 1});
            
            while(isValid(maze, current[0], r)){
                r++;
            }
            queue.offer(new int[] {current[0], r - 1});
        }
        
        return false;
    }
    
    private boolean isValid(int[][] maze, int m, int n){
        if(m < 0 || m >= maze.length || n < 0 || n >= maze[0].length || maze[m][n] == 1){
            return false;
        }
        return true;
    }
}
```

题解的bfs版本
```java
public class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        int[][] dirs={{0, 1}, {0, -1}, {-1, 0}, {1, 0}}; //bfs的好处之一是，因为没有递归，这样一个direction变量不需要放在全局了，函数内部就可以
        Queue < int[] > queue = new LinkedList < > ();//才知道int[] 也是可以作为一种类型的?
        queue.add(start);
        visited[start[0]][start[1]] = true;//注意这里和自己版本的区别
        while (!queue.isEmpty()) {
            int[] s = queue.remove();
            if (s[0] == destination[0] && s[1] == destination[1])
                return true;
            for (int[] dir: dirs) {
                int x = s[0] + dir[0];
                int y = s[1] + dir[1];
                while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                }
                //题解的版本是最后才判断和设置visited为true的
                if (!visited[x - dir[0]][y - dir[1]]) {
                    queue.add(new int[] {x - dir[0], y - dir[1]});
                    visited[x - dir[0]][y - dir[1]] = true;
                }
            }
        }
        return false;
    }
}
```

### 笔记

这是一道之前自己见过的Google的面经题，非常有意思。

这一题最难也是最关键的一个点就是: **小球一旦朝着一个方向滚动，则必须碰到障碍物或者边界才能停下来。**

如果没有这个条件，那么该题完全就是最经典和普通的迷宫搜索问题，直接最经典的dfs或者bfs模板就能解决，而对于该题，则只有真正理解和处理好这个条件，才能把本题做对和做好。

而本题的关键则在于，需要把**小球停下来时候**和**小球正在滚动中**当成完全不同的情况进行处理。

从自己的第一个版本可以看出，自己的思考中，对于**小球停下来时候**和**小球正在滚动中**的情况，是当成同类型的不同情况进行处理。最后也还是做出来了，但是可以见到代码略蹩脚:
为了判断当前情况到底是停下来的还是在滚动中，需要在parameter中处了坐标信息外，还要**添加方向**，这样，如果当前坐标已经不能再在参数的方向上进行移动了，我们就可以知道已经不能滚停下来了。

而其实如果是这种思路，另一个没法解决的问题就是如果判断某一个点之前访问过?
因为如果对所有的访问过的块都一视同仁的话，碰到已经visited的块就停止进一步的搜索，那么像
```
 * --
  |  |
s----
  |
```
这种路线就不能走了。(小游戏Maze Dash中感觉是倒是正好可以利用这种visited的)

所以，该题对于visited怎么处理的思想也是一样，需要把**小球停下来时候**和**小球正在滚动中**当成完全不同的情况进行处理，也就是说**visited记录的只是停下来的时候访问过的点**。

而看过题解以后可以发现，**其实对于小球滚动时的状态，因为方向是确定的，只有一个，所以并不算是搜索，也就完全不需要使用recursion进行处理。**
所以，完全可以在dfs中，**直接通过while循环配合某一方向上一直递增到喷到障碍或者边界，来模拟滚动到下一个静止的点。**


另外，可以从本题中发现和学到的东西有:

1. 可以看出dfs和Backtracking的区别，本题属于典型的dfs，可以看到visited并不会在recursion结束的时候reset回false，因为访问过就是访问过，不需要再设置回来了。并且本题还可以用queue来bfs，而Backtracking则不行。
2. 该题是一个非常好的可以比较dfs和bfs两种写法的题目。可以看到，关键的步骤其实都是一样的，只不过一个是recursion，一个需要借助queue
3. 对于bfs的版本，更适合声明二维方向变量，因为没有递归，所以可以直接放在函数内部，而不像dfs必须要放在全局。
4. 对于这种matrix或者图的搜索的dfs或者bfs，非常适合提取出一个`private boolean isValidBlock(int[][] matrix, int x, int y)`或者`isInBoard`函数来判断是否当前位置是有效位置或者在界内。
5. 对于dfs的recursion的helper函数，一般只需要**位置**，而不需要**方向**，方向应该是在helper函数内部决定的，然后确定下一个要走的位置，再调用helper函数。所以本题自己一开始的解法把方向也带入到helper函数中就会使得思路比较混乱。
6. 自己的经验表明，使用(int x, int y)来作为参数表示一个位置比使用start[]要方便和清晰许多，在写程序的时候如果使用start[0]和使用start[1]是非常眼花缭乱的。但是有一种情况例外，就是bfs的时候，对于queue中，坐标必须以一个pair来进行offer或者poll，所以，要么就需要一个额外的"Pair" class，要么就是用int[]类型，感觉上后者更方便，因为省去了声明class，在面试中应该会快不少。
