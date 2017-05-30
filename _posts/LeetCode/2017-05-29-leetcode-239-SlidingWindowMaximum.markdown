---
layout: post
title:  "LeetCode 239 - Sliding Window Maximum"
date:   2017-05-29 00:15:02 -0400
categories: leetcode, Amazon
---

# Sliding Window Maximum

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

brute force
```java
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0 || nums.length < k){
            return new int[0];
        }
        
        int[] result = new int[nums.length - k + 1];
        
        for(int i = 0; i < nums.length - k + 1; i++){
            int max = Integer.MIN_VALUE;
            for(int j = i; j < i + k; j++){
                max = Math.max(nums[j], max);
            }
            result[i] = max;
        }
        
        return result;
    }
}
```

Heap(其实并无什么改进)
```java
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0 || nums.length < k){
            return new int[0];
        }
        
        int[] result = new int[nums.length - k + 1];
        
        PriorityQueue pq = new PriorityQueue<Integer>(k, Collections.reverseOrder());
        
        for(int i = 0; i < nums.length; i++){
            pq.offer(nums[i]);
            
            if(i >= k){
                pq.remove(nums[i - k]);
            }
            
            if(i >= k - 1){
                result[i - k + 1] = (int)pq.peek();
            }
        }
        
        return result;
    }
}
```

dequeue
```java
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0 || nums.length < k){
            return new int[0];
        }
        
        int[] result = new int[nums.length - k + 1];
        
        //store index, not value
        Deque<Integer> deque = new ArrayDeque<Integer>();
        
        for(int i = 0; i < nums.length; i++){
            
            //先比较是否已经超出了window
            //这里比较的是index，是看index是否已超出范围
            while(!deque.isEmpty() && deque.peek() < i - k + 1){ //i所在的位置可以看成是window的右端, 所以window左端的坐标就是i - k + 1
                //注意这里是从头poll
                deque.poll();
            }
            
            //再比较新的要加入是否使得dequeue中的元素有序
            //这里比较的是value
            while(!deque.isEmpty() && nums[deque.peekLast()] < nums[i]){
                //注意这里是从尾poll
                deque.pollLast();
            }
            
            deque.offer(i);
            
            //当window的左端也开始"启程"，才是真正需要开始计算window的时候
            if(i - k + 1 > 0){
                //注意Result中放的是结果，所以不能是直接的deque.peek()
                result[i - k + 1] = nums[deque.peek()];
            }
            
        }
        
        return result;
    }
}
```

### 笔记
这题首先坐标的计算是挺烦的一个地方，如果使用到底什么时候开始需要remove？什么时候开始向结果集中添加元素？

(1)brute force就是直接的两层循环，一层控制整个window的挪动，一层用来在window中寻找最大值。所以复杂度应该是O(nk)

(2)Heap的版本需要说一下，Leetcode的tag是heap,有误导性。在[https://segmentfault.com/a/1190000003903509]中，Ethan Li分析说使用PriorityQueue的版本的复杂度是O(nlogk)，这应该是不对的，因为这里PriorityQueue使用的并不是offer和poll操作，如果是的话，因为两个操作都是O(logk)的时间，所以可以达到O(nlogk)。但是这题中使用的是remove，而remove的操作需要O(n)的时间，所以其实最后的复杂度应该还是O(nk)

(3)另外需要注意的一点是，PriorityQueue在默认情况下是minHeap，而我们这里需要用的是maxHeap，所以在实例化的时候需要指明。一开始以为必须给一个comparator，但其实可以给一个**Collections.reverseOrder()**作为参数，就能够达到maxHeap的效果。

(4)dequeue的版本代码不多，但是非常巧妙，理解起来还是需要一些时间，具体的参考见：
[https://discuss.leetcode.com/topic/19055/java-o-n-solution-using-deque-with-explanation]
[http://www.programcreek.com/2014/05/leetcode-sliding-window-maximum-java/]

**其思想和Largest Rectangle in Histogram中利用stack很像，都是利用维持一个有序的数据结构，存储所有有效的信息，不会有任何的冗余信息来增加负担**

而这题中使用Deque而不是stack的地方更加精妙，是因为在两种情况下我们需要移除元素:
<1>如果新要添加的元素会破坏queue中的有序性，那么需要从队列尾开始remove(peekLast配合pollLast)
<2>如果在队列中的元素已经不在window之中了，那么需要从队列首开始remove(peek配合poll)

要注意的是deque中存在的元素在array中的index，因为<1>中需要使用value，而<2>中需要使用index。而有index就能使用nums[index]知道value,但是知道value并不能知道index。所以deque中果断应该保存index信息，这点和"Largest Rectangle in Histogram"中的一样。

另外Deque的实现有很多种，但是似乎ArrayDeque比LinkedList在多数情况下的性能更好，不仅能节省空间，并且因为是头尾的删除，不涉及到在中间某一处的insert或者remove，所以array的性能也会比LinkedList更好。