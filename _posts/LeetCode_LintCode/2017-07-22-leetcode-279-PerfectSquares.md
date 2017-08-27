---
layout: post
title:  "leetcode 279 - Perfect Squares"
date:   2017-07-22 19:15:33.141403
categories: leetcode, Google
---

# Perfect Squares

## 一刷

### 代码

想用Greedy做的错误版本：

```java
public class Solution {
    /**
     * @param n a positive integer
     * @return an integer
     */
    public int numSquares(int n) {
        // Write your code here
        
        int findFirstPowLess = findFirstPowLessThan(n);
        
        int left = n;
        
        int result = 0;
        
        while(left != 0 && findFirstPowLess != 0){
            while(left >= findFirstPowLess * findFirstPowLess &&
            left != 0 && findFirstPowLess != 0){
                
                System.out.println(left);
                
                left = left - findFirstPowLess * findFirstPowLess;
                result++;
            }
                findFirstPowLess--;
        }
        
        return result;
    }
    
    private int findFirstPowLessThan(int n){
        
        int trial = 1;
        
        while(trial * trial <= n){
            trial++;
        }
        
        return trial - 1;
        
    }
}
```

```java
public class Solution {
    /**
     * @param n a positive integer
     * @return an integer
     */
    public int numSquares(int n) {
        // Write your code here
        
        int sqrt = (int)Math.sqrt(n);
        
        int[] dp = new int[n + 1];
        
        Arrays.fill(dp, Integer.MAX_VALUE);
        
        dp[0] = 0;
        
        for(int i = 1; i <= sqrt; i++){
            dp[i * i] = 1;
        }
        
        for(int i = 1; i <= n; i++){
            for(int j = 1; i - j * j <= n && i - j * j >= 0; j++){
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        
        return dp[n];
        
    }
}
```

### 笔记(后来再看很多分析似乎不太到位)

这一题有点意思，一开始想用Greedy做：
找平方根然后向下取整得出sqrt，再循环n - sqrt * sqrt再重复这个过程直到被加完。

结果发现其实这题Greedy是错误的，很好的一个例子就是12：
如果用greedy的方法，那么找到的组合就是：9 + 1 + 1 + 1
而实际上:4 + 4 + 4

看了大家的题解之后发现主要的解法是DP(正好也符合只求最大或者最小值而不求具体的组合的特点)：

状态：
dp[i]表示数字i的Perfect Squares是多少

状态转换方程：
dp[i] = min(dp[i], dp[i-square]+1)

初始化状态：
dp[0] = 0 这是因为后面当dp[i - j * j] + 1当i = j*j时结果应该是1。所以dp[0] = 0

设i从1到sqrt(n), dp[i*i] = 1

其他状态都初始化为Integer.MAX_VALUE以方便后面Math.min()的计算。(因为是“其他状态”，所以应该把该初始化放在最前面，然后让前面的状态去覆盖相应的位置。)

结果:
dp[n]

注意是n不是n-1.这也是一道new dp[n + 1]的题。

注意虽然是一维DP，但是因为每一次都要再过一遍之前所有的可能，所以需要两层循环。
内层循环的终止条件要注意。


除了DP的解法外，其实本题还有一种更高效，但是很数学的解法，就是利用“四平方和定理”。
具体见Grandyang的题解。这里就不深入研究了。


最后，因为这题还额外注意到，其实求平方根完全没必要自己写，
Math.sqrt()就有现成的可用。只不过如果要向下取整，需要在前面再加一个(int):
int sqrt = (int)Math.sqrt(n);

再就是注意，如果要方便，将Arrays中的所有值都填充成某一确定值可以直接使用：
Arrays.fill(array, value);
来代替手动用for循环(当然，for循环更灵活，可以设置动态地值)


## 二刷

### 代码

```java
public class Solution {
    public int numSquares(int n) {
        
        int[] dp = new int[n + 1];
        
        for(int i = 1; i <= n; i++){
            dp[i] = i;
        }
        
        //其实dp[0]并没有什么含义
        dp[0] = 0;
        
        for(int i = 1; i * i <= n; i++){
            dp[i * i] = 1;
        }
        
        for(int i = 1; i <= n; i++){
            for(int j = 1; i + j * j <= n; j++){
                dp[i + j * j] = Math.min(dp[i + j * j], dp[j] + 1);
            }
        }
        
        return dp[n];
        
    }
}
```

替换双层循环的内外次序仍然能够work的版本
```java
public class Solution {
    public int numSquares(int n) {
        
        int[] dp = new int[n + 1];
        
        for(int i = 1; i <= n; i++){
            dp[i] = i;
        }
        
        //其实dp[0]并没有什么含义
        dp[0] = 0;
        
        for(int i = 1; i * i <= n; i++){
            dp[i * i] = 1;
        }
        
        for(int i = 1; i <= n; i++){
            for(int j = 1; j + i * i <= n; j++){
                dp[j + i * i] = Math.min(dp[j + i * i], dp[j] + 1);
            }
        }
        
        return dp[n];
        
    }
}
```


### 笔记

首先，这题第一的直觉是dfs肯定能做，不过java的话需要一个全局变量(或者传入一个只有一个值的int[])。而且复杂度肯定高的惊人。
而这题能比DFS更好的一个很明显的标志就是问的是"least number of ..."，而并不需要找到具体是哪一个组合。所以有很大可能是可以用dp解决的。

二刷的时候发现一刷的时候很多问题

那么先说这题使用dp分析

状态:
很直接，dp[i]就表示数字i的least number of perfect square numbers

状态转换方程:
dp[i + j * j] = Math.min(dp[i] + 1, dp[i + j * j]);

初始化条件:
注意不是dp[0] = 0;
而是
dp[i * i] = 1; i * i <=n

其实有了上述条件就肯定比较清晰了。说一下这题的注意点

1. 之所以声明的时候使用int[] dp = new int[n + 1];并不是和之前许多声明的长度 + 1的情况一样。
之前需要声明length + 1的dp是需要使用dp[0]作为初始化条件。但是这题你会发现dp[0]是完全没用的。

这题之所以enw int[n + 1]， 应该是为了状态的方便，因为dp[i]就表示数字i的least number of perfect square numbers。而其实使用int[n]也是可以做的，但是写起来会很麻烦。

这也是为什么for循环中结束条件都是<=n

2. 相比于一刷中使用了sqrt，其实完全不用。直接在for循环中的判读使用i * i <=n就可以表示。

3. 这题虽然是一维dp，但是使用两层循环来表示。因为需要两个变量:j来表示能组成perfect square的那个数，i来表示增量。有意思的是这次两层循环的位置是可以互换的，具体见自己二刷的code。

4. 注意初始条件是dp[i * i] = 1,dp[0]并没有什么意义。并且剩下的dp[i]可以初始化成为Integer.MAX_VALUE。其实可以初始化成i,因为至少i可以表示成i个1的和。
