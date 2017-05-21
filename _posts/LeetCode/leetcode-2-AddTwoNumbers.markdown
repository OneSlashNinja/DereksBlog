---
layout: post
title:  "LeetCode 2 - Add Two Numbers"
date:   2017-05-17 23:24:02 -0400
categories: leetcode, Amazon
---

# Add Two Numbers

## 一刷

### 代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode lastNode = null;
        ListNode currentL1Node = null;
        ListNode currentL2Node = null;
        ListNode firstNode = null;
        
        Boolean carryOver = false;
        int result = l1.val+l2.val;
        if(result >= 10){
            carryOver = true;
            result -= 10;
        }else{
            carryOver = false;
        }
        
        firstNode = new ListNode(result);
        lastNode = firstNode;
        
        currentL1Node = l1.next;
        currentL2Node = l2.next;
        
        
        while(true){
            if(currentL1Node != null && currentL2Node != null){
                
                result = currentL1Node.val+currentL2Node.val;
                if(carryOver) result += 1;
                if(result >= 10){
                    carryOver = true;
                    result -= 10;
                }else{
                    carryOver = false;
                }
                
                lastNode.next = new ListNode(result);
                lastNode = lastNode.next;
                
                currentL1Node = currentL1Node.next;
                currentL2Node = currentL2Node.next;
                
            }else if(currentL1Node == null && currentL2Node == null){
                if(carryOver) lastNode.next = new ListNode(1);
                break;
            }else{
                result = currentL1Node != null ? currentL1Node.val : currentL2Node.val;
                if(carryOver) result += 1;
                if(result >= 10){
                    carryOver = true;
                    result -= 10;
                }else{
                    carryOver = false;
                }
                
                lastNode.next = new ListNode(result);
                lastNode = lastNode.next;
                
                currentL1Node = currentL1Node != null? currentL1Node.next : null;
                currentL2Node = currentL2Node != null? currentL2Node.next : null;
            }
        }
        
        return firstNode;
    }
}
```

### 笔记


---

## 二刷

### 代码

```java
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        if(l1 == null){
            return l2;
        }
        
        if(l2 == null){
            return l1;
        }
        
        ListNode dummy = new ListNode(0);
        
        ListNode head = dummy;
        
        int carry = 0;
        int valFromL1 = 0;
        int valFromL2 = 0;
        int currentDigit = 0;
        
        while(l1 != null || l2 != null){
            if(l1 != null){
                valFromL1 = l1.val;
                l1 = l1.next;
            }else{
                valFromL1 = 0;
            }
            
            if(l2 != null){
                valFromL2 = l2.val;
                l2 = l2.next;
            }else{
                valFromL2 = 0;
            }
            
            currentDigit = (valFromL1 + valFromL2 + carry) % 10;
            carry = (valFromL1 + valFromL2 + carry) / 10;
            head.next = new ListNode(currentDigit);
            head = head.next;
        }
        
        if(carry != 0){
            head.next = new ListNode(carry);
            head = head.next;
        }
        
        return dummy.next;
        
    }
}
```

### 笔记

1. 进位的技巧:
是否进位使用 (valFromL1 + valFromL2 + carry) / 10
余数使用 (valFromL1 + valFromL2 + carry) % 10

2. 
(1) 另外要注意考虑两个list不等长的情况。
(2) 另外不等长的一种极端情况就是某个list直接为0，这时可以直接不用计算返回另一个

3. 
使用dummy node不仅可以使得即使2.(2)中提到的情况也方便返回结果，而且更方便的是在返回最后结果的list时，直接使用dummy.next就可以定位了。