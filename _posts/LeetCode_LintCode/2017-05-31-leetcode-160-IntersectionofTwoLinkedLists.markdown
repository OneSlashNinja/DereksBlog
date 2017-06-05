---
layout: post
title:  "LeetCode 160 - Intersection of Two Linked Lists"
date:   2017-05-31 00:15:02 -0400
categories: leetcode, Amazon
---

# Intersection of Two Linked Lists

## 一刷

### 代码

看了思路后的自己第一个版本：
```java
/**
 * Definition for singly-linked list.
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
    /**
     * @param headA: the first list
     * @param headB: the second list
     * @return: a ListNode 
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // Write your code here
        
        if(headA == null || headB == null){
            return null;
        }
        
        int lenA = 0;
        int lenB = 0;
        
        ListNode currentA = headA;
        ListNode currentB = headB;
        
        while(currentA != null && currentA.next != null){
            currentA = currentA.next;
            lenA++;
        }
        lenA++;
        
        while(currentB != null && currentB.next != null){
            currentB = currentB.next;
            lenB++;
        }
        lenB++;
        
        if(currentA != currentB){
            return null;
        }
        
        if(lenA > lenB){
            int diff = lenA - lenB;
            currentA = headA;
            currentB = headB;
            for(int i = 0; i < diff; i++){
                currentA = currentA.next;
            }
        }else{
            int diff = lenB - lenA;
            currentA = headA;
            currentB = headB;
            for(int i = 0; i < diff; i++){
                currentB = currentB.next;
            }
        }
        
        while(currentA != currentB && currentA != null && currentB != null){
            currentA = currentA.next;
            currentB = currentB.next;
        }
        
        return currentA;//or return currentB
        
    }  
}
```

稍微改进的版本：
```java
/**
 * Definition for singly-linked list.
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
    /**
     * @param headA: the first list
     * @param headB: the second list
     * @return: a ListNode 
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // Write your code here
        
        if(headA == null || headB == null){
            return null;
        }
        
        int lenA = getListLength(headA);
        int lenB = getListLength(headB);
        
        ListNode currentA = headA;
        ListNode currentB = headB;
        
        if(lenA > lenB){
            int diff = lenA - lenB;
            for(int i = 0; i < diff; i++){
                currentA = currentA.next;
            }
        }else{
            int diff = lenB - lenA;
            for(int i = 0; i < diff; i++){
                currentB = currentB.next;
            }
        }
        
        while(currentA != currentB && currentA != null && currentB != null){
            currentA = currentA.next;
            currentB = currentB.next;
        }
        
        return currentA;//or return currentB
        
    }
    
    private int getListLength(ListNode node){
        int len = 0;
        
        ListNode current = node;
        
        while(current != null){
            current = current.next;
            len++;
        }
        
        return len;
    }
}
```

### 笔记

首先，本题也有对应的array版本"Intersection of two array"。但是和其他array和linkedlist的题目的不同有一点本质的区别：
array的版本找的是“value”的intersection，而linkedlist的版本找的是“reference”的intersection。
所以其实是完全不同的题目。这道题实际上找的不是说有哪些点的value相等。而是找两个linkedlist“汇入同一条河流”的入口。

一开始自己的思路是，如果两个head都走到list的尽头，然后比较是否相等，是可以至少知道这两个list是否有intersection的，但是没有办法知道这个intersection在哪儿。而从两个list的头开始判断node相等，又不知道这个“节奏”该如何把握，也许listA和ListB已经走到共同的“河流之中”，但是比较的不是同一个点，也是没有办法进行判定的。

那怎么办？其实很简单，就是先找到两个list的长度，然后让长的先走长出来的长度。这时，再让两个node同时前进，就可以肯定，如果走到了“入河口”，必定是两个list同时走到的，可以每次判断两个node来看是否intersection。

自己写了两个版本，其实都各有优点：
(1)版本2的优点很明显，主要是把“获取list的长度”作为一个单独的方法提取了出来。这样的提取有两个好处，一来程度的代码立马缩短了很多，并且增加了服用性。再次，把如何获取list的长度的具体实现分离了出去，如果想改成不是一个指针一直到头，而是使用快慢指针，也可以很方便改动。

(2)版本1的优点其实主要在于，在找两个list的长度时，就可以把currentA和currentB留在最后一个node，然后这时候像之前说的判断如果这两个node不相等，那么直接就可以返回null了，而后面的各种操作都可以提前短路掉，提升效率。但是程序也因此会比较长和繁琐。

另外，本题还有一种比较屌的解决方法，见Yu's garden的说明，但是似乎有点玄乎，在此不做讨论。

---

## 二刷

### 代码

```java
/**
 * Definition for singly-linked list.
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
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int listALen = getLengthOfList(headA);
        int listBLen = getLengthOfList(headB);
        
        if(listALen > listBLen){
            for(int i = 0; i < listALen - listBLen; i++){
                headA = headA.next;
            }
        }else if(listBLen > listALen){
            for(int i = 0; i < listBLen - listALen; i++){
                headB = headB.next;
            }
        }
        
        while(headA != null && headB != null){
            if(headA == headB){
                return headA;
            }
            headA = headA.next;
            headB = headB.next;
        }
        
        return null;
    }
    
    private int getLengthOfList(ListNode head){
        
        int length = 0;
        
        while(head != null){
            head = head.next;
            length++;
        }
        
        return length;
    }
}
```


### 笔记

二刷的时候观察后稍微思考了下就发现或者说回想起了这题的trick:就是**先计算长度**,知道了两个list分别的长度后，可以让长的先走长出来的步数，使得两个选手都在“同一起跑线上”，这样的话就可以以同样的速度同时出发，如果有intersection，那么肯定会出现headA==headB的情况。

二刷发现即使是同样的方法，感觉第二次写的会更简洁，感觉多练果然还是会有更好的代码感的。