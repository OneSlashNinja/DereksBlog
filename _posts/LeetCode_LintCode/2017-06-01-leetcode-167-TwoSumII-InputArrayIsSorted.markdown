---
layout: post
title:  "LeetCode 167 - Two Sum II - Input array is sorted"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Two Sum II - Input array is sorted

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

```java
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        int[] result = new int[2];
        result[0] = result[1] = -1;
        
        if(numbers == null || numbers.length == 0){
            return result;
        }
        
        int left = 0, right = numbers.length - 1;
        
        while(left < right){
            if(numbers[left] + numbers[right] == target){
                result[0] = left + 1;
                result[1] = right + 1;
                return result;
            }
            
            if(numbers[left] + numbers[right] < target){
                left++;
            }else{
                right--;
            }
        }
        
        return result;
        
    }
}
```


### 笔记

其实就是Two Sum的Two pointer版本省去了sorting，所以时间是O(n),空间是O(1)的。

其他也没啥好说的了，注意到底是什么情况下left++,什么情况下right--就好了。