---
layout: post
title:  "leetcode 382 - Linked List Random Node"
date:   2017-12-02 21:28:32.061248
categories: leetcode, Google
---

# Linked List Random Node

## 一刷

### 代码

根据Reservoir Sample的思想自己写的版本
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {

    private ListNode head;
    private Random rand;
    
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        this.head = head;
        this.rand = new Random();
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        ListNode current = head;
        int index = 0;
        int result = -1;
        
        while(current != null){
            index++;
            //注意rand.nextInt(index)生成的是[0, index)区间的数，不会包含index本身，所以index应该是1开始
            if(rand.nextInt(index) == 0){
                result = current.val;
            }
            
            current = current.next;
        }
        
        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
```

### 笔记

这题在没有follow up的情况下很简单:
直接先traverse一遍list(或者快慢指针)，找到list的length，然后直接`int offset = rand.nextInt(length)`(整好length位置被exclude)， 再走上offset步就可以了。

但是follow up中提到
`What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?`

那么有没有什么能够**一遍**pass，并且**不需要知道整个样本量长度**的办法?
答案是:有的，那就是**Reservoir Sampling**, 也就是**蓄水池抽样**

具体对于蓄水池抽样的分析，请见自己的笔记。

具体参考的连接，见
[leetcode - Java Solution with cases explain](https://discuss.leetcode.com/topic/55049/java-solution-with-cases-explain/2)
[数据工程师必知算法：蓄水池抽样](http://blog.jobbole.com/42550/)