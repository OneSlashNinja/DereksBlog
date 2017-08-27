---
layout: post
title:  "leetcode 276 - Paint Fence"
date:   2017-07-23 21:57:12.742202
categories: leetcode, Google
---

# Paint Fence

## 一刷

### 代码

空间O(n), 时间O(n)的dp
```java
public class Solution {
    public int numWays(int n, int k) {
        
        if(n == 0 || k == 0){
            return 0;
        }
        
        if(n == 1){
            return k;
        }
        
        // same[i] means the ith post has the same color with the (i-1)th post.
        int[] same = new int[n];
        // diff[i] means the ith post has a different color with the (i-1)th post.
        int[] diff = new int[n];
        
        same[0] = same[1] = k;
        diff[0] = k;
        diff[1] = k * (k - 1);
        
        for(int i = 2; i < n; i++){
            same[i] = diff[i - 1];
            diff[i] = (k - 1) * (same[i - 1] + diff[i - 1]);
        }
        
        return same[n - 1] + diff[n - 1];
    }
}
```

空间O(1),时间O(n)的优化dp
```java
public class Solution {
    public int numWays(int n, int k) {
        
        if(n == 0 || k == 0){
            return 0;
        }
        
        if(n == 1){
            return k;
        }
        
        
        int same = k;
        int diff = k * (k - 1);
        
        for(int i = 2; i < n; i++){
            int temp = diff;
            diff = (k - 1) * (same + diff);
            same = temp;
        }
        
        return same + diff;
    }
}
```

### 笔记

这题和Paint House很像，却又是完全不一样的一道。

这题比起Paint House，没有了cost这个维度，问的也不是最后的花费，而是可能Paint的种类。

如果限制条件和Paint House的一样，是相邻的两个不能Paint同一个颜色，那么此题则会非常简单，完全不用dp，直接计算就可以了，除了第一个fence可以有k种选择，剩下的所有fence都有(k - 1)种选择，直接计算即可。

但是这题最关键的限制条件就在于**You have to paint all the posts such that no more than two adjacent fence posts have the same color.**

也就是说两个相邻的元素是可以Paint同一种颜色的，但是不能超过两个。

那么这就需要分情况讨论了。

最后证明这也是一道dp题，而且也是一道很不同的dp题，以前所见到的dp不管是几维的，状态一般都只有一个，而这题因为分情况，所以状态和状态转换方程有两个，但又是相互依存的两个，非常有意思。

那么就看一下这道dp的具体要素:

状态:

same[i]表示第i块post和第i - 1块post有着**相同**的颜色的所有可能性有多少种?
diff[i]表示第i块post和第i - 1块post有着**不同**的颜色的所有可能性有多少种？

状态转换方程:

same[i] = diff[i - 1];
diff[i] = (k - 1) * (same[i - 1] + diff[i - 1]);

same[i] = diff[i - 1];好理解，第i块要想和第i-1块颜色相同，那么i - 1块一定和i - 2块得颜色不同，而颜色相同又只有一种选择，所以same[i] = diff[i - 1] * 1 = diff[i - 1];

diff[i] = (k - 1) * (same[i - 1] + diff[i - 1])也就容易理解了:

因为假设第i块post和第i - 1块post不一样，所以第i - 1块post既可以和第i - 2块post一样，也可以不一样，在此基础上，对第i块post要选不一样的，有(k - 1)种选法， 所以状态转换时diff[i] = (k - 1) * (same[i - 1] + diff[i - 1])

初始化:

这题的初始化其实比较特殊，首先n == 1的情况属于特殊情况，应该单独提出来:

if(n == 1){
    return k;
}

再次因为same[i]和diff[i]表示的都是i和i - 1块板之间的关系，所以其实same[0]和diff[0]并没有什么含义，试验的话你会发现可以替换成任何值都无所谓。

而最重要的初始化，来启动装换方程的，应该是:

same[1] = k;
diff[1] = k * (k - 1);


结果:

这题的结果也是不一样，是两个状态最后之和，也就是

same[n - 1] + diff[n - 1]

---

这题其实dp的空间上会有冗余，前面计算的结果在后面就完全不会用了，所以空间上还可以继续压缩，把int[]压缩成两个int。就和爬楼梯一样。

由于same和diff是相互依存的关系，所以这里的一个关键技巧就是**使用temp来先将diff保存，然后再计算diff，最后再把temp当先前的diff用，传给same**