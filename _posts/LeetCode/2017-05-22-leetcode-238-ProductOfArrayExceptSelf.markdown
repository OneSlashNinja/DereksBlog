---
layout: post
title:  "LeetCode 238 - Product of Array Except Self"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Product of Array Except Self

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

自己的back and forth traverse版本
```java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        int arrLen = nums.length;
        
        int[] resultArr = new int[arrLen];
        int[] leftPrefixProductArr = new int[arrLen];
        int[] rightPrefixProductArr = new int[arrLen];
        
        leftPrefixProductArr[0] = nums[0];
        for(int i = 1; i < arrLen; i++){
            leftPrefixProductArr[i] = leftPrefixProductArr[i - 1] * nums[i];
        }
        
        rightPrefixProductArr[arrLen - 1] = nums[arrLen - 1];
        for(int i = arrLen - 2; i >= 0; i--){
            rightPrefixProductArr[i] = rightPrefixProductArr[i + 1] * nums[i];
        }
        
        for(int i = 0; i < arrLen; i++){
            int leftProduct = i == 0 ? 1 : leftPrefixProductArr[i - 1];
            int rightProduct = i == arrLen - 1 ? 1 : rightPrefixProductArr[i + 1];
            resultArr[i] = leftProduct * rightProduct;
        }
        
        return resultArr;
        
    }
}
```
leetcode的back and forth traverse版本
```java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        if(nums == null || nums.length == 0){
            return new int[0];
        }
        
        int[] result = new int[nums.length];
        
        int[] forward = new int[nums.length];
        int[] backward = new int[nums.length];
        forward[0] = backward[nums.length - 1] = 1;
        
        for(int i = 1; i < nums.length; i++){
            forward[i] = forward[i - 1] * nums[i - 1];
        }
        
        for(int i = nums.length - 2; i >= 0; i--){
            backward[i] = backward[i + 1] * nums[i + 1];
        }
        
        for(int i = 0; i < nums.length; i++){
            result[i] = forward[i] * backward[i];
        }
        
        return result;
    }
}
```

no extra space version
```java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        if(nums == null || nums.length == 0){
            return new int[0];
        }
        
        int[] result = new int[nums.length];
        result[0] = 1;
        
        for(int i = 1; i < nums.length; i++){
            result[i] = result[i - 1] * nums[i - 1];
        }
        
        int backward = 1;
        
        for(int i = nums.length - 1; i >= 0; i--){
            //注意顺序，backward的计算是在后面，就相当于最后一个i == 0时候的backward是没用的。
            //就像上一个版本中计算backward只计算了从nums.length - 1到1是一样的
            result[i] = result[i] * backward;
            backward = backward * nums[i];
        }
        
        return result;
    }
}
```

### 笔记

这一题三种版本的思想都是一致的，就是想要知道Product of Array Except Self，那么result[i] = [product of all element from 0 to i - 1] * [product of all elements from i + 1 to n - 1]

所以我们可以额外创建两个array，一个用来存prefix的product，一个用来存postfix的product。最后只需要从两个数组中提取相应的数字进行相乘就可以了。

自己的back and forth traverse版本和leetcode的版本相比的区别是自己的prefixarray就真的是从0到i的prefix，而leetcode的版本则是从0到除了自己以外的之前一个元素，也就是从0到i-1的元素。Postfix也是一样。

leetcode的版本这样的好处是对于后面计算最终结果非常直观。需要注意的是需要初始化第一个元素为1.


而不使用额外存储空间的版本其实是同样的思想，只不过是巧妙地精简了内存的使用:
(1)先是直接利用result的空间来存放prefix
(2)然后再从后循环一遍，直接计算出结果。(因为计算完一个结果后，其所在的postfix的值也就不再需要了，所以直接使用一个变量来代替当前的postfix就可以。)

