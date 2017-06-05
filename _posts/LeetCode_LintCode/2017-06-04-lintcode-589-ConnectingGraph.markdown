---
layout: post
title:  "Lintcode 589 - Connecting Graph"
date:   2017-06-04 00:15:02 -0400
categories: lintcode, Amazon
---

# Connecting Graph

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

```java
public class ConnectingGraph { 

    private int[] unions;//起名叫father比较make sense

    public ConnectingGraph(int n) {
        // initialize your data structure here.
        this.unions = new int[n];
        for(int i = 0; i < n; i++){
            unions[i] = i;
        }
    }
    
    //quick union中要记住的就是connect操作和query操作都需要用到这个root
    private int root(int index){
        while(unions[index] != index){
            index = unions[index];
        }
        
        return index;
    }

    public void connect(int a, int b) {
        // Write your code here
        
        int indexA = root(a - 1);
        int indexB = root(b - 1);
        
        unions[indexA] = indexB;
        
    }
        
    public boolean query(int a, int b) {
        // Write your code here
        
        int indexA = root(a - 1);
        int indexB = root(b - 1);
        
        return indexA == indexB;
        
    }
}
```


### 笔记

这题没什么好多说的，完全就是Union find的最经典应用。

因为会使用很多的union，所以我们使用quick union的方法。

其实对于那个数组的取名，叫father更好。

再者root是quick union的基础操作，connect和query都需要借助root.