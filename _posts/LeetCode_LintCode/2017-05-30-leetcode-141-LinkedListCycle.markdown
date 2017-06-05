---
layout: post
title:  "LeetCode 141 - Linked List Cycle"
date:   2017-05-30 00:15:02 -0400
categories: leetcode, Amazon
---

# Linked List Cycle

## 一刷

### 代码
自己的版本
```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */ 
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: True if it has a cycle, or false
     */
     public Boolean hasCycle(ListNode head) {
         
         if(head == null || head.next == null || head.next.next == null){
             return false;
         }
         
         ListNode fast = head;
         ListNode slow = head;
         
         while(fast.next != null && fast.next.next != null
                && slow.next != null){
             fast = fast.next.next;
             slow = slow.next;
             
             if(fast == slow){
                 return true;
             }
             
         }
         
         return false;
         
     }
}
```

九章的版本：
```java
public class Solution {
    public Boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode fast, slow;
        fast = head.next;
        slow = head;
        while (fast != slow) {
            if(fast==null || fast.next==null)
                return false;
            fast = fast.next.next;
            slow = slow.next;
        } 
        return true;
    }
}
```

### 笔记

就是根据上课笔记中说的：
如果有环，那么一块一慢两个指针从头开始一直走肯定会相遇。

---

## 二刷

### 代码

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        ListNode fast = head;
        ListNode slow = head;
        
        while(slow != null && fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(fast == slow){
                return true;
            }
        }
        
        return false;
        
    }
}
```


### 笔记

思路很简单，就还是和一刷时候一样，一快一慢两个指针。
和第一次自己的版本相比，发现其实不需要一开始对于head是否为null或者head.next甚至head.next.next是否为null的判断。

另外要注意的是在while循环中，
```java
if(fast == slow){
    return true;
}
```
的判断放在最后面，否则在一开始两个指针还没跑就会被判定相等，从而返回true。