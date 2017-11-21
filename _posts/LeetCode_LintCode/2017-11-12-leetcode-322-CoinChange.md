---
layout: post
title:  "leetcode 322 - Coin Change"
date:   2017-11-12 19:23:38.687147
categories: leetcode, Bloomberg
---

# Coin Change

## 一刷

### 代码

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

这题的brute force是可以使用Backtracking来做的，但是时间复杂度会奇高，这个方案相当于可行解。

DP的时间复杂度和空间复杂度是:

Time complexity : O(S*n)O(S∗n). On each step the algorithm finds the next F(i)F(i) in nn iterations, where 1\leq i \leq S1≤i≤S. Therefore in total the iterations are S*nS∗n.
Space complexity : O(S)O(S). We use extra space for the memoization table.