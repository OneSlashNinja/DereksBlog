---
layout: post
title:  "leetcode 254 - Factor Combinations"
date:   2017-07-19 23:04:37.303533
categories: leetcode, Linkedin, Uber
---

# Factor Combinations

## 一刷

### 代码

```java
public class Solution {
    public List<List<Integer>> getFactors(int n) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<Integer> currentList = new ArrayList<Integer>();
        
        dfsHelper(n, 2, currentList, results);
        
        return results;
    }
    
    //如果没有start，则会有重复的组合出现
    private void dfsHelper(int n, int start, List<Integer> currentList, List<List<Integer>> results){
        //not n == 0
        if(n == 1){
            if(currentList.size() > 1){
                results.add(new ArrayList<Integer>(currentList));
            }
            return;
        }
        
        //一定要注意这里是i <= n, 直觉上会觉得题目中要求了"Factors should be greater than 1 and less than n."
        //就应该是i < n, 但实际上如果使用i < n则最后完全结不了尾，因为最后一个数肯定是以除以自己为结尾的
        //至于为了满足"Factors should be greater than 1 and less than n."， 可以交给上面的if处理
        for(int i = start; i <= n; i++){
            if(n % i == 0){
                currentList.add(i);
                dfsHelper(n / i, i, currentList, results);
                currentList.remove(currentList.size() - 1);
            }
        }
    }
}
```

### 笔记

这一题大体的思路自己是都想到了:

一看到“return all possible combinations”就基本可以断定可以用Backtracking了。

然后大体的结构写对了，但是出了几个问题，导致程序最后结果不对:

(1) 粗心的一点: 把Backtracking的触底条件写成了n == 0，但实际上最后被完全除掉以后应该是 n == 1才对。

(2) 非常重要的第一点，for循环中的终止条件必须是 i <= n,既不能是i < n, 更不能是 i < n / 2

介于 n / 2到n之间的数不能整除n没错，条件中要求了"Factors should be greater than 1 and less than n."也没错，但是如果手动地去画图你就会发现，必须条件是i <= n才能最后收尾，因为最后一个数肯定需要除以自己然后收尾。

而为了满足"Factors should be greater than 1 and less than n."， 我们可以在一开始的触底判断中加入`currentList.size() > 1`的条件就可以筛出掉n自己。

(3) 关于去处重复，将排列变组合的关键点就是加入start这个变量，使得下一层的时候从上一层断掉的地方开始，而不是从头开始，而且这样还会使得组合的顺序是有序的。否则就会出现同样的组合但是不同的排列。


