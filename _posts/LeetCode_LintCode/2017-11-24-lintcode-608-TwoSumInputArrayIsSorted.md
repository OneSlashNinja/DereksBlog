---
layout: post
title:  "lintcode 608 - Two Sum Input Array Is Sorted"
date:   2017-11-24 20:23:14.397023
categories: lintcode, Amazon
---

# Two Sum Input Array Is Sorted

## 一刷

### 代码

```java
public class Solution {
    /*
     * @param nums: an array of Integer
     * @param target: target = nums[index1] + nums[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] nums, int target) {
        // write your code here
        
        int[] result = {-1, -1};
        
        if(nums == null || nums.length == 0){
            return result;
        }
        
        int l = 0, r = nums.length - 1;
        
        while(l < r){
            int sum = nums[l] + nums[r];
            
            if(sum > target){
                r--;
            }else if(sum < target){
                l++;
            }else{
                result[0] = l + 1;//要求的是以1为底的下标
                result[1] = r + 1;
                break;
            }
        }
        
        return result;
    }
}
```

### 笔记

此题没啥太多好说的，Two Sum的两种经典解法:(1) HashMap, (2) Two pointers

前者时间复杂度O(n)但是需要O(n)的额外空间，后者不需要额外空间，但是时间复杂度是O(nlogn)

而现在给的是排好序的数组，那么完全肯定一定就是第二种做法啦，一个while循环配合俩指针一遍扫描O(n)时间搞定。