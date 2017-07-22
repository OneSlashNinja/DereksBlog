---
layout: post
title:  "leetcode 364 - Nested List Weight Sum2 "
date:   2017-07-17 21:44:36.766396
categories: leetcode, Linkedin
---

# Nested List Weight Sum 2

## 一刷

### 代码

错误思路
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    
    class ResultType{
        public int bottomUpDepth;
        public int sum;
        
        public ResultType(int bottomUpDepth, int sum){
            this.bottomUpDepth = bottomUpDepth;
            this.sum = sum;
        }
    }
    
    public int depthSumInverse(List<NestedInteger> nestedList) {
        
        return sumHelper(nestedList).sum;
    }
    
    private ResultType sumHelper(List<NestedInteger> nestedList){
        int sum = 0;
        int currentBottomUpDepth = 1;
        for(NestedInteger item : nestedList){
            if(!item.isInteger()){
                List<NestedInteger> innerList = item.getList();
                currentBottomUpDepth = Math.max(currentBottomUpDepth, sumHelper(innerList).bottomUpDepth + 1);
            }
        }
        
        for(NestedInteger item : nestedList){
            if(item.isInteger()){
                sum += item.getInteger() * currentBottomUpDepth;
            }else{
                List<NestedInteger> innerList = item.getList();
                sum += sumHelper(innerList).sum;
            }
        }
        
        return new ResultType(currentBottomUpDepth, sum);
    }
    
}
```

自己写的2d list转化为1d list版本
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    
    public int depthSumInverse(List<NestedInteger> nestedList) {
        
        List<Integer> buffer = new ArrayList<Integer>();
        fillBuffer(nestedList, 1, buffer);
        
        int sum = 0;
        
        for(int i = buffer.size() - 1, j = 1; i >= 0; i--, j++){
            sum += buffer.get(i) * j;
        }
        
        return sum;
    }
    
    private void fillBuffer(List<NestedInteger> nestedList, int depth, List<Integer> buffer){
        
        while(depth > buffer.size()){
            buffer.add(0);
        }
        
        for(NestedInteger item : nestedList){
            if(item.isInteger()){
                //buffer[depth - 1] += item.getInteger(); java没有[]操作符真是太不方便了
                buffer.set(depth - 1, buffer.get(depth - 1) + item.getInteger());
            }else{
                fillBuffer(item.getList(), depth + 1, buffer);
            }
        }
        
    }
    
    
}
```

完全没有depth，直接递推的最巧妙的版本
```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        
        int unweighted = 0;
        int weighted = 0;
        
        while(!nestedList.isEmpty()){
            List<NestedInteger> nextLevel = new ArrayList<>();
            for(NestedInteger item : nestedList){
                if(item.isInteger()){
                    unweighted += item.getInteger();
                }else{
                    //不是nextLevel.add(item);
                    nextLevel.addAll(item.getList());
                }
            }
            //注意unweighted并没有每次清零，所以之前的值都会被重复计算
            weighted += unweighted;
            nestedList = nextLevel;
        }
        
        return weighted;
        
    }
}
```

### 笔记

和Nested List Weight Sum在给出的结构上一样的，只不过权重的计算方式不一样了，但是一下题目的难度就上升了。

我首先得弄清楚为什么越"浅"的层权重越大会使得原来的解法不能使用?
这是因为一开始在浅的层的时候，没有办法知道到底最深的list有多深。

一开始自己的思路是仍然使用recursion，只不过原来是在recursion自顶向下的过程中计算，但是这回变成下降到最下面后开始返回，自底向上的时候再开始计算。但是这样会有问题，比如像:

[1,[1,1],[1,1,[1]]]

你如果按层级来看是这样的:

1
    [1 , 1] [1 , 1] 
                1

也就是说,在第二层[1,1]recursion的过程中，它也是并不知道最深的层是多少，所以在触底后开始开始向上的过程会只能以自己为参照，最后计算出错误的结果。


之后看了GrandYang的帖子

[Nested List Weight Sum II 嵌套链表权重和之二](http://www.cnblogs.com/grandyang/p/5615583.html)

明白了两种不同的思路，都能解出来:

1. 把整个过程拆分成两步:

(1) 因为我们关心的是深度，所以把整个多维的list转化2d的array来表示，比如刚才的
[1,[1,1],[1,1,[1]]]
可以转化为
[
    [1], 
    [1, 1, 1, 1],
    [1]
]

(2)经过第一步，就可以把index和深度对应起来，然后计算最后需要的结果了。


上面这个版本的优化是，因为我们关心的最后结果只是sum，并不关心每个元素具体是什么，所以在每一个划分每一个depth的过程中，直接可以只记录结果，也就可以把二维的数组再降维变成一维的，也就是说把

[
    [1], 
    [1, 1, 1, 1],
    [1]
]

变成

[1, 4, 1]

这样最后直接计算结果

1 * 3 + 4 * 2 + 1 * 1 = 12

就可以了。


2. 第二种方法更是巧妙

核心就是: 递推 + 重复计算

因为递推是从最浅的层往最深的层递推，而我们每递推到下一层，都可以将上一层计算的结果带到当前层从而进行再一次的重复计算，这样在浅层的数据每深一层就被多计算一次，就完全就省去了需要depth的麻烦，同样也将刚才方法中的分两步走巧妙合并成了一步。

要注意程序是怎么样利用unweighted和weighted能够重复计算之前的元素的。
