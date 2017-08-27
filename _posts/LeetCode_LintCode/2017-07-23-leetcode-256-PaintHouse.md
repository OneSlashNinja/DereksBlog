---
layout: post
title:  "leetcode 256 - Paint House"
date:   2017-07-23 20:41:15.203293
categories: leetcode, Linkedin
---

# Paint House

## 一刷

### 代码

最直观版dp
```java
public class Solution {
    public int minCost(int[][] costs) {
        
        if(costs == null || costs.length == 0 || costs[0].length != 3){
            return 0;
        }
        
        int[][] dp = new int[costs.length][costs[0].length];
        
        for(int i = 0; i < costs[0].length; i++){
            dp[0][i] = costs[0][i];
        }
        
        for(int i = 1; i < costs.length; i++){
            dp[i][0] = costs[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = costs[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
            dp[i][2] = costs[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
        }
        
        return Math.min(dp[costs.length - 1][0], Math.min(dp[costs.length - 1][1], dp[costs.length - 1][2]));
        
    }
}
```

### 笔记

”Find minimum cost to paint all houses“，基本上可以肯定是DP，那么整个DP的要素是什么呢?

状态:
首先说因为有二维信息:哪个房子和什么颜色，所以dp的状态也需要对应的是这二维的

dp[i][j]表示第i + 1个房子被涂成j颜色所需要的最小花费

状态转换方程:

dp[i][j] = costs[i][j] + Math.min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]);

初始化:
dp[0][i] = costs[0][i];

结果:
dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]中的最小值

具体见GrandYang的题解
[[LeetCode] Paint House 粉刷房子](http://www.cnblogs.com/grandyang/p/5319384.html)
