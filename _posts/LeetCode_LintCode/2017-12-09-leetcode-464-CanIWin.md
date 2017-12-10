---
layout: post
title:  "leetcode 464 - Can I Win"
date:   2017-12-09 23:05:12.380330
categories: leetcode, Linkedin, Microsoft
---

# Can I Win

## 一刷

### 代码

暴力backtracking的版本
```java
class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        
        //因为数列是有规律的从1...maxChoosableInteger的数列，所以可以直接使用等差数列求和在O(1)时间算出sum，而不需要遍历一遍
        //等差数列求和(a1 + an) * n / 2
        int sum = (maxChoosableInteger + 1) * maxChoosableInteger / 2;
        
        //如果所有数的和都比desiredTotal小，那么没人能赢
        if(sum < desiredTotal){
            return false;
        }
        
        //这种情况下，只要有可选的数，那么直接就赢了
        if(desiredTotal <= 0){
            return true;
        }
        
        //这里其实长度maxChoosableInteger就够用了，但是为了方便下标和数字直接对应，就多占一位
        boolean[] isUsed = new boolean[maxChoosableInteger + 1];
        
        return canIWinHelper(isUsed, desiredTotal);
        
    }
    
    private boolean canIWinHelper(boolean[] isUsed, int remainTotal){
        
        for(int i = 1; i <= isUsed.length - 1; i++){
            
            //如果已经使用过了，就不能深入进行搜索了，这行不要忘
            if(isUsed[i]){
                continue;
            }
            
            isUsed[i] = true;
            //一定要明白，这里递归调用就攻守变换，变到对手的先手局面了，所以是"CanOpponentWin"
            boolean canOpponentWin = canIWinHelper(isUsed, remainTotal - i);
            //因为是Backtracking，所以不能忘了这一行
            isUsed[i] = false;
            
            //如果此时已经有拿某一个没用过的数就赢的情况，那么肯定是先手必胜状态
            //如果如果能知道使用i后的局面对于对手是先手必败状态，那么也可以确定自己的状态是先手必胜
            if(remainTotal - i <= 0 || !canOpponentWin){
                return true;
            }
        }
        
        //能走到这里，说明当前局面下，所有转移到该状态的状态都是对手先手必胜，那么这就是个先手必败状态
        return false;
    }
    
}
```

使用memorization优化的版本
```java
class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        
        //因为数列是有规律的从1...maxChoosableInteger的数列，所以可以直接使用等差数列求和在O(1)时间算出sum，而不需要遍历一遍
        //等差数列求和(a1 + an) * n / 2
        int sum = (maxChoosableInteger + 1) * maxChoosableInteger / 2;
        
        //如果所有数的和都比desiredTotal小，那么没人能赢
        if(sum < desiredTotal){
            return false;
        }
        
        //这种情况下，只要有可选的数，那么直接就赢了
        if(desiredTotal <= 0){
            return true;
        }
        
        //这里其实长度maxChoosableInteger就够用了，但是为了方便下标和数字直接对应，就多占一位
        boolean[] isUsed = new boolean[maxChoosableInteger + 1];
        HashMap<Integer, Boolean> map = new HashMap<>();//注意是Boolean而不是boolean, 这里需要class类型
        
        return canIWinHelper(isUsed, map, desiredTotal);
        
    }
    
    private boolean canIWinHelper(boolean[] isUsed, HashMap<Integer, Boolean> map, int remainTotal){
        //这里先进性判断会很confusing(返回的是false而不是true)，放在循环中直接测试会比较好
        // if(remainTotal <= 0){
        //     return false;
        // }
        
        int key = booleanArrToInt(isUsed);
        
        //如果已经计算过了，则不需要重复计算，直接返回之前计算的结果即可，memorization省时间的关键
        if(map.containsKey(key)){
            return map.get(key);
        }
        
        //否则，需要完全地backtracking所有没有used的情况，注意是backtracking而不是dfs
        for(int i = 1; i <= isUsed.length - 1; i++){//注意这里也是为了方便计算，使得i处于1...maxChoosableInteger而不是0...maxChoosableInteger-1
            
            //如果已经使用过了，就不能深入进行搜索了，这行不要忘
            if(isUsed[i]){
                continue;
            }
            
            isUsed[i] = true;
            //一定要明白，这里递归调用就攻守变换，变到对手的先手局面了，所以是"CanOpponentWin"
            boolean canOpponentWin = canIWinHelper(isUsed, map, remainTotal - i);
            
            //如果此时已经有拿一个没用过的数就赢的情况，那么肯定是先手必胜状态
            //如果如果能知道使用i后的局面对于对手是先手必败状态，那么也可以确定自己的状态是先手必胜
            if(remainTotal - i <= 0 || !canOpponentWin){
                map.put(key, true);//注意这里是map.put(key, true);而不是map.put(booleanArrToInt(isUsed), true);因为此时的isUsed表示的是子状态
                isUsed[i] = false;//因为是Backtracking，所以不能忘了这一行，而这一行需要写在map记录完当前状态后，所以本题回溯的位置需要分开写
                return true;
            }
            isUsed[i] = false;//因为是Backtracking，所以不能忘了这一行，而这一行需要写在map记录完当前状态后，所以本题回溯的位置需要分开写
        }
        
        //当前局面下，所有转移到该状态的状态都是对手先手必胜，那么这是个先手必败状态
        map.put(key, false);
        return false;
    }
    
    //isUsed的长度不能超过32，这也是为什么题目中说maxChoosableInteger will not be larger than 20
    //利用bit operation来进行转换，非常巧妙
    private int booleanArrToInt(boolean[] isUsed){
        int result = 0;
        for(int i = 0; i < isUsed.length; i++){
            if(isUsed[i]){
                result += 1;
            }
            
            result = result << 1;
        }
        
        return result;
    }
}
```

