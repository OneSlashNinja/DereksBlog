---
layout: post
title:  "leetcode 461 - Hamming Distance"
date:   2017-07-23 14:34:10.056752
categories: leetcode, Facebook
---

# Hamming Distance

## 一刷

### 代码

```java
public class Solution {
    public int hammingDistance(int x, int y) {
        
        int mask = 1;
        
        int distance = 0;
        
        while(mask != 0){
            if(((mask & x) ^ (mask & y)) != 0){
                distance++;
            }
            
            mask <<= 1;
        }
        
        return distance;
    }
}
```

### 笔记

做完Hamming Weight，总结完套路后做这道题就是很轻松了。

唯一这里需要注意的就是这题要用到异或操作XOR，
既可以先x和y分别和mask进行&然后再xor，
也可以需要通过算出x和y的XOR，然后再和mask进行&。


Bit manipulation中要注意一点:

**&(或者 |, ^) 和 &&的优先级不一样，&&的优先级高于comparison，但是&的优先级lower于comparison。所以在写的时候很容易下意识的不加括号而写错**。
