---
layout: post
title:  "leetcode 460 - LFU Cache"
date:   2018-01-06 18:52:33.341521
categories: leetcode, Google, Bloomberg, Amazon
---

# LFUCache

## 一刷

### 代码

```java

```

### 笔记

如果LRU算是Hard的话，那么这题肯定是Hard+.**因为这题本质上就是LRU多加了一个维度**，也就是对于cache已经满了的情况，要evict的元素需要移除频次最低的，如果频次最低的有好多个，那么还是要按LRU的来，移除最早加入的。

那么，这题其实有多种实现，在面试中如果能都大致提一遍的话肯定会很加分:
The first one: PriorityQueue + HashMap set O(capacity) get O(capacity)
The second one: TreeMap + HashMap set O(log(capacity)) get O(log(capacity))
The third one: HashMap + HashMap + DoubleLinkedList set O(1) get O(1)
[leetcode discuss - Java solutions of three different ways. PriorityQueue : O(capacity)  TreeMap : O(log(capacity)) DoubleLinkedList  : O(1)](https://leetcode.com/problems/lfu-cache/discuss/94657)

这三种做法的大致分析是:
1. PriorityQueue的版本基本就是陪衬的，因为Queue的remove操作需要O(n)时间，非常不efficient。
2. TreeMap的版本，这个版本虽然set和get操作比起doubleLinkedlist的版本来说稍逊一些，但是是有优势的:
    * 首先来说**代码会短很多**，而且也少很多，因为两个维度只要在comparator中依照顺序来比较就行，相当于合并了。
    * 其次，TreeMap的O(log(n))是guarantee的，而HashMap的版本的O(1)其实是amortized
3. HashMap + HashMap + DoubleLinkedList的版本虽然效率最高，但是代码量奇大，在面试中几乎不可能直接写出来，所以一定要问能不能使用神器:**LinkedHashSet**,该数据结构既有HashSet的各个特性，又能保证元素以输入时的顺序iterate，能够省下非常多的时间。
具体见[leetcode discuss - JAVA O(1) very easy solution using 3 HashMaps and LinkedHashSet](https://leetcode.com/problems/lfu-cache/discuss/94521)

注意在LinkedHashSet中取最早的元素的操作是:`lists.get(min).iterator().next();`

其实如果这么做题的话，你肯定会问那LRU岂不是完全不用写代码就能完成了？还真是,使用LinkedHashMap就可以，具体见[leetcode discuss - Laziest implementation: Java's LinkedHashMap takes care of everything](https://leetcode.com/problems/lru-cache/discuss/45939)

说其实，对于LRU，面试的时候肯定是不会让这么写，不过提一下也是不错的。而且如果真的是在自己工作写代码的时候，就不应该重复造轮子，使用已有的结构解决问题最好。