### 笔记

个人感觉这题的难度绝对是不止medium的，绝对应该是Hard级别的。

不仅需要**博弈论**的知识，还需要**memorization**的知识，甚至还运用了一些**bit operation**的知识。

也对应了本题的三个level:

1. weak hire: 能运用博弈论的知识写出可行解，也就是暴力搜索。

2. hire: 能在暴力的基础上想到memorization

3. strong hire: 能够使用bit operation来将状态压缩为一个int


本题属于bottom-up的DP似乎没有找到有效的解法，所以需要使用memorization来进行Top-down的DP的题目。

首先看第一个level: 使用博弈论知识暴力搜索

    leetcode对于该题的其中一个标签就是Minmax，个人感觉Minmax说的其实就是零和博弈中的核心思想: 最小化对手的利益来最大化自己的利益。

    而其中核心的概念(具体见自己博弈论总结)就是:

    ```
    * 一个状态是先手必胜状态当且仅当可以转移到它的状态(也就是自己下完该对手先手的状态)中**存在一个**先手必败状态
    * 一个状态是先手必败状态当且仅当可以转移到它的状态中**都是**先手必胜状态
    * 所有状态要么是先手必胜，要么是先手必败，没有中间态。
    * 先手后手是对于局面来说的，一个人在不同的局面下先手后手会转换
    ```

    其中，要明白的非常重要的一点是:
    对于backtracking的过程，**如果当前层分析的是自己的状态，那么再深入递归得到的是下一步对手的状态，而不是下一步自己的状态**，相当于没下完一步，就攻守转换了，这一点一定要非常重要。

    并且，需要借助isUsed这个相当于visited的数组来看某个数是否已经被取过了。

那么，再来看第二个和第三个level:

那么，在暴力搜索的基础上，如何进行进一步的优化？答案是使用记忆化(memorization)来减少重复计算。

**那么作为dp，我们需要搞清楚状态到底是什么，或者说，使用memorization，要记住的到底是什么值。这样我们才能复用这个记忆。**

对于本题，dp状态的维度相当于是maxChoosableInteger维的，也就是说，

dp[1][2]...[maxChoosableInteger - 1][maxChoosableInteger]
表示的是当各个数字处于使用，或者尚未被使用的某种状态下，是否能够先手必胜

这也是为什么这题的记忆化不同于像“Coin change”和“Longest Increasing Path in a Matrix”，使用一个int[]就可以表示了。这两题中的dp的变量是1维的，而该题中的状态的变量是maxChoosableInteger维的。

不过，由于这maxChoosableInteger维是相互独立的，所以每一个维度的Boolean都可以使用一个bit来表示，这样我们就可以把他们压缩成一个int。这样一个int就能uniquely地表示某一种isUsed的状态。然后使用HashMap进行cache就可以。

注意如何使用bit operation来进行转换。

其他注意点:
1. 本题一开始可以剪枝pruning: 也就是当从1...maxChoosableInteger之和如果都不能大于等于total的话，那么相当于没人能赢，直接返回false即可。
而1...maxChoosableInteger是一个增量为1的递增序列，所以直接使用等差数列求和公式就可以直接得出结果，而不需要使用for循环

2. 题目中说maxChoosableInteger是有原因的，如果我们想要把isUsed转换成一个int的话，那么isUsed的长度就不能超过int的位数，也就是32。

参考:

[知乎 - 极大极小算法有些不明白 ?](https://www.zhihu.com/question/27221568)

使用bit operation来将boolean[]转换为int很有启发性，但是`if(desiredTotal <= 0) return false;`这一行的写法有瑕疵，还是每日一题中的写法比较make sense
[leetcode - Java solution using HashMap with detailed explanation](https://discuss.leetcode.com/topic/68896/java-solution-using-hashmap-with-detailed-explanation)

讲得比较全面
[九章 - Microsoft 面试题 | 我能赢](https://mp.weixin.qq.com/s/EGMed1FDnpPYLhOGRM5ydA)

讲的不错，但是对于isUsed标识，其实可以使用int来代替String
[【每日一题：小Fu讲解】LeetCode 464. Can I Win](https://www.youtube.com/watch?v=md3qQ-5B0aU)