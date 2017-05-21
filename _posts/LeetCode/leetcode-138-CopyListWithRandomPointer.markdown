---
layout: post
title:  "LeetCode 138 - Copy List With Random Pointer"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Copy List With Random Pointer

## 一刷

### 代码
```java
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    public RandomListNode copyRandomList(RandomListNode head) {
        // write your code here
        
        if(head == null){
            return null;
        }
        
        RandomListNode newListHead = new RandomListNode(head.label);
        RandomListNode firstNode = newListHead;
        
        Map<RandomListNode, RandomListNode> oldToNewMap = new HashMap<RandomListNode, RandomListNode>();
        Map<RandomListNode, RandomListNode> newToOldMap = new HashMap<RandomListNode, RandomListNode>();
        
        oldToNewMap.put(head, newListHead);
        newToOldMap.put(newListHead, head);
        
        while(head.next != null){
            RandomListNode newNode = new RandomListNode(head.next.label);
            newListHead.next = newNode;
            newListHead = newListHead.next;
            head = head.next;
            oldToNewMap.put(head, newListHead);
            newToOldMap.put(newListHead, head);
        }
        
        newListHead = firstNode;
        while(newListHead != null){
            RandomListNode originalNode = newToOldMap.get(newListHead);
            newListHead.random = oldToNewMap.get(originalNode.random);
            
            newListHead = newListHead.next;
        }
        
        return firstNode;
        
    }
}
```

### 笔记

其实完全可以使用一个map来盛放两个方向的mapping。

注意Java中的map的添加操作是put而不是add。

---

## 二刷

### 代码

自己的代码
```java
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        
        if(head == null){
            return null;
        }
        
        HashMap<RandomListNode, RandomListNode> oldToNewNodeMap = new HashMap<RandomListNode, RandomListNode>();
        
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode newHead = dummy;
        
        RandomListNode temp = head;
        
        while(head != null){
            newHead.next = new RandomListNode(head.label);
            newHead = newHead.next;
            oldToNewNodeMap.put(head, newHead);
            head = head.next;
        }
        
        head = temp;
        newHead = dummy.next;
        while(head != null){
            if(head.random != null){
                newHead.random = oldToNewNodeMap.get(head.random);
            }
            head = head.next;
            newHead = newHead.next;
        }
        
        return dummy.next;
        
    }
}
```

九章的代码
```java
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    public RandomListNode copyRandomList(RandomListNode head) {
        // write your code here
        
        if(head == null){
            return null;
        }
        
        RandomListNode newListHead = new RandomListNode(head.label);
        RandomListNode firstNode = newListHead;
        
        Map<RandomListNode, RandomListNode> oldToNewMap = new HashMap<RandomListNode, RandomListNode>();
        Map<RandomListNode, RandomListNode> newToOldMap = new HashMap<RandomListNode, RandomListNode>();
        
        oldToNewMap.put(head, newListHead);
        newToOldMap.put(newListHead, head);
        
        while(head.next != null){
            RandomListNode newNode = new RandomListNode(head.next.label);
            newListHead.next = newNode;
            newListHead = newListHead.next;
            head = head.next;
            oldToNewMap.put(head, newListHead);
            newToOldMap.put(newListHead, head);
        }
        
        newListHead = firstNode;
        while(newListHead != null){
            RandomListNode originalNode = newToOldMap.get(newListHead);
            newListHead.random = oldToNewMap.get(originalNode.random);
            
            newListHead = newListHead.next;
        }
        
        return firstNode;
        
    }
}
```

### 笔记
这题还真是Amazon的高频题啊，自己的电面上次就是这题。

二刷也是一遍搞定，基本上和九章的版本一模一样。
主要思路就是：
**一个从old到new的HashMap配合两次while循环，第一次通过next指针来构建一遍新的list，并且建立起HashMap的的对应关系，第二遍用来通过hashMap的对应关系来将新的list中的random指针指向正确的地方**

自己的九章的不一样的地方就在于使用了dummy node，这里使用dummy node也不是不行，但是相比九章的办法稍微有点不是那么工整。因为在一开始就进行了`if(head == null)`的判断，所以之后在循环之前是可以先直接`RandomListNode newListHead = new RandomListNode(head.label);`的。