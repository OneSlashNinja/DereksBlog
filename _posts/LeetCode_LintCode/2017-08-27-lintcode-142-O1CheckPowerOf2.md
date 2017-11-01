---
layout: post
title:  "lintcode 142 - O(1) Check Power Of 2"
date:   2017-08-27 20:00:57.805635
categories: lintcode, Microsoft
---

# O1CheckPowerOf2

## 一刷

### 代码

最直接的思维，非O(1)时间的版本(但也通过了LintCode)
```java
class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        
        if(n <= 0){
            return false;
        }
        
        while(n % 2 == 0){
            n = n / 2;
        }
        
        return (n == 1);
        
    }
};
```

自己写的Bit Manipulation
```java
class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        
        if(n <= 0){
            return false;
        }
        
        int mask = 1;
        
        while(mask != 0){
            
            int result = n & mask;
            
            if(result == n){
                return true;
            }else if(result > 0){
                return false;
            }
            
            mask = mask << 1;
        }
        
        return false;
        
    }
};
```

最简洁的Bit Manipulation
```java
class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        
        if(n <= 0){
            return false;
        }
        
        return (n & (n - 1)) == 0;
        
    }
};
```

### 笔记

首先，这题不管是那种做法，都需要排除掉当n <= 0的条件。

第一种做法就是惯性思维能想到的最简答的方法，对于n进行连续的除2求余，一直到n不能被2整除，看结果是否为1，如果是1则肯定是2的power，反之则不是。

但这种做法显示不能达到O(1)的要求(虽然也过了LintCode)，而要达到O(1)的要求，想一下2的power的数有什么性质? 从比特位上来讲，就是**只有一个bit为1**

第二种做法是自己想到的标准的Bit Manipulation的做法，使用Mask进行一位一位的移动，从而进行判断。

最后一种做法是此题真正优雅简洁的做法，核心就是一行`(n & (n - 1)) == 0`。为什么呢? 

因为只有一个bit为1的特性，使得其如果-1，则会从该比特位向右全部取反。比如

```
0100 ==> 4
0011 ==> 3
```

而如果不是2的power，则肯定互有leading的几个位并不变动，也就不会达到`(n & (n - 1)) == 0`

参考见[O(1) Check Power of 2](http://www.code123.cc/docs/leetcode-notes/math_and_bit_manipulation/o1_check_power_of_2.html)