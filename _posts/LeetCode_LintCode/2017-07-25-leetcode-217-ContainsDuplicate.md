---
layout: post
title:  "leetcode 217 - ContainsDuplicate"
date:   2017-07-25 21:08:27.771374
categories: leetcode, Palantir,Airbnb
---

# ContainsDuplicate

## 一刷

### 代码

```java
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        HashSet<Integer> set = new HashSet<Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i])){
                return true;
            }
            set.add(nums[i]);
        }
        
        return false;
    }
}
```

### 笔记

这题写出来非常简单，是一道很好的比较不同解法的题目，也为后面的follow up做准备。

这题可以想到的有三种方法:

(1) 暴力法，两两为一对进行比较，两层循环，空间复杂度O(1), 时间复杂度O(n^2)
(2) 排序法，整个数组先排序，然后每个数和自己的后一位进行比较，空间复杂度O(1),时间复杂度O(nlogn)
(3) HashSet法(这题问的是有没有，所以可以用HashSet，而如果问了具体什么坐标的话，则需要使用HashMap)，利用Hash的特点，空间复杂度O(n), 时间复杂度近似O(n)

具体请参考leetcode solution:

[Contains Duplicate - leetcode](https://leetcode.com/problems/contains-duplicate/#/solution)