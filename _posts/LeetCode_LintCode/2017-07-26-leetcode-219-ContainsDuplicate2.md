---
layout: post
title:  "leetcode 219 - Contains Duplicate 2"
date:   2017-07-26 22:21:55.349593
categories: leetcode, Palantir,Airbnb
---

# Contains Duplicate 2

## 一刷

### 代码

```java
public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
        HashSet<Integer> set = new HashSet<>();
        
        for(int i = 0; i < nums.length; i++){
            if(i - k >= 1){
                set.remove(nums[i - k - 1]);
            }
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