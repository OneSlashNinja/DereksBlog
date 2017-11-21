---
layout: post
title:  "lintcode 219 - Insert Node In Sorted Linked List"
date:   2017-11-19 18:52:59.427435
categories: lintcode, Expedia
---

# Insert Node In Sorted Linked List

## 一刷

### 代码

自己的版本
```java
/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /*
     * @param head: The head of linked list.
     * @param val: An integer.
     * @return: The head of new linked list.
     */
    public ListNode insertNode(ListNode head, int val) {
        // write your code here
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode current = dummy;
        
        ListNode insertNode = new ListNode(val);
        
        while(current.next != null){
            if(val <= current.next.val){
                insertNode.next = current.next;
                current.next = insertNode;
                
                //插入完成了就直接返回，这样就可以把while循环外的内容留给特殊情况
                return dummy.next;
            }else{
                current = current.next;
            }
        }
        
        //如果程序能走到这里，说明要么直接原链表为空，要么val大于所有list中的内容
        current.next = insertNode;
        return dummy.next;
        
    }
}
```

[野球拳刷刷刷的版本](https://yeqiuquan.blogspot.com/2016/02/insert-node-in-sorted-linked-list.html)
```java
/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /*
     * @param head: The head of linked list.
     * @param val: An integer.
     * @return: The head of new linked list.
     */
    public ListNode insertNode(ListNode head, int val) {
        // write your code here
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;//其实不需要再声明一个current，因为最后直接返回的是dummy.next，已经不需要head了
        
        //整个while循环只负责定位，不涉及插入的部分
        while(head.next != null && head.next.val < val){
            head = head.next;
        }
        
        //定位完成，就可以直接插入了
        ListNode newNode = new ListNode(val);
        //注意插入需要先引导newNode.next的指针，然后才是head.next
        newNode.next = head.next;
        head.next = newNode;
        
        return dummy.next;
    }
}
```

### 笔记

此题虽然标的是naive的题，但是还是需要稍微理清下步骤才行的。

基本思路就是类似插入排序的思路: 指定的val和当前元素的val进行比较，如果指定的val > 当前元素的val，则继续往右走，直到找到插入位置，然后插入。


这里因为有可能head直接为null，也有可能需要插入的元素就在list的头部，所以需要用到dummy node的技巧。

自己思考了之后写出了自己的版本，也是基本一遍过。但是看过"野球拳刷刷刷"的版本后，发现有几个值得改进和学习的地方:

1. 其实可以使用head来替代current，因为最后返回的是dummy.next，head就并不必须待在原head指的位置了。

2. 自己的程序中，插入和移动都放在了while循环中进行，就使得整个程序的逻辑有点tricky，如果因为`current.next != null`的条件不满足而跳出了程序，则说明此时并没有插入node，还需要"补一刀"，来将新node添加到整个list的最后(或者list本身就为null,那直接新node就是新list)

而"野球拳刷刷刷"的版本则做到了软件工程中"职责分离"的特点。整个while循环只负责定位，并不涉及到插入的操作。当while循环结束后，我们就可以肯定，当前已经到了合适插入的位置，直接进行一次刷入就可以。不仅可读性增强，也不容易出错，并且很直观。