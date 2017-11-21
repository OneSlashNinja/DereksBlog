---
layout: post
title:  "leetcode 25 - Reverse Nodes In K Group"
date:   2017-11-19 21:44:32.213165
categories: leetcode, Expedia
---

# Reverse Nodes In K Group

## 一刷

### 代码

自己写的使用Stack代码比较简短的版本，但是占用额外O(k)的空间，
同样使用begin和end两指针
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
    /*
     * @param head: a ListNode
     * @param k: An integer
     * @return: a ListNode
     */
    public ListNode reverseKGroup(ListNode head, int k) {
        // write your code here
        
        if(head == null || head .next == null || k == 1){
            return head;
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode begin = dummy;
        ListNode end = head;
        
        Stack<ListNode> stack = new Stack<>();
        
        int count = 0;
        while(end != null || count == k){ //之所以还有个 || count == k是因为coner case有可能当end为null的时候，需要reverse的section正好还满足要求
            
            if(count == k){
                
                while(count != 0){
                    begin.next = stack.pop();
                    begin = begin.next;
                    count--;
                }
                begin.next = end;

            }else{
                stack.push(end);
                end = end.next;
                count++;
            }
        }
        
        return dummy.next;
    }
}
```

in place， 使用begin和end双指针版本
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
    /*
     * @param head: a ListNode
     * @param k: An integer
     * @return: a ListNode
     */
    public ListNode reverseKGroup(ListNode head, int k){
        
        if(head == null || head .next == null || k == 1){
            return head;
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode begin = dummy;
        
        int count = 0;
        while(head != null){
            
            count++;
            
            //因为count在之前就++了，当count == k时，说明head已经走到了last的前一个位置，就应该开始反转了（因为有可能正好last为null，但这种情况也需要反转,如果让head走到last的位置则会跳出循环)
            if(count == k){
                begin = reverseSection(begin, head.next);
                head = begin.next;
                count = 0;// reset count
            }else{
                head = head.next;
            }
            
        }
        
        return dummy.next;
    }
    
    //注意，该函数能被call则说明要被reverse的部分肯定至少有k的长度，所以可以放心next
    //return previous first element in the section, which is the last element in section afterwards
    private ListNode reverseSection(ListNode begin, ListNode end){
        
        //对于这题来说需要的额外两个变量
        ListNode current = begin.next;
        ListNode initialFirst = current;
        
        //普通reverseList也需要的两个变量
        ListNode prev = null;
        ListNode temp = null;
        
        //while中条件变成遇到end便是结尾
        while(current != end){
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        
        //因为是reverse section，所以最后还需要将reverse后的section的头尾"缝合"到整个list中去
        begin.next = prev;//此时prev已经是新的list的头了
        initialFirst.next = end;//此时initialFirst是新的list的尾
        
        return initialFirst;
    }
}
```

### 笔记

这题其实是Swap Nodes in Pairs的升级版，但难度一下从easy(leetcode中标注的是medium)陡升为hard。

第一个stack的版本的思路来自于[Youtube - Reverse Nodes In K group](https://www.youtube.com/watch?v=pLx1VP-FnuY)

基本思路就是利用stack的特性，使得指定的section能够得到reverse。该版本代码量较后面一种的版本稍微少一点，不过downside就是需要占用额外O(k)的空间。

第二个使用begin和end来配合加强版reverse函数的版本思路来自于
[leetcode discuss - Reverse Nodes in k-Group](https://discuss.leetcode.com/topic/12364/non-recursive-java-solution-and-idea)
，其中的图画的很好:

```
   /**
     * Reverse a link list between begin and end exclusively
     * an example:
     * a linked list:
     * 0->1->2->3->4->5->6
     * |           |   
     * begin       end
     * after call begin = reverse(begin, end)
     * 
     * 0->3->2->1->4->5->6
     *          |  |
     *      begin end
     * @return the reversed list's 'begin' node, which is the precedence of node end
     */
```

之所以说是加强版本的reverse是因为这次是需要reverse整个list中的某个区间，而不是整个list。所以需要两个辅助的begin和end来指向需要reverse的需要的前后。

而更精髓的是initialFirst这个指针，当经过reverse之后，它正好指向下一个需要reverse区间的begin。

本题的tricky的情况需要考虑当最后end已经为null，但是正好需要reverse的section的长度已经满足了k的情况。这种情况是需要仍然进行reverse的。