---
layout: post
title:  "Lintcode 532 - Reverse Pairs"
date:   2017-05-21 00:15:02 -0400
categories: lintcode, Amazon
---

# Reverse Pairs

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

基于merge sort的方法
```java
public class Solution {
    /**
     * @param A an array
     * @return total of reverse pairs
     */
    public long reversePairs(int[] A) {
        // Write your code here
        if(A == null || A.length == 0){
            return 0;
        }
        
        int[] temp = new int[A.length];
        
        return mergeSort(A, 0, A.length - 1, temp);
    }
    
    private long mergeSort(int[] A, int start, int end, int[] temp){
        
        if(start >= end){
            return 0;
        }
        
        int sum = 0;
        int mid = start + (end - start) / 2;
        sum += mergeSort(A, start, mid, temp);
        sum += mergeSort(A, mid + 1, end, temp);
        sum += merge(A, start, mid, end, temp);
        
        return sum;
    }
    
    private long merge(int[] A, int start, int mid, int end, int[] temp){
        int left = start;
        int right = mid + 1;
        int index = start;
        int sum = 0;
        
        while(left <= mid && right <= end){
            if(A[left] <= A[right]){
                temp[index++] = A[left++];
            }else{
                //比如是左边是2，5，9，右边是1，3，7，当左边指向2右边指向1时，
                //因为是增序，所以知道1肯定会小于所有左边剩下的数，但是不能保证2大于所有右边的数
                //所以是sum += mid - left + 1, 而不是sum += end - right + 1;
                sum += mid - left + 1;
                temp[index++] = A[right++];
            }
        }
        
        while(left <= mid){
            temp[index++] = A[left++];
        }
        
        while(right <= end){
            temp[index++] = A[right++];
        }
        
        for(int i = start; i <= end; i++){
            A[i] = temp[i];
        }
        
        return sum;
    }
    
}

```


### 笔记

这题直接能想到的肯定是暴力法，直接两层循环，固定住一个数字后，对其后的数字进行比较。但是这样的时间复杂度是O(n^2)的。

而冥冥之中感觉这题肯定是有某种方法，就像使用Dequeue解出"SlidingWindowMaximum"中的方法一样，会有某种"部分排序"的方法，使得秩序需要排我们关系的部分的序而更有效地解出答案。

那么这道题就正好地可以利用merge sort的过程，搭上这趟快车，**主要是利用merge的过程中，两个要merge的array都是各自有序的这一特点，然后可以直接统计出符合reverse pair的数量。而且当这个数量被统计以后，两个array就会merge成一个有序的array，这个信息就会被消除，以更方便地服务下一个merge的计算。非常巧妙**

要注意因为是array的merge sort，所以需要额外一块和原数组一样大的数组作为额外的空间。这点和"merge k sorted linked list"不一样，要注意。

本题中最需要注意的一点就是在统计sum的时候，到底是sum += mid - left + 1;还是sum += end - right + 1;要想清楚。

使用了merge sort，复杂度降为"O(nlogn)"

这一题使用merge sort的方法其实是一种特殊方法。更加一般性的方法其实可以参考题目**"Count of Smaller Numbers After Self"**