---
layout: post
title:  "leetcode 529 - Minesweeper"
date:   2017-12-03 11:58:02.820777
categories: leetcode, Amazon
---

# Minesweeper

## 一刷

### 代码

自己写的dfs版本
```java
class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        
        if(board == null || board[0] == null){
            return board;
        }
        
        //第一次就是雷需要单独提取出来，因为和recursion的过程中碰到雷是完全不同的
        if(board[click[0]][click[1]] == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }
        
        dfsHelper(board, click);
        
        return board;
    }
    
    private boolean isInBoard(char[][] board, int[] click){
        if(click[0] < 0 || click[0] >= board.length || click[1] < 0 || click[1] >= board[0].length){
            return false;
        }
        return true;
    }
    
    //其实本题不使用helper也能做，但是使用helper的好处是:
    //1. 在主updateBoard中就可以直接做一次Corner case的检查就可以了
    //2. helper方法可以返回是否是雷，这样就不用专门额外统计一次
    private void dfsHelper(char[][] board, int[] click)
    {
        //越界判断没必要在这里做，因为后面统计时必须要check是否越界，所以相当于所有能进入该dfs函数的click都是有效的click
        // if(click[0] < 0 || click[0] >= board.length || click[1] < 0 || click[1] >= board[0].length){
        //     return false;
        // }
        
        //本题的dfs并不需要boolean[][] visited, 因为通过修改board本身就有track是否被visited的能力，但是check一定要做
        //并且如果是mine，也应该不要再继续search了。注意这里遇到mine和刚一开始就点击到mine的处理是不一样的
        if(board[click[0]][click[1]] == 'M' || board[click[0]][click[1]] != 'E'){
            return;
        }
        
        //统计周边雷的数目和recursion必须分开，因为需要知道周边有没有雷才能决定是否继续recursion
        int mineCount = 0;
        //对于八个方向的check，可以使用两层循环+一个是否i和j同时为0进行判断
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                if(i == 0 && j == 0){
                    continue;
                }
                
                int x = click[0] + i;
                int y = click[1] + j;
                
                if(isInBoard(board, new int[] {x, y}) && board[x][y] == 'M'){
                    mineCount++;
                }
            }
        }
        
        if(mineCount > 0){
            board[click[0]][click[1]] = (char)('0' + mineCount);
            return;
        }else{
            board[click[0]][click[1]] = 'B';
        }
        
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                if(i == 0 && j == 0){
                    continue;
                }
                
                int x = click[0] + i;
                int y = click[1] + j;
                
                if(isInBoard(board, new int[] {x, y})){
                    dfsHelper(board, new int[] {x, y});
                }
            }
        }
        
    }
}
```

将getSurroundingMineNum提取出来的版本
```java
class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        
        if(board == null || board[0] == null){
            return board;
        }
        
        //第一次就是雷需要单独提取出来，因为和recursion的过程中碰到雷是完全不同的
        if(board[click[0]][click[1]] == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }

        dfsHelper(board, click[0], click[1]);
        
        return board;
    }
    
    private boolean isInBoard(char[][] board, int x, int y){
        if(x < 0 || x >= board.length || y < 0 || y >= board[0].length){
            return false;
        }
        return true;
    }
    
    private int getSurroundingMineNum(char[][] board, int x, int y){
        //统计周边雷的数目和recursion必须分开，因为需要知道周边有没有雷才能决定是否继续recursion
        int mineCount = 0;
        //对于八个方向的check，可以使用两层循环+一个是否i和j同时为0进行判断
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                if(i == 0 && j == 0){
                    continue;
                }

                int xx = x + i;
                int yy = y + j;
                
                if(isInBoard(board, xx, yy) && board[xx][yy] == 'M'){
                    mineCount++;
                }
            }
        }
        
        return mineCount;
    }
    
    //其实本题不使用helper也能做，但是使用helper的好处是:
    //1. 在主updateBoard中就可以直接做一次Corner case的检查就可以了
    //2. 可以使用x, y来代替click[]
    private void dfsHelper(char[][] board, int x, int y)
    {
        //越界判断没必要在这里做，因为后面统计时必须要check是否越界，所以相当于所有能进入该dfs函数的click都是有效的click
        // if(click[0] < 0 || click[0] >= board.length || click[1] < 0 || click[1] >= board[0].length){
        //     return false;
        // }
        
        //本题的dfs并不需要boolean[][] visited, 因为通过修改board本身就有track是否被visited的能力，但是check一定要做
        //并且如果是mine，也应该不要再继续search了。注意这里遇到mine和刚一开始就点击到mine的处理是不一样的
        //等等，这里写的有问题，首先，board[x][y] != 'E'的情况就包括了board[x][y] == 'M'
        //其次，board[x][y] == 'M'的情况其实是不会被reach的，因为，能到达M的情况肯定来自其八个方向之一，但是其八个方向肯定至少是数字1，那么就停下了，不会来到board[x][y] == 'M'
        //if(board[x][y] == 'M' || board[x][y] != 'E'){
        if(board[x][y] != 'E'){
            return;
        }
        
        int mineCount = getSurroundingMineNum(board, x, y);
        
        if(mineCount > 0){
            board[x][y] = (char)('0' + mineCount);//注意这里应该知道雷的数量肯定<=8，所以可以使用一个char来表示，所以可以使用该小技巧
            return;
        }else{
            board[x][y] = 'B';
        }
        
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                if(i == 0 && j == 0){
                    continue;
                }
                
                int xx = x + i;
                int yy = y + j;
                
                if(isInBoard(board, xx, yy)){
                    dfsHelper(board, xx, yy);
                }
            }
        }
        
    }
}
```

bfs版本
```java
class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        
        if(board == null || board[0] == null){
            return board;
        }
        
        //第一次就是雷需要单独提取出来，因为和recursion的过程中碰到雷是完全不同的
        if(board[click[0]][click[1]] == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(click);
        
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            
            //需要先检查当前要处理的这一块是不是还未被处理的，相当于检查visited[current[0]][current[1]] == false
            if(board[current[0]][current[1]] != 'E'){
                continue;
            }
            
            int mineNum = getSurroundingMineNum(board, current[0], current[1]);
            
            if(mineNum == 0){
                board[current[0]][current[1]] = 'B';
                
                for(int i = -1; i <= 1; i++){
                    for(int j = -1; j <= 1; j++){
                        if(i == 0 && j == 0){
                            continue;
                        }
                        
                        int nx = current[0] + i;
                        int ny = current[1] + j;
                        if(isInBoard(board, nx, ny)){
                            queue.offer(new int[] {nx, ny});
                        }
                    }
                }
                
            }else{
                board[current[0]][current[1]] = (char)('0' + mineNum);
            }
        }
        
        return board;
    }
    
    private boolean isInBoard(char[][] board, int x, int y){
        if(x < 0 || x >= board.length || y < 0 || y >= board[0].length){
            return false;
        }
        return true;
    }
    
    private int getSurroundingMineNum(char[][] board, int x, int y){
        //统计周边雷的数目和recursion必须分开，因为需要知道周边有没有雷才能决定是否继续recursion
        int mineCount = 0;
        //对于八个方向的check，可以使用两层循环+一个是否i和j同时为0进行判断
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                if(i == 0 && j == 0){
                    continue;
                }

                int xx = x + i;
                int yy = y + j;
                
                if(isInBoard(board, xx, yy) && board[xx][yy] == 'M'){
                    mineCount++;
                }
            }
        }
        
        return mineCount;
    }
    
}
```

### 笔记

首先要说的是这题的表示方式并不太make sense，因为如果没有点到雷，也是会直接显示出哪些块是雷的，那扫雷还有什么意义？？

感觉正确的做法是应该讲具体的"块的内容"，"和是否显示"进行分离，也就是说需要一个额外的boolean[][] display来表示是否应该显示某一块。

本题的关键算法是，将搜索分为两个步骤，前一个步骤会影响是否执行后一个步骤:
1. 对于当前的block，看看其八个方向上，是否有雷，如果没有雷，则将该block设置成'B'。而如果周围有雷, 则将该块设置为雷的数目。
2. 前一步的结果中如果发现周围没雷，则继续搜索，否则，如果周围有雷，则**不再进行进一步的搜索**

这样，就不会导致随便点开一块非雷的区域，则整个地图都被打开了(那扫雷也就没意义了，因为雷相当于都显示出来了)。

而第一步**因为并不涉及到搜索，不需要recursion，所以可以单独提取出来作为一个独立的private函数**，这样是一种比较好的practice。

本题有几点需要注意的地方:
1. 对于第一次click到了mine和recursion或者搜索过程中"click"到了mine是完全不一样的。前者相当于直接踩了雷，后者则只是停止搜索(其实具体过程中是不会对mine所在的块进行recursion的)。
所以，需要提前先对第一次是不是click到了mine额外提出来先判断一下。
2. 本题因为可以直接修改board，所以不需要bolean[][] visited，直接board本身就可以检测是否visited。
3. 之前的dfs的search一般都是上下左右四个方向，而本题则是八个方向，对于对八个方向进行搜索，是可以使用两层for循环的模板:
```java
for(int i = -1; i <= 1; i++){
    for(int j = -1; j <= 1; j++){
        if(i == 0 && j == 0){
            continue;
        }
        
        int xx = x + i;
        int yy = y + j;
        
        if(isInBoard(board, xx, yy)){
            dfsHelper(board, xx, yy);
        }
    }
}
```
来代替八段重复的代码
4. 对于isInBoard的检查也可以单独提取出来。