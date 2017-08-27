---
layout: post
title:  "leetcode 191 - Hamming Weight (Number Of 1 Bits)"
date:   2017-07-23 13:48:07.044850
categories: leetcode, Microsoft,Apple
---

# Hamming Weight (Number Of 1 Bits)

## 一刷

### 代码

标准的使用mask的版本
```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int bits = 0;
        int mask = 1;
        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0) {
                bits++;
            }
            mask <<= 1;
        }
        return bits;
    }
}
```

自己写的使用mask的版本
```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        
        int mask = 1;
        
        int totalOne = 0;
        
        while(mask != 0){
            int result = mask & n;
            //注意是result != 0而不是result > 0
            if(result != 0){
                totalOne++;
            }
            mask <<= 1;
        }
        
        return totalOne;
    }
}
```

使用mask但是shift的是n的版本(稍微会有优化)
```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        
        int mask = 1;
        
        int totalOne = 0;
        
        while(n != 0){
            int result = mask & n;
            //注意是result != 0而不是result > 0
            if(result != 0){
                totalOne++;
            }
            //注意，这里要使用 >>> (unsigned right shift)
            n >>>= 1;
        }
        
        return totalOne;
    }
}
```

利用least significant 1-bit的版本
```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        
        int bitNum = 0;
        
        while(n != 0){
            bitNum++;
            n &= (n - 1);
        }
        
        return bitNum;
    }
}
```

### 笔记

这题是标准的bit manipulation题。而且是必须使用bit manipulation的题。

使用标准的bit manipulation的破冰器就是mask掩码。

利用 int mask = 1，然后配合 mask <<= 1和 逻辑与&或者逻辑或|或者xor^等，来对每个bit进行操作或者验证。

这题就完全可以利用这种套路。

使用这种套路时需要需要注意几个地方:

1. 
基本的int是32位，所以应该使用mask来进行32次的比对。
但是在写for的时候会非常迷惑:

mask的1已经在最后一位了，那总共32位，是不是只移动31次就行了，所以是不是应该是
for (int i = 0; i < 31; i++)
然后又发现，因为mask是放在比对的逻辑的后面，所以还是应该执行32次Shift。

所以，针对上面这种情况，其实更好的一种写法是直接使用
while(mask != 0){...}当1被移出mask后以后mask就变成0了，也就不用操心到底Shift了几次，也就是自己的写法。


2. 注意，不管是while中的,还是if中的判断，都是mask != 0而不是mask > 0，因为对于unsigned int，移到最后一位时会变成负数。

3. 同样是使用mask，但是可以shift n而不是mask。这样的稍微的优化是如果碰到像0....101这样的数字，那么只要移动3次就能使得n==0，而之前的版本固定会移动32次。但是这种做法要注意的一个问题是需要使用unsigned right shift,也就是>>>。这样就不会有可能把左边全部置为1.

shift操作只有三种:
`The operators << (left shift), >> (signed right shift), and >>> (unsigned right shift) are called the shift operators`
并没有unsigned left shift

---

比起移动n的版本，还有一种利用**flips the least-significant 1-bit**的方法更加简单并且优化，就是写的最后一种。least-significant 1-bit也就是最后一位1。

**使用n & (n - 1)就可以将最后一位1置为0**，这样的话，就可以跳过所有的后面的0，n中有多少个1，就会执行多少次n & (n - 1)，可谓是最优化的版本。

具体见Leetcode solution
[LeetCode Solution - Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/#/solution)

虽然上面的几种版本中的时间复杂度都是O(1){因为最多只会执行确定的32次shift操作}，但是会有不同的优化程度。