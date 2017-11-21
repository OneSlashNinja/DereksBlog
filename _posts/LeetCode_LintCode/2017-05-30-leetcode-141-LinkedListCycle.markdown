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


## 三刷

### 代码

配合HashSet版
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
        
        Set<ListNode> set = new HashSet<>();
        
        while(head != null){
            if(set.contains(head)){
                return true;
            }
            set.add(head);
            head = head.next;
        }
        
        return false;
    }
}
```

最简洁容易记住的Two pointer版
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
        
        if(head == null){
            return false;
        }
        
        ListNode fast = head.next; //不要怕，这里已经被前面的判断cover了，head肯定不会为null
        ListNode slow = head;
        
        //这里不用判断slow的情况，因为slow已经被fast的情况都cover了
        while(fast != null && fast.next != null){
            if(slow == fast){
                return true;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return false;
    }
}
```

### 笔记

刷到第三遍，就要有更高的视野了，不仅应该能从容自得地给出"直觉解"并进行分析，而且应该能写出最优解，并且知道为什么最优解能work。

首先这题的直觉解，其实就是查重，那么肯定就是配合HashMap或者HashSet然后进行traverse，如果走完了没有重复，那么肯定没有cycle，如果没走完之前发现有重复，就肯定是cycle。

直觉解的时间复杂度是O(n), 但是空间也是O(n).

而two pointer的版本之所以更优，其实并不是时间上更优(还是O(n))，而是空间上变成了O(1)。

那么说为什么fast和slow两个指针一定会相遇?

这其实可以反推，也就是说fast肯定不是skip low，并且可以肯定相遇的前一步必定是fast在slow的right behind。
也就是说，**如果有环，fast追及slow的距离肯定是每次递减1的，最后一定会递减为0**

而two pointer的版本感觉hackerrank上的写的最好，也最容易记。

### 参考

[hackrank](https://www.youtube.com/watch?v=MFOAbpfrJ8g&t=1s)
[leetcode - linked list cycle - solution](https://leetcode.com/problems/linked-list-cycle/solution/)