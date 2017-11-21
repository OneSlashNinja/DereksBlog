---
layout: post
title:  "leetcode 346 - Moving Average From Data Stream"
date:   2017-11-20 00:17:42.075430
categories: leetcode, Google,Zynga
---

# Moving Average From Data Stream

## 一刷

### 代码

```java
public class MovingAverage {
    
    private int size;
    private Queue<Integer> queue;
    private int sum;
    
    /*
    * @param size: An integer
    */public MovingAverage(int size) {
        // do intialization if necessary
        this.size = size;
        this.queue = new LinkedList<Integer>();
        this.sum = 0;
    }

    /*
     * @param val: An integer
     * @return:  
     */
    public double next(int val) {
        // write your code here
        
        queue.offer(val);
        sum += val;
        
        if(queue.size() > size){
            sum -= queue.poll();
        }
        
        return (double)sum / queue.size();
        
    }
}
```

### 笔记
一道简单题。没啥特别说的，使用一个queue配合一个sum变量来维护，每次next新进来的元素都先添加进queue并加入sum，然后判断是否超出了规定的size，如果是则从队尾弹出一个元素，并从sum减去之，最后直接根据sum / size算平均值就可以，记得转型。

这题就看出了lintcode的系统还是没有leetcode做的robust。该题lintcode叫`Sliding Window Average from Data Stream`明明正确的代码，在leetcode都可以跑过，在lintcode跑不过。该题java的solution好像对于lintcode都是。