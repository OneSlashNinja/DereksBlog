---
layout: post
title:  "leetcode 287 - Find The Duplicate Number"
date:   2017-10-14 22:50:12.840939
categories: leetcode, Bloomberg
---

# Find The Duplicate Number

## 一刷

### 代码

```java
class Solution {
    public int findDuplicate(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return -1;
        }
        
        int start = 1, end = nums.length - 1;
        while(start < end){
            
            int mid = start + (end - start) / 2;
            
            int count = 0;
            for(int i = 0; i < nums.length; i++){
                if(nums[i] <= mid){
                    count++;
                }
            }
            
            if(count > mid){
                end = mid;
            }else if(count < mid){
                start = mid + 1;
            }else{
                start = mid + 1;
            }
            
        }
        
        return start;
        
        
    }
}
```

为了证明使用`while(start + 1 < end)`的形式也能做的版本
```java
class Solution {
    public int findDuplicate(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return -1;
        }
        
        int start = 1, end = nums.length - 1;
        while(start + 1 < end){
            
            int mid = start + (end - start) / 2;
            
            int count = 0;
            for(int i = 0; i < nums.length; i++){
                if(nums[i] <= mid){
                    count++;
                }
            }
            
            if(count > mid){
                end = mid;
            }else if(count < mid){
                start = mid;
            }else{
                start = mid;
            }
            
        }
        
        //最后需要再将count和缩小范围后的两个结果进行比较
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] <= start){
                count++;
            }
        }
        
        if(count <= start){
            return end;
        }
        
        return start;
        
        
    }
}
```


### 笔记

感觉这题说是medium还是小看了它，起码得是中上甚至hard的级别，还是稍微有点烧脑的。不过帮我缕清了binary search很多东西。见自己binary search的总结。

一开始审题没审清楚，以为跟lintcode中的first missing number解法一样，只不过从missing变成了duplicate。以为使用等差数列求和，再把整个数列的数值相加，一减就可以了。

结果发现，虽然duplicate的num只有一个，但这个num可能会有多个分身，也就是多个duplicate，那么等差数列的方法就不能写了。

而这题又有很多的限制:
* You must not modify the array (assume the array is read only).
* You must use only constant, O(1) extra space.
上两条否定了排序的可能。

* Your runtime complexity should be less than O(n2).
这一条说明不能直接暴力检测。
* There is only one duplicate number in the array, but it could be repeated more than once.

那么复杂度肯定需要在O(nlogn)甚至O(n)的级别。

还别说，两种实现都有。

O(nlogn)的时间复杂度利用的是比较特殊的二分搜索(**应该属于二分结果型**)，在每次的搜索过程中需要进行O(n)的count，所以总体时间复杂度是O(nlogn).

而这里能使用二分的一个重要理论依据就是**鸽笼原理(Pigeonhole Principle)**

这篇对二分的解释比较好[LeetCode 287. Find the Duplicate Number | 智商被碾压！](https://boweihe.me/2016/03/30/leetcode-287-find-the-duplicate-number-%E6%99%BA%E5%95%86%E8%A2%AB%E7%A2%BE%E5%8E%8B%EF%BC%81/)

这个鸽笼原理对于理解解法中的很多点很重要。

首先，注意start并不是从0开始，而是从1开始，而end虽然是nums.length - 1，但意义和之前不一样，代表虽然有个nums.length个数，但是由于有duplicate，所以最多只到nums.length - 1.

其中一开始最不明白的地方就是: **为什么count == mid时，需要start = mid + 1**？

利用鸽笼原理，从start到end之间的数字中，取中间数mid，然后把整个array中<=mid的数字统计一遍，作为count。

当count < mid时，可以知道从start到mid之间的鸽笼肯定是有富余的

比如[1,2,3,3,4]
