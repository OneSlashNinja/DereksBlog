---
layout: post
title:  "LeetCode 221 - Add Two Numbers II"
date:   2017-06-04 00:22:02 -0400
categories: lintcode, Amazon
---

# Add Two Numbers II

## 一刷

### 代码
```java

```

### 笔记


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
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    public ListNode addLists2(ListNode l1, ListNode l2) {
        // write your code here
        
        ListNode reversedL1 = reverseList(l1);
        ListNode reversedL2 = reverseList(l2);
        
        boolean carry = false;
        int currentDigit;
        
        ListNode dummy = new ListNode(0);
        ListNode newHead = dummy;
        
        while(reversedL1 != null && reversedL2 != null){
            currentDigit = (reversedL1.val + reversedL2.val + (carry ? 1 : 0)) % 10;
            carry = ((reversedL1.val + reversedL2.val + (carry ? 1 : 0)) / 10) > 0;
            
            newHead.next = new ListNode(currentDigit);
            newHead = newHead.next;
            reversedL1 = reversedL1.next;
            reversedL2 = reversedL2.next;
            
        }
        
        while(reversedL1 != null){
            currentDigit = (reversedL1.val + (carry ? 1 : 0)) % 10;
            carry = ((reversedL1.val + (carry ? 1 : 0)) / 10) > 0;
            newHead.next = new ListNode(currentDigit);
            newHead = newHead.next;
            reversedL1 = reversedL1.next;
        }
        
        while(reversedL2 != null){
            currentDigit = (reversedL2.val + (carry ? 1 : 0)) % 10;
            carry = ((reversedL2.val + (carry ? 1 : 0)) / 10) > 0;
            newHead.next = new ListNode(currentDigit);
            newHead = newHead.next;
            reversedL2 = reversedL2.next;
        }
        
        if(carry){
            newHead.next = new ListNode(1);
            newHead = newHead.next;
        }
        
        return reverseList(dummy.next);
        
    }
    
    private ListNode reverseList(ListNode l1){
        
        ListNode prev = null;
        ListNode next = null;
        
        while(l1 != null){
            next = l1.next;
            l1.next = prev;
            prev = l1;
            l1 = next;
        }
        
        return prev;
    }
    
}
```


### 笔记

这题还真没啥好说的，就是Add Two Numbers和Reverse Linked list的简单结合。

先反转两个参数linkedlist，然后完全按照add two numbers一样的步骤进行计算。最后再把结果翻转就是需要的答案。


## 三刷

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
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        
        ListNode dummy = new ListNode(0);
        
        ListNode head = dummy;
        
        int carry = 0;
        int sum = 0;
        while(l1 != null || l2 != null){
            
            sum = 0;
            if(l1 != null){
                sum += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                sum += l2.val;
                l2 = l2.next;
            }
            sum += carry;
            
            head.next = new ListNode(sum % 10);
            head = head.next;
            carry = sum / 10;
        }
        
        if(carry > 0){
            head.next = new ListNode(1);
            head = head.next;
        }
        
        ListNode result = reverseList(dummy.next);
        
        return result;
    }
    
    private ListNode reverseList(ListNode node){
        
        ListNode temp = null;
        ListNode prev = null;
        
        while(node != null){
            temp = node.next;
            node.next = prev;
            prev = node;
            node = temp;
        }
        
        return prev;
        
    }
}
```

### 笔记

二刷的版本太冗长了，被merge sort中的merge操作给思维定势了。其实这里的add和merge sort中的merge是有区别的，并不需要对两个list中的node进行比较，所以可以合并两者都有元素和只有一个list有元素的情况。

也就是说把

```java
while(reversedL1 != null && reversedL2 != null){
    ...
}
while(reversedL1 != null){
    ...
}
while(reversedL2 != null){

}
```

可以简化成配合一个**int sum**，只需要一个while循环就可以
```java
while(l1 != null || l2 != null){
    sum = 0;
    if(l1 != null){
        sum += l1.val;
        l1 = l1.next;
    }
    if(l2 != null){
        sum += l2.val;
        l2 = l2.next;
    }
    sum += carry;
    
    head.next = new ListNode(sum % 10);
    head = head.next;
    carry = sum / 10;
}
```

注意不管二刷还是三刷，都是用了dummy node的技巧。

另外，如果不考虑空间消耗，也可以使用stack来做，代码量会稍微小点，不过比起reverse的版本似乎并没有什么优势。