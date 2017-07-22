---
layout: post
title:  "leetcode 268 - Missing Number"
date:   2017-07-16 19:27:25.592125
categories: leetcode, Microsoft
---

# Missing Number

## 一刷

### 代码

```java
public class Solution {
    /**    
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        // write your code here
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
        }
        
        return ((nums.length + 1) * nums.length) / 2 - sum;
    }
}
```

### 笔记

这道题给我们n个数字，是0到n之间的数但是有一个数字去掉了，让我们寻找这个数字，要求线性的时间复杂度和常数级的空间复杂度。那么最直观的一个方法是用等差数列的求和公式求出0到n之间所有的数字之和，然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字。

此题还有很多其他的解法。见Grandyang的解法。


---

## 二刷

### 代码

等差数列解法
```java
public class Solution {
    public int missingNumber(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return -1;
        }
        
        int idealSum = (1 + nums.length) * nums.length / 2;
        
        int actualSum = 0;
        
        for(int i = 0; i < nums.length; i++){
            actualSum += nums[i];
        }
        
        return idealSum - actualSum;
    }
}
```

xor解法
```java
public class Solution {
    public int missingNumber(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return -1;
        }
        
        int xor = 0;
        int i = 0;
        
        for(; i < nums.length; i++){
            xor = xor ^ i ^ nums[i];
        }
        
        return xor ^ i;
    }
}
```

### 笔记

二刷使用等差数列一次过。不过查看leetcode discuss发现还有xor的做法。主要是利用再创建一个从0...n的数列然后和目标数列整个一起xor，最后没有missing的number就会两两消除，而剩下的missing number就会留下来。

两者从时间复杂度上来看应该是一样的(其实等差数列应该更快，因为相当于等差数列是n的时间复杂度，xor是2n)。
