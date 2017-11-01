---
layout: post
title:  "leetcode 274 - H-Index"
date:   2017-10-14 22:43:04.994761
categories: leetcode, Bloomberg
---

# H-Index

## 一刷

### 代码

```java
class Solution {
    public int hIndex(int[] citations) {
        
        Arrays.sort(citations);
        
        reverseArray(citations);
        
        int h = 0;
        
        for(int i = 0; i < citations.length; i++){
            if(citations[i] >= i + 1){
                h = i + 1;
            }
        }
        
        return h;
    }
    
    private void reverseArray(int[] citations){
        int i = 0, j = citations.length - 1;
        
        while(i < j){
            int temp = citations[i];
            citations[i] = citations[j];
            citations[j] = temp;
            
            i++;
            j--;
        }
    }
    
}
```

### 笔记

这是一道让人有点摸不着头脑的题目。没什么一般性，首先的关键是需要理解H-Index的定义。

看懂H-Index的定义是从[[LeetCode]H-Index 书影博客](http://bookshadow.com/weblog/2015/09/03/leetcode-h-index/)


> “一名科学家的h指数是指其发表的N篇论文中，有h篇论文分别被引用了至少h次，其余N-h篇的引用次数均不超过h次”

而看了很多题解之后都还是迷迷糊糊的，唯独也就[leetcode的第一个思路](https://leetcode.com/problems/h-index/solution/) 还比较易懂，主要是将问题象形化，转化为**降序排列后的histogram中，最大的正方形(注意是正方形)的边长，就是h**

那么就其实一行代码就行了，但是不知道为什么leetcode中居然不能使用`Arrays.sort(array, Collections.reverseOrder())`进行降序排列，还得自己写一个reverseArray的方法。
