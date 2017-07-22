---
layout: post
title:  "leetcode 339 - Nested List Weight Sum"
date:   2017-07-17 21:10:50.373693
categories: leetcode, Linkedin
---

# Nested List Weight Sum

## 一刷

### 代码

```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public int depthSum(List<NestedInteger> nestedList) {
        return depthSumHelper(nestedList, 1);
    }
    
    private int depthSumHelper(List<NestedInteger> nestedList, int layer){
        
        int sum = 0;
        
        for(NestedInteger integer : nestedList){
            if(integer.isInteger()){
                sum += integer.getInteger() * layer;
            }else{
                List<NestedInteger> children = integer.getList();
                sum += depthSumHelper(children, layer + 1);
            }
        }
        
        return sum;
    }
}
```

### 笔记

没啥好说的，一遍过。基本上考的就是recursion的基本功。

主要点在于要写调用自己的helper方法。