---
layout: post
title:  "leetcode 322 - Coin Change"
date:   2017-11-12 19:23:38.687147
categories: leetcode, Bloomberg
---

# Coin Change

## 一刷

### 代码


暴力Backtracking
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        
        //若是amount本身就是0或者负数，那么直接就达到目标了，返回0即可
        if(amount < 1){
            return 0;
        }
        
        //在经过了前面的filter后，现在的amount肯定是>=1的了，而这种情况下如果没有coins可选，那么肯定没有可行方案，直接返回-1
        if(coins == null || coins.length == 0){
            return -1;
        }
        
        return coinChangeHelper(coins, amount);
        
    }
    
    private int coinChangeHelper(int[] coins, int remaining){
        
        if(remaining < 0){
            return -1;
        }
        
        if(remaining == 0){
            return 0;
        }
        
        int minCount = Integer.MAX_VALUE;
        
        for(int i = 0; i < coins.length; i++){
            int count = coinChangeHelper(coins, remaining - coins[i]);
            if(count >= 0){
                //在选定当前coin[i]的情况下，计算子问题，返回的结果加上coin[i]本身，总共count + 1个coin，看和目前最小的minCount谁更小
                minCount = Math.min(count + 1, minCount);
            }
        }
        
        return minCount == Integer.MAX_VALUE ? -1 : minCount;
    }
}
```

暴力Backtracking的基础上记忆化搜索(memorization), 其实也就是top-down的dp
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        
        //若是amount本身就是0或者负数，那么直接就达到目标了，返回0即可
        if(amount < 1){
            return 0;
        }
        
        //在经过了前面的filter后，现在的amount肯定是>=1的了，而这种情况下如果没有coins可选，那么肯定没有可行方案，直接返回-1
        if(coins == null || coins.length == 0){
            return -1;
        }
        
        int[] dp = new int[amount + 1];
        //Arrays.fill(dp, -1);//注意这里不能把dp初始化成-1， -1代表是无解，而dp中的值需要代表尚未计算
        //如果把无解和尚未计算当成同一种状态，那么会引起错误
        //而dp的值==0在计算中不会出现，所以初始化成dp=0,其实初始成dp = -2也是可以的
        
        return coinChangeHelper(coins, amount, dp);
        
    }
    
    private int coinChangeHelper(int[] coins, int remaining, int[] dp){
        
        if(remaining < 0){
            return -1;
        }
        
        //这一行决定了dp[i] == 0并不会实际出现，所以我们可以使用dp[i] = 0来代表尚未计算过的状态
        if(remaining == 0){
            return 0;
        }
        
        if(dp[remaining] != 0){
            return dp[remaining];
        }
        
        int minCount = Integer.MAX_VALUE;
        
        for(int i = 0; i < coins.length; i++){
            int count = coinChangeHelper(coins, remaining - coins[i], dp);
            if(count >= 0){
                //在选定当前coin[i]的情况下，计算子问题，返回的结果加上coin[i]本身，总共count + 1个coin，看和目前最小的minCount谁更小
                minCount = Math.min(count + 1, minCount);
            }
        }
        
        //注意dp[i] == -1代表无解，而dp[i] == 0代表尚未计算，是两种不同的状态，要注意
        dp[remaining] = minCount == Integer.MAX_VALUE ? -1 : minCount;
        
        return minCount == Integer.MAX_VALUE ? -1 : minCount;
    }
}
```

bottom up DP
```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        
        if(coins == null || coins.length == 0 || amount < 0){
            return -1;
        }

        //其实换成int MAX = amount + 2或者 + 3都是可以的，因为coin假设最小的是1，所以coin的数量最多是amount，大于amount就成为一个界限
        //但是不要用int MAX = Integer.MAX_VALUE; 因为dp[i - coins[j]] + 1就会使使其溢出
        int MAX = amount + 1;

        //dp[i]表示钱数为i时的最小硬币数的找零
        int[] dp = new int[amount + 1];

        //初始化
        Arrays.fill(dp, MAX);
        dp[0] = 0;

        for(int i = 1; i <= amount; i++ ){
            for(int j = 0; j < coins.length; j++){
                if(i >= coins[j]){
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];

    }
}
```

### 笔记

本题是一道非常好的能比较DP的bottom-up和top-down两种做法的题目。

那么说，top-down的记忆化搜索都是一般改进于暴力搜索，那么暴力搜索怎么搜?

leetcode中的暴力版本没看太明白，而且也是和记忆化搜索的版本不太一致，所以不推荐。
比较直观的搜索应该就是每次，每次都对余额进行一次for循环，循环每个coin的面值，然后找出子问题中使用硬币数最少的情况，然后加上当前这枚coin，也就是coinNum + 1.

那么如果使用dp的版本，就需要提炼出关键的dp的状态:

**dp[i]表示钱数为i时的最小硬币数的找零**

那么看暴力的搜索过程可以发现，会有很多重复的计算，所以可以使用memorization进行优化，将计算过的结果cache起来。

可以看出，从暴力搜索到加入记忆化，其实**是非常容易嵌入的**

那么再比较地看看iteration的DP，对于bottom up的dp，其实最主要需要能够找到从bottom推到top的这个过程，这也是为什么我们需要DP的四要素:

* 状态:
不管是top-down还是bottom-up，状态是一样的： **dp[i]表示钱数为i时的最小硬币数的找零**

* 初始化:
1. 其他所有状态的都设为MAX，这里注意MAX的设置:
        其实换成int MAX = amount + 2或者 + 3都是可以的，因为coin假设最小的是1，所以coin的数量最多是amount，大于amount就成为一个界限,但是不要用int MAX = Integer.MAX_VALUE; 因为dp[i - coins[j]] + 1就会使使其溢出
2. dp[0] = 0, 也就是说当钱数为0时，一个硬币都不需要就能达成

* 状态转换:
对于amount和coin两个维度进行两层for循环， dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);

* 结果:
如果dp[amout]是能够从bottom的某个位置到达的，那么肯定dp[amount] <= amount，否则就是无解。

DP的时间复杂度和空间复杂度是:

Time complexity : O(S*n)O(S∗n). On each step the algorithm finds the next F(i)F(i) in nn iterations, where 1\leq i \leq S1≤i≤S. Therefore in total the iterations are S*nS∗n.
Space complexity : O(S)O(S). We use extra space for the memoization table.

具体参考:
[leetcode solution -  322. Coin Change](https://leetcode.com/problems/coin-change/solution/)
[Grandyang - [LeetCode] Coin Change 硬币找零](http://www.cnblogs.com/grandyang/p/5138186.html)