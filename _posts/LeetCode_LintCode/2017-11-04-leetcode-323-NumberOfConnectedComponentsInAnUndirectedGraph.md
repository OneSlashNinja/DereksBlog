---
layout: post
title:  "leetcode 323 - Number Of Connected Components In An Undirected Graph"
date:   2017-11-04 20:52:54.735609
categories: leetcode, Google
---

# Number Of Connected Components In An Undirected Graph

## 一刷

### 代码

```java

```

### 笔记


## 二刷

### 代码

```java
class Solution {
    public int countComponents(int n, int[][] edges) {
        
        //分配roots
        int[] roots = new int[n];
        
        //初始化，每个root都是独立的
        for(int i = 0; i < n; i++){
            roots[i] = i;
        }
        
        //用'查'来'并'
        for(int i = 0; i < edges.length; i++){
            int root1 = find(roots, edges[i][0]);
            int root2 = find(roots, edges[i][1]);
            
            if(root1 != root2) {
                roots[root1] = root2;
                n--;
            }
        }
        
        return n;
    }
    
    private int find(int[] roots, int id){
        
        while(roots[id] != id){
            roots[id] = roots[roots[id]];// optional: path compression
            id = roots[id];
        }
        
        return id;
    }
}
```

### 笔记

使用union find的quick union来解题。

union find记住四个要素:
1. 分配int[] roots数组(如果是quick find，就叫ids)
2. 初始化数组，每个都是独立的"小岛"
3. find方法, 对于quick union就是使用while找到最顶端的root，
4. union方法，对于quick union就是对两个元素先分别使用find找到root，然后比较root，如果一样就不需要union了，如果不一样，就把一个的root设成另一个。

注意本题的结果是要返回有多少个独立的component，利用了union的过程，当union了两个本来并不相连的component的时候就对于n--，非常巧妙。比起整个结束了以后再遍历roots然后分辨有多少个distinct的value要少些代码，并且节省空间，巧妙地多。

最后注意optional的那个path compression。

对于quick union有两种优化方案:
1. union by rank
2. Path Compression

优化后的quick union时间复杂度

> The two techniques complement each other. The time complexity of each operations becomes even smaller than O(logn) ~ O(n). In fact, amortized time complexity effectively becomes small constant.

[StackOverflow - What is the Time Complexity of Quick Union?](https://stackoverflow.com/questions/43036204/what-is-the-time-complexity-of-quick-union)