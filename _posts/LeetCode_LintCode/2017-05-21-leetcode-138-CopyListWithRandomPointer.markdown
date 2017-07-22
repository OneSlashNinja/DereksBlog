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


---

## 三刷

keys words: one HashMap, dummy node

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
    public RandomListNode copyRandomList(RandomListNode head) {
        
        if(head == null){
            return null;
        }
        
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        
        RandomListNode dummy = new RandomListNode(0);
        
        RandomListNode p = head;
        RandomListNode q = dummy;
        
        while(p != null){
            q.next = new RandomListNode(p.label);
            //注意q = q.next需要在map.put之前，而p = p.next需要在map.put之后
            q = q.next;
            map.put(p, q);
            p = p.next;
        }
        
        p = head;
        while(p != null){
            if(p.random != null){
                q = map.get(p); 
                q.random = map.get(p.random);
            }
            p = p.next;
        }
        
        return dummy.next;
    }
}
```

在怎么初始化第一个copy出来的RandomListNode的时候陷入混乱出不来了。

看了不同版本的，有使用HashMap和不适用HashMap的版本。这里暂时只看使用一个HashMap的版本。

在三刷的时候，发现怎么让第一次while启动起来完全没有概念了。看了Amazon九题的版本和二刷自己写的版本发现：

如果不使用dummy node，则要启动while循环，必须先单独创建第一个copy的node，否则while循环中完全没有copy的head可以使用。

而使用dummy node的版本，则因为已经有了dummy作为初始的指针，而可以直接开始进入while循环。

所以可以看出:**dummy node不仅适合于首指针可能会被操作的情景，对于这种需要创建新的一个List的情况，dummy node也能提供支持，并且dummy node还可以使得head随心所欲操作，最后要返回整个链表，直接返回dummy.next就可以了。总而言之，就是有百利而无一害(最多也就是多创建了一个额外的node)**

另外，对于这题，使用p和q作为整个链表复制过程中的变量名，不仅很明显，不会绕来绕去，而且在白板上也能省出很多时间。
