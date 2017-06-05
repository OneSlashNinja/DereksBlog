---
layout: post
title:  "LeetCode 234 - Palindrome Linked List"
date:   2017-05-31 00:15:02 -0400
categories: leetcode, Amazon
---

# Palindrome Linked List

## 一刷

### 代码
List转Array版本：
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
    /**
     * @param head a ListNode
     * @return a boolean
     */
    public boolean isPalindrome(ListNode head) {
        // Write your code here
        if(head == null){
            return true;
        }
        
        int length = findListLength(head);
        int[] arr = new int[length];
        
        int i = 0;
        while(head != null){
            arr[i] = head.val;
            
            head = head.next;
            i++;
        }
        
        return isPalindrome(arr);
        
    }
    
    private int findListLength(ListNode head){
        int length = 0;
        
        while(head != null){
            length++;
            head = head.next;
        }
        
        return length;
        
    }
    
    private boolean isPalindrome(int[] arr){
        int left = 0, right = arr.length - 1;
        
        while(left < right){
            if(arr[left] == arr[right]){
                left++;
                right--;
            }else{
                return false;
            }
        }
        
        return true;
    }
}
```

reverse List版本(自己想到的哦！:)
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
    /**
     * @param head a ListNode
     * @return a boolean
     */
    public boolean isPalindrome(ListNode head) {
        // Write your code here
        if(head == null){
            return true;
        }
        
        ListNode middle = findMiddle(head);
        ListNode rightHead = reverseList(middle);
        
        while(head != null && rightHead != null){
            if(head.val == rightHead.val){
                head = head.next;
                rightHead = rightHead.next;
            }else{
                return false;
            }
        }
        
        return true;
    }
    
    private ListNode findMiddle(ListNode head){
        
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        
        return slow;
    }
    
    private ListNode reverseList(ListNode head){
        
        ListNode prev = null;
        ListNode temp = null;
        
        while(head != null){
            temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        
        return prev;
        
    }
    
}
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
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null){
            return true;
        }
        
        int len = getListLength(head);
        
        //一开始感觉要对是否(len % 2 == 0)分情况进行讨论，但是在纸上演算了一下发现
        //其实无论len是奇数还是偶数都直接除2就可以了
        len = len / 2;
        
        ListNode leftHead = head;
        for(int i = 0; i < len; i++){
            head = head.next;
        }
        
        ListNode rightHead = reverseLinkedList(head);
        
        for(int i = 0; i < len; i++){
            if(leftHead.val == rightHead.val){
                leftHead = leftHead.next;
                rightHead = rightHead.next;
            }else{
                return false;
            }
        }
        
        return true;
    }
    
    private int getListLength(ListNode head){
        int len = 0;
        
        while(head != null){
            head = head.next;
            len++;
        }
        return len;
    }
    
    private ListNode reverseLinkedList(ListNode head){
        ListNode prev = null;
        ListNode next = null;
        
        while(head != null){
            next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        
        return prev;
    }
    
}
```


### 笔记

看到题目中说*Could you do it in O(n) time and O(1) space?*的提示就想起来了要用reverse Linked list来做

基本就是找到长度，然后从中间开始进行后半段Linked list的reverse。然后分别从left和right两个end同时开始比较已经移动，直到移过了len/2的长度，如果都一致则肯定是Palindrome的。

唯一需要注意的就是程序中标明了注释的地方，对于list的长度到底是奇数还是偶数，都是从len/2处开始进行reverse，该过程可以自己手动举个比如长度为3的例子进行演算。