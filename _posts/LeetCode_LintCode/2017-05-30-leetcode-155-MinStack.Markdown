---
layout: post
title:  "LeetCode 155 - Min Stack"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Min Stack

## 一刷

### 代码

简单version：
```java
public class MinStack {
    
    private Stack<Integer> numsStack;
    private Stack<Integer> minHistoryStack;
    
    public MinStack() {
        // do initialize if necessary
        this.numsStack = new Stack<Integer>();
        this.minHistoryStack = new Stack<Integer>();
    }

    public void push(int number) {
        // write your code here
        this.numsStack.push(number);
        if(minHistoryStack.isEmpty()){
            this.minHistoryStack.push(number);
        }else{
            this.minHistoryStack.push(Math.min(minHistoryStack.peek(), number));
        }
    }

    public int pop() {
        // write your code here
        this.minHistoryStack.pop();
        return this.numsStack.pop();
    }

    public int min() {
        // write your code here
        return minHistoryStack.peek();
    }
}
```

加强version:
```java
public class MinStack {
    
    private Stack<Integer> numsStack;
    private Stack<Integer> minHistoryStack;
    
    public MinStack() {
        // do initialize if necessary
        this.numsStack = new Stack<Integer>();
        this.minHistoryStack = new Stack<Integer>();
    }

    public void push(int number) {
        // write your code here
        this.numsStack.push(number);
        if(minHistoryStack.isEmpty()){
            this.minHistoryStack.push(number);
        }else{
            if(number <= minHistoryStack.peek()){
                this.minHistoryStack.push(number);
            }
        }
    }

    public int pop() {
        // write your code here
        int popNum = this.numsStack.pop();
        if(popNum == this.minHistoryStack.peek()){
            this.minHistoryStack.pop();
        }
        return popNum;
    }

    public int min() {
        // write your code here
        return minHistoryStack.peek();
    }
}
```

### 笔记

本题和“喜刷刷”的作者的思路基本一样：
"
看到题目第一反应是用一个int minVal来记录整个stack当前的最小值就可以了。然后仔细想下，发现问题在于当这个最小值被pop以后，无法O(1)时间得到新的最小值。所以问题的关键在于要跟踪记录每个新数字压入栈时的当前最小值，而不是只记录一个总的最小值。

一种思路是将make_pair(xi, curMin)一起压入栈stack<pair<int,int>>中。但这种方法的空间复杂度为2n。再仔细观察，发现只有当push或pop的对象xi<= min(stack)时，才会影响到min(stack)的值。
"
第一个版本就是直接做一个和存放实际数据同步的minHistoryStack(或者叫trackMinStack),这两个stack的长度总是一致的，同出同进，所以易于实现。

第一个版本需要注意：
if(minHistoryStack.isEmpty()){
本来写的numsStack.isEmpty()，本来想的是因为minHistoryStack和numsStack会同增同减，所以一样，但是“同增同减”是宏观上的，而push操作已经是原子操作中了，而因为先执行了this.numsStack.push(number);numsStack就会比minHistoryStack暂时性地长1.

但是我们会发现，minHistoryStack中的数组从底到顶一定是越来越小的，而且其中可能有很多的重复元素，所以这就会产生冗余信息。

对于增强版本，喜刷刷也解释地非常好：

"
用另一个stack<int> trackMin来记录min值的变化，trackMin.top()表示当前最小值。
当有新的xi<=trackMin.top()被压入时，将xi压入trackMin变为新的当前最小值。
当xi==trackMin.top()时被pop出时，trackMin也同时pop。

这里的一个关键是理解为什么是x<=trackMin.top()而不是x<trackMin.top()。加入对于push(x)只有当x<trackMin.top()时，才将x压入trackMin中。

例如压入以下数后：
xi:    3 2 1 2 1 
trackMin: 3 2 1

此时如果pop，则变为
xi:    3 2 1 2
trackMin: 3 2

然而实际栈里的最小值仍旧为1，这个1因为重复数字的关系在trackMin中丢失。
"

最后
```java
if(minHistoryStack.isEmpty()){
    this.minHistoryStack.push(number);
}else{
    if(number <= minHistoryStack.peek()){
        this.minHistoryStack.push(number);
    }
}
```
这段可以用一个"或"简化为
```java
if(minHistoryStack.isEmpty() || number <= minHistoryStack.peek()){
    this.minHistoryStack.push(number);
}
```
---

## 二刷

### 代码

简单version:
```java
public class MinStack {

    private Stack<Integer> numStack;
    private Stack<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        this.numStack = new Stack<Integer>();
        this.minStack = new Stack<Integer>();
    }
    
    public void push(int x) {
        numStack.push(x);
        if(minStack.isEmpty()){
            minStack.push(x);
        }else{
            minStack.push(Math.min(minStack.peek(), x));
        }
    }
    
    public void pop() {
        numStack.pop();
        minStack.pop();
    }
    
    public int top() {
        return numStack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

强化version:
```java
public class MinStack {

    private Stack<Integer> numStack;
    private Stack<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        this.numStack = new Stack<Integer>();
        this.minStack = new Stack<Integer>();
    }
    
    public void push(int x) {
        numStack.push(x);
        
        //注意条件中的x <= minStack.peek()是<=，
        //因为如果多次出现同一个最小值，那么pop的过程中就会pop出第一个，然后失去对另一个的track
        //具体例子见笔记
        if(minStack.isEmpty() || x <= minStack.peek()){
            minStack.push(x);
        }
    }
    
    public void pop() {
        int num = numStack.pop();
        if(num == minStack.peek()){
            minStack.pop();
        }
    }
    
    public int top() {
        return numStack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

### 笔记
具体的思路以及优化的方法在一刷的笔记中已经很清楚了。就是要注意加强版本中的push中的条件(见注释)

