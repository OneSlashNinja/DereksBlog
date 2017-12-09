---
layout: post
title:  "lintcode 681 - First Missing Prime Number"
date:   2017-11-24 23:09:29.114846
categories: lintcode, Zynga
---

# First Missing Prime Number

## 一刷

### 代码

```java
public class Solution {
    /*
     * @param : an array of integer
     * @return: the first missing prime number
     */
    public int firstMissingPrime(int[] nums) {
        // write your code here
        
        Set<Integer> set = new HashSet<Integer>();
        
        for(int i = 0; i < nums.length; i++){
            set.add(nums[i]);
        }
        
        //注意，上限是Integer.MAX_VALUE而不是nums中最大的，因为有可能该prime根本不在nums中的数的范围
        for(int i = 2; i < Integer.MAX_VALUE; i++){
            if(set.contains(i)){
                continue;
            }
            
            if(isPrime(i)){
                return i;
            }
        }
        
        return -1;
    }
    
    private boolean isPrime(int num){
        for(int i = 2; i * i <= num; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
};
```

### 笔记

这题至自己做出来为止似乎搜不到什么大神写的版本，可能是太新了并且leetcode上还没有出来。

自己的思路其实很简单:
* 需要一个isPrime的辅助函数，具体见"CountPrime"自己的笔记来找到isPrime的最优写法，也就是` i * i <= num;`这个关键点
* 然后整个程序的思路就变成了，先把所有元素都装进一个Set中。然后从2开始，一直到无穷大地进行遍历检测，如果某个数不在set中，然后又是prime，那么第一个碰到的这个数就是要找的数。

时间复杂度:?? 空间复杂度:O(n)