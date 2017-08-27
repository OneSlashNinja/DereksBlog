---
layout: post
title:  "leetcode 277 - Find the Celebrity"
date:   2017-07-22 21:32:33.915803
categories: leetcode, Facebook, Linkedin
---

# Find the Celebrity

## 一刷

### 代码

自己写出的O(n^2)的版本
```java
public class Solution extends Relation {
    public int findCelebrity(int n) {
        for(int i = 0; i < n; i++){
            int j = 0;
            for(; j < n; j++){
                if(i == j){
                    continue;
                }

                if(knows(i, j) || !knows(j, i)){
                    break;
                }
            }

            if(j == n){
                return i;
            }
        }
        
        return -1;
    }

}
```

O(1)版本
```java
/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        
        int candidate = 0;
        
        for(int i = 1; i < n; i++){
            if(knows(candidate, i)){
                candidate = i;
            }
        }
        
        for(int i = 0; i < n; i++){
            if(candidate == i){
                continue;
            }
            
            if(knows(candidate, i) || !knows(i, candidate)){
                return -1;
            }
        }
        
        return candidate;
        
    }
}
```

### 笔记

这题还是蛮有意思的一道题。关键点就是celebrity的特征:**其他任何人都认识他，但他不认识其他任何人**。但凡不满足这两个条件中的任何一个，就肯定不是名人。那其实最直接的解法就是把上面的这种条件转换为程序代码就可以了。

最直接的实现自然可以想到是**两层for，每次假定某个人i是名人，然后分别去看他跟剩下的每个人j的关系。**

这题的一个技巧就在于: 如何表示某个人是否经过了重重考验，最后被认定为时名人？

这个技巧就是在strstr中用到的技巧: **把for中对于循环变量j的声明和初始化拿到循环外**，这样，在循环内如果满足条件则什么也不做，而不满足条件则break。这样只要在循环结束后就可以使用j跟整个数组的长度进行比较，如果相等，则说明通过了"重重考验"，不等于则说明肯定在某一点上不满足。

这种解的时间复杂度是O(n^2),是不是还可以再优化呢？


优化的版本非常巧妙，相当于一遍循环就利用了三个条件:

(1)celebrity谁也不认识

(2)谁都认识celebrity

(1)最多只可能有一个celebrity

所以在一遍循环的过程中，可以想象，假定真的有这个一个celebrity，那么肯定是所有人的指向这个celebrity，而celerity不指向任何人，所以在一遍扫描的筛选过程中，如果有celebrity而当前candidate不是celebrity，那么肯定会在某个时候这个假candidate因为指向了真candidate而把"接力棒"交给了真candidate。而真candidate因为不指向任何人，所以肯定不会把"接力棒"交给任何人。

并且因为最多只可能有一个celebrity，所以这个过程也不会漏选谁。

不过上述循环是建立在”肯定有这个一个celebrity“的基础上选出来的candidate，到底是不是真的有这么一个celebrity其实并不确定，所以需要使用这个candidate进行一次循环，比对和其他人的关系进行一次验证。

所以，two pass完成，时间复杂度O(n),非常巧妙。
