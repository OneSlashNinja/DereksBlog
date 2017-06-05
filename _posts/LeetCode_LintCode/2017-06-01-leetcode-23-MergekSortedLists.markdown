---
layout: post
title:  "LeetCode 23 - Merge k Sorted Lists"
date:   2017-06-01 00:22:02 -0400
categories: leetcode, Amazon
---

# Merge k Sorted Lists

## 一刷

### 代码

version(PriorityQueue)
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
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {  
        // write your code here
        
        if(lists == null || lists.size() == 0){
            return null;
        }
        
        int k = lists.size();
        Comparator comp = new ListNodeComparator();
        Queue<ListNode> pq = new PriorityQueue<ListNode>(k, comp);
        
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        for(int i = 0; i < k; i++){
            if(lists.get(i) != null){
                pq.offer(lists.get(i));
            }
        }
        
        while(!pq.isEmpty()){
            ListNode newNode = pq.poll();
            tail.next = newNode;
            tail = tail.next;
            if(newNode.next != null){
                pq.offer(newNode.next);
            }
        }
        
        return dummy.next;
        
    }
    
    private class ListNodeComparator implements Comparator<ListNode> {
        public int compare(ListNode A, ListNode B){
            
            if(A == null){
                return -1;
            }
            
            if(B == null){
                return 1;
            }
            
            return A.val - B.val;
        }
    }
}
```

version(Divide and Conquer):
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
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {  
        // write your code here
        
        if(lists == null || lists.size() == 0){
            return null;
        }
        
        return mergeHelper(lists, 0, lists.size() - 1);
        
    }
    
    private ListNode mergeHelper(List<ListNode> lists, int start, int end){
        if(start == end){
            return lists.get(start);
        }
        
        int mid = start + (end - start) / 2;
        
        ListNode left = mergeHelper(lists, start, mid);
        ListNode right = mergeHelper(lists, mid + 1, end);
        
        return mergeTwoLists(left, right);
    }
    
    private ListNode mergeTwoLists(ListNode left, ListNode right){
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        while(left != null && right != null){
            if(left.val < right.val){
                tail.next = left;
                tail = tail.next;
                left = left.next;
            }else{
                tail.next = right;
                tail = tail.next;
                right = right.next;
            }
        }
        
        if(left != null){
            tail.next = left;
        }else{
            tail.next = right;
        }
        
        return dummy.next;
    }
    
    
}
```

### 笔记

此题很火，并且有三种解法，三种都要会。

思路上来说，最简单的应该算是PriorityQueue的解法。因为相当于有现成的功能强大的数据结构给你用，为何不用？

那么先说Java中PriorityQueue的使用：

首先，Java中PriorityQueue是Queue这个interface的一种具体实现。而我们用到的也都是Queue的各种常规操作（offer和poll），所以使用
Queue<ListNode> pq = new PriorityQueue<ListNode>(k, comp);这样的方式更能有OO的感觉。

然后说，PriorityQueue中的元素因为要取最大或者最小的，所以元素间是需要具有可比较性的。而对于题目中的这种情况，ListNode并没有实现Comparable接口，而我们也对该Class没有控制权，所以退而求其次，需要使用comparator。（具体comparable和comparator的比较见本题最后）。
那么Comparator作为一个class，应该写在哪儿？可以写在两个位置：
(1)和Solution同级，但是因为一个问题中只能有一个public class，所以如果写在这里就不能有public
(2)作为一个内部类(inner class)写在Solution的内部，那么最好是用private作为修饰。这里使用这种方式。

对于comparator的实现其实普通情况下直接return A.val - B.val;就好了。但是可能会有null的情况，所以最好再单独说明下某个“选手”为null的情况。

说完comparator，再回到PriorityQueue。PQ能够接受comparator作为参数的构造函数只有一个，而该函数有两个参数：
第一个是int initialCapacity，规定该PQ初始的容量（如果不指定则为11。而且这里只是初始的容量，并不是定死的，是可以扩容的）。
第二个就是comparator。

而该题比较有意思或者说恰好的一点就是：PQ从始至终只需要k个容量。

那么接下来的思路就很清晰：

(1)把k个LinkedList的头指针都压入PQ中(需要判断null的情况，因为压入null按理说是非法情况)
(2)用一个while循环（如果不仔细想会感觉是两层循环，一层处理k个list，一层处理每个list本身。但实际上利用PQ的特性，只用一层while就能直接走到底）来实现：
每次从PQ中提出最大的Node，然后链到目标list后面，然后再把该Node的后续元素压入PQ。直到整个PQ为空，说明所有元素都已经被转化到目标list上了。


Java中的Comparable和Comparator的比较和区别：

