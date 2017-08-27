---
layout: post
title:  "leetcode 477 - Total Hamming Distance"
date:   2017-07-23 15:55:27.882420
categories: leetcode, Facebook
---

# Total Hamming Distance

## 一刷

### 代码

根据Hamming Distance直接改写的版本，O(n^2)超时
```java
public class Solution {
    public int totalHammingDistance(int[] nums) {
        int totalDistance = 0;
        
        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                totalDistance += hammingDistance(nums[i], nums[j]);
            }
        }
        
        return totalDistance;
    }
    
    private int hammingDistance(int x, int y){
        int mask = 1;
        int xor = x ^ y;
        int distance = 0;
        
        while(mask != 0){
            if((mask & xor) != 0){
                distance++;
            }
            mask <<= 1;
        }
        
        return distance;
    }
}
```

优化版本,O(n)
```java
public class Solution {
    public int totalHammingDistance(int[] nums) {
        
        int mask = 1;
        
        int totalOnes = 0;
        
        while(mask != 0){
            int currentOnes = 0;
            
            for(int i = 0; i < nums.length; i++){
                if((nums[i] & mask) != 0){
                    currentOnes++;
                }
            }
            
            totalOnes += currentOnes * (nums.length - currentOnes);
            
            mask <<= 1;
        }
        
        return totalOnes;
        
    }
}
```

### 笔记

这题很明显可以看出是Hamming Distance的follow up，那么自然最容易想到的解法就是使用Hamming Distance的解法作为子方法，然后双重循环(注意内层的起点j = i + 1以防重复)找出所有的非重复组合，计算total。

但是分析会发现这种方法的时间复杂度为O(n^2),会在大数据量的时候超时。

那么怎么优化呢？

Leetcode的solution中的优化方法非常巧妙:

首先，大的层面上来说，不单独地去计算每个num的hamming Distance然后加起来，而是先计算每个num的每个bit的hamming Distance之和，然后再加起来。

这样，在计算所有num的某个bit的hamming Distance时就有优化可以做:

想一下hamming Distance的定义是什么?如果某个bit上出现不一样的位则为1个hamming Distance，那么hamming Distance肯定就是两个num中一个有1，一个有0的情况。

那么我们就可以统计某个bit上到底有几个1？假设有i个1，那么就可以直接知道有nums.length - i个0.所以我们可以**将原先枚举式的找组合，变成直接的运算**。这样的话，sum上所有32位的和，就是最终结果。

而时间复杂度也从之前的O(n^2)降为了O(n)

