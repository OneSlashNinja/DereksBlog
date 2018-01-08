---
layout: post
title:  "leetcode 253 - MeetingRoom2"
date:   2018-01-07 18:57:44.531597
categories: leetcode, Google,
---

# MeetingRoom2

## 一刷

### 代码

Heap版本1
```java
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    
    class IntervalComparator implements Comparator<Interval>{

        public int compare(Interval i1, Interval i2){
            return i1.start - i2.start;
        }
    }
    
    public int minMeetingRooms(Interval[] intervals) {
        
        if(intervals == null || intervals.length == 0){
            return 0;
        }
        
        Arrays.sort(intervals, new IntervalComparator());
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        
        minHeap.offer(intervals[0].end);
        
        for(int i = 1; i < intervals.length; i++){

            //之所以是if而不是while是因为当新的intervals[i]来的时候，如果在intervals[i].start之前
            //最早开完的会议已经开完了，那就能腾出来一个room给intervals[i]
            if(intervals[i].start >= minHeap.peek()){
                minHeap.poll();
            }
            minHeap.offer(intervals[i].end);
        }
        
        return minHeap.size();
    }
    
    
}
```

自己写的heap版本2
```java
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    
    class IntervalComparator implements Comparator<Interval>{

        public int compare(Interval i1, Interval i2){
            return i1.start - i2.start;
        }
    }
    
    public int minMeetingRooms(Interval[] intervals) {
        
        if(intervals == null || intervals.length == 0){
            return 0;
        }
        
        Arrays.sort(intervals, new IntervalComparator());
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        
        int max = 0;
        for(int i = 0; i < intervals.length; i++){
            //这里使用while把所有当前intervals[i].start之前已经结束了的会议都踢出heap，剩下的都是在intervals[i].start还在开的会议
            while(!minHeap.isEmpty() && intervals[i].start >= minHeap.peek()){
                minHeap.poll();
            }
            minHeap.offer(intervals[i].end);

            //当前必须同时需要的meeting room
            max = Math.max(max, minHeap.size());
        }
        
        return max;
    }
    
    
}
```

### 笔记

本道题有多种写法，其中比较make sense的就是heap的版本，而heap的版本也都写了两种版本。

大概套路差不多，都是先按start排序，然后以end来将interval插入到heap中去。

对于版本1，不需要额外的`int max`变量，最后heap的size就是结果。其思想是**如果新的会议要开始了，去看看最早结束的那个会议是不是已经结束了? 如果结束了，那用那个结束的meeting room就可以了嘛**

版本1的思路来源是[](https://www.youtube.com/watch?v=118Ie3nPCdc)

而对于版本2，heap则维护的是同时在开的会议的情况，其思想是**如果新的会议要开始了，就check一下，把所有已经结束的会议的room都清空了，然后再给新的这个会议分割room**

个人感觉自己的第二个版本更一般化一些。虽然是个while来代替了if，但其实复杂度没有上升，相当于每个interval进出都一次。