StackOverflow上的一个回答很好：

Comparator provides a way for you to provide custom comparison logic for types that you have no control over.

Comparable allows you to specify how objects that you are implementing get compared.

Obviously, if you don't have control over a class (or you want to provide multiple ways to compare objects that you do have control over) then use Comparator.

Otherwise you can use Comparable.

Comparable和Comparator的目标是一样的，都是为了使某个Class的各个object之间具有可比性，只不过是实现方式上的区别：
Comparable是直接让被比对的class（”选手“）去implements Comparable这个接口，从而该Class自己与生俱来就已经有了可比对性，在任何场合下都可以对其任意两个objects进行比较。

而Comparator是给进行比对的class（”裁判“）一个裁决方案，让其对某个指定类型的两个对象之间能够分出高下。因为某些情况下，要被比对的class并没有implements comparable，而我们对该需要比对的Class并没有control，或者说只是临时需要比对（或者需要比对的方式和该class自身comparable的并不相同？比如某个class有"智力值"和"武力值"）。那么就需要使用comparator

所以，如果对需要比对的class有控制权，那么应该先考虑使用comparable，这样对于以后会有更大的灵活性。要被比对的class并没有implements comparable，而我们对该需要比对的Class并没有control，或者说只是临时需要比对（或者需要比对的方式和该class自身comparable的并不相同？）。那么我们可以declare一个第三方的comparator class来专门说明该需要被比对对象的某种比对规则，然后作为一套规则或者说一个裁判传来用。

Comparable要实现的是compareTo方法，只需要一个”对手“参数。
Comparator要实现的是compare方法，需要两个参数，分别代表“对垒双方”


而另外两种方法放在一起比较会更容易记得清楚：
Divide and conquer和merge(小组赛打比赛)都是两两merge然后再把merge后的结果再两两merge。（两个解法都用到了mergeKLists或者说merge这个方法）
那么区别是什么呢？
从实现上来说，最大的区别就是分治用了递归而merge方法用的是两重循环的递推。

而从思想上方面
分治是宏观地抽象：每次使用二分，将list分为两个部分，再分再分，直到“触底”也就是start和end重合然后开始合并并返回。
而merge则是脚踏实地一点一点做起的“实干家”：每次两两merge两组，然后再将出线的重复该过程。

对于这两种方法，merge two list是基本功，主要的思路就是：
先
ListNode dummy = new ListNode(0);
ListNode tail = dummy;
然后用while循环地执行（注意要写循环）：
如果两个list都不为空，那么就比较当前head中谁小，然后添加到新的list的尾部，并且被取list向前走一步，新list也要向前走一步。

当跳出循环，就可以肯定两个list中至少有一个已经为null，那么把剩下不为null的那个直接整个添加在新list尾部即可。

另外注意这题从分治法的实现可以发现，其并不是把lists分身给拆分，而是利用了start和end两个参数，来模拟地将lists拆分，以后也可以学习这种方法。而这种方法的一个明显特点就是，因为参数数量和本身解题的函数的数量不对应，需要写一个额外的helper来进行专门的分治。


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
    public ListNode mergeKLists(ListNode[] lists) {
        return mergeHelper(lists, 0, lists.length - 1);
    }
    
    private ListNode mergeHelper(ListNode[] lists, int start, int end){
        
        //注意lists有可能为null或者是空list，所以最先判断的应该是这种情况
        if(lists == null || lists.length == 0){
            return null;
        }
        
        if(start == end){
            return lists[start];
        }
        
        int mid = start + (end - start) / 2;

        ListNode left = mergeHelper(lists, start, mid);
        //注意有+1
        ListNode right = mergeHelper(lists, mid + 1, end);
        
        return mergeTwoLists(left, right);
    }
    
    private ListNode mergeTwoLists(ListNode l1, ListNode l2){
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                head.next = l1;
                l1 = l1.next;
                head = head.next;
            }else{
                head.next = l2;
                l2 = l2.next;
                head = head.next;
            }
        }
        
        while(l1 != null){
            head.next = l1;
            l1 = l1.next;
            head = head.next;
        }
        
        while(l2 != null){
            head.next = l2;
            l2 = l2.next;
            head = head.next;
        }
        
        return dummy.next;
    }
}
```


### 笔记

二刷的时候使用了divide and conquer的方法来解的。
假设每个list的长度都为n，那么不管是用PriorityQueue还是divide and conquer，都是nlogk的时间复杂度。

使用divide的conquer的方法的话最重要的一点就是把merge two sorted list的merge作为基础操作，再配合分治的经典结构就可以解出，但是一定要注意的是再递归地去对右边进行调用的时候，需要使用(mid + 1),否则mid所在的元素就会被“分身”
