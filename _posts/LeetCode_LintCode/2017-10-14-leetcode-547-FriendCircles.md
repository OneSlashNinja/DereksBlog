---
layout: post
title:  "leetcode 547 - Friend Circles"
date:   2017-10-14 00:11:44.757510
categories: leetcode, Bloomberg
---

# Friend Circles

## 一刷

### 代码

自己写的使用Quick Find的union-find
```java
class Solution {
    public int findCircleNum(int[][] M) {
        
        if(M == null || M.length == 0 || M[0].length == 0){
            return 0;
        }
        
        int[] unionFind = new int[M.length];
        
        for(int i = 0; i < unionFind.length; i++){
            unionFind[i] = i;
        }
        
        for(int i = 0; i < M.length; i++){
            //注意这里j = i + 1可以省去一些操作: 从0...i这部分是镜像的duplicate，而j == i则是必定为1，也没必要检测，题目中已经提及过
            for(int j = i + 1; j < M[0].length; j++){
                
                if(M[i][j] == 1){
                    
                    //一定注意要先办unionFind[from]提取到一个单独的临时变量中，否则因为unionFind[from]会动态改变，循环到后面可能会出错
                    int from = unionFind[i];
                    for(int k = 0; k < unionFind.length; k++){
                        
                        //一定注意并不是
                        // if(unionFind[k] == i){
                        //     unionFind[k] = j;
                        // }             
                        if(unionFind[k] == from){
                            unionFind[k] = unionFind[j];
                        }
                    }
                    
                }
                
            }
        }
        
        HashSet<Integer> set  = new HashSet<>();
        
        for(int i = 0; i < unionFind.length; i++){
            if(!set.contains(unionFind[i])){
                set.add(unionFind[i]);
            }
        }
        
        return set.size();
        
    }
}
```

将union方法封装成一个单独的private方法
```java
class Solution {
    public int findCircleNum(int[][] M) {
        
        if(M == null || M.length == 0 || M[0].length == 0){
            return 0;
        }
        
        int[] unionFind = new int[M.length];
        
        for(int i = 0; i < unionFind.length; i++){
            unionFind[i] = i;
        }
        
        for(int i = 0; i < M.length; i++){
            for(int j = i + 1; j < M[0].length; j++){
                
                if(M[i][j] == 1){
                    
                    union(unionFind, i, j);
                }
                
            }
        }
        
        HashSet<Integer> set  = new HashSet<>();
        
        for(int i = 0; i < unionFind.length; i++){
            if(!set.contains(unionFind[i])){
                set.add(unionFind[i]);
            }
        }
        
        return set.size();
        
    }
    
    private void union(int[] ids, int from, int to){
        int fromValue = ids[from];
        for(int i = 0; i < ids.length; i++){
            if(ids[i] == fromValue){
                ids[i] = ids[to];
            }
        }
    }
}
```

quick-union版本
```java
class Solution {
    public int findCircleNum(int[][] M) {
        
        if(M == null || M.length == 0 || M[0].length == 0 || M.length != M[0].length){
            return 0;
        }
        
        int[] parents = new int[M.length];
        Arrays.fill(parents, -1);
        
        for(int i = 0; i < M.length; i++ ){
            for(int j = i + 1; j < M[0].length; j++){
                if(M[i][j] == 1){
                    if(find(parents,i) != find(parents, j)){
                        union(parents, i, j);
                    }
                }
            }
        }
        
        int count = 0;
        
        for(int i = 0; i < M.length; i++){
            if(parents[i] == -1){
                count++;
            }
        }
        
        return count;
    }
    
    private int find(int[] parents, int id){
        if(parents[id] != -1){
            return find(parents, parents[id]);
        }
        return id;
    }
    
    private void union(int[] parents, int a, int b){
        int aParent = find(parents, a);
        int bParent = find(parents, b);
        
        if(aParent != bParent){
            parents[aParent] = bParent;
        }
    }
}
```

dfs版本
```java
class Solution {
    public int findCircleNum(int[][] M) {
        if(M == null || M.length == 0 || M[0].length == 0){
            return 0;
        }
        
        boolean[] visited = new boolean[M.length];
        
        int count = 0;
        
        for(int i = 0; i < M.length; i++){
            if(!visited[i]){
                count++;
                dfs(M, visited, i);
            }
        }
        
        return count;
    }
    
    
    private void dfs(int[][] M, boolean[] visited, int id){
        visited[id] = true;
        
        for(int i = 0; i < M.length; i++){
            //这次的触底是在for循环内部判断，有了这个条件，就能保证dfs不会无限递归
            if(M[id][i] == 1 && !visited[i]){
                dfs(M, visited, i);
            }
        }
        
    }
}
```

### 笔记

一开始没什么思路，思考之后感觉应该可以使用union-find来做。直观上感觉quick find思考起来比较直接。
程序可分为两步:
1. 创建quick find的核心数组， 并且利用两层for循环来遍历M矩阵，对于每个i到j的连接，都使用union操作将其化为一体。
2. 在所有union完成后，就可以使用一个Set来统计核心数组中的值到底有多少个distinct的value，也就是朋友圈的数量。


结果程序写完以后，大致结构都对，但是花了将近一个多小时的时间debug，后来发现犯了两个quick find最容易犯的错误:
1. 千万注意不是
```java
if(unionFind[k] == i){
    unionFind[k] = j;
}        
```
很容直觉上感觉因为是i和j相连，那肯定是把i所在的value改成j啊，或者相反。但是其实经过一段时间的合并，i和j位置所对应的value很有可能已经不是i和j自己了，而我们需要去使用和比较的其实是i和j对应的value，所以一定是unionFind[i]和unionFind[j]。

2. 对于unionFind[i]一定要在循环前提取出来单独放在一个变量中。这一点和binary tree level order traverse中要把size提取出来是一个道理，因为unionFind[i]在循环过程中值是会动态改变的，而我们需要的是其固定的初始值。在princeton算法课的讲义中看到了单独提取出来，但原来还以为只是为了看着清楚，没体会这其中的道理。


另外，自己写的这个版本其实有coupling比较严重的问题。对于union-find的题目，最好是能把union-find封装成一个数据结构，像这题中虽然因为需要直接操作ids这个数组而不好封装，也最好是将union和find这两个操作封装成单独的方法。也就是第二个版本。

使用quick find的时间复杂度是外层的双层循环加上union操作自己的内部一层循环，所以是O(n^3)，空间上额外开出一块ids[](还有HashSet，不过一遍情况下比ids应该少)，是O(n)



quick union的版本有几点需要注意:
1. 和自己之前写的quick union的版本稍微有不同:
    * 之前写的版本初始化时是将ids[i] == i, 而这里是将所有ids[i] == -1
    * 之前的root(也就是find)使用的是while来进行迭代，而这里使用了recursion来递归调用

其实都是一样的。

quick union注意find方法(或者说root)是整个数据结构的核心，union也需要使用这个方法。

一开始感觉quick union在所有union都完成后的结果，也就是int parents[]似乎不好统计到底有多少个独立的朋友圈。但是看了题解后恍然大悟，因为**有多少个root其实就代表有多少个朋友圈，而root的判断标准就是parents[id] == -1(如果是另一个实现，就是parents[id] == id)**，所以也是非常直接和巧妙的。

---

而没想到的是这题具体dfs和BFS也能做，而且DFS的代码还非常少，时间复杂度还低。

要注意的是这题的dfs虽然也有参照的字典(int[][] M), 和用来定位的坐标(int id)，用来记录是否已经访问过的(boolean[] visited), 但是并没有用来专门盛放结果的container参数。这是因为调用DFS的外部程序就是利用一层循环配合visited这个数组来判断有几个独立的朋友圈，非常巧妙。

另外，对于**Graph型的dfs，其的复杂度是O(n + m)**，n代表node的数目，m代表edge的数目。这题中最多所有人都有连接，所以edge的数量最多是n^2，所以整个题目的时间复杂度是O(n^2)(虽然外面还有一层for循环，但是如果所有人都有连接，那么dfs一次就把所有人都连接上了)，空间复杂度是O(n)(使用boolean[] visited)

BFS的版本思路稍微有点不是很直接，就不写了，不过也是visited + queue。