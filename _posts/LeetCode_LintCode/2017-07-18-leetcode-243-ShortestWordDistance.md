---
layout: post
title:  "leetcode 243 - Shortest Word Distance"
date:   2017-07-18 21:36:31.522165
categories: leetcode, Linkedin
---

# Shortest Word Distance

## 一刷

### 代码

O(n)的版本
```java
public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        
        int word1Index = -1;
        int word2Index = -1;
        
        int shortestDist = Integer.MAX_VALUE;
        
        for(int i = 0; i < words.length; i++){
            
            if(words[i].equals(word1)){
                word1Index = i;
                if(word2Index >= 0){
                    shortestDist = Math.min(shortestDist, Math.abs(word1Index - word2Index));
                }
            }else if(words[i].equals(word2)){
                word2Index = i;
                if(word1Index >= 0){
                    shortestDist = Math.min(shortestDist, Math.abs(word1Index - word2Index));
                }
            }
            
        }
        
        return shortestDist;
        
    }
}
```

### 笔记

这一题一开始不太明白，觉得找到word1然后再找到Word2直接一算不就行了，然后发现某一个word是可以出现多次的，所以需要计算最短的路径。

最暴力的算法肯定就是使用双重for枚举所有的组合，时间复杂度O(n^2)

但其实你会发现这也是一道完全可以**利用扫描过程**的题目，在扫描的过程中，不仅找word1，也找word2.这样的话找到其中一个，就可以和上次找到的另一个进行比较，而最短的距离肯定就在这些距离中的某一个。

其实还可以进一步优化，从使用两个临时变量变为使用一个临时变量。但是意义其实不大，并没有优化太多(但是后来发现对于解follow up3有着非常重要的意义)

> 我们还可以进一步优化上面的算法，只用一个辅助变量idx，初始化为-1，然后遍历数组，如果遇到等于两个单词中的任意一个的单词，我们在看idx是否为-1，若不为-1，且指向的单词和当前遍历到的单词不同，我们更新结果

[Leetcode Shortest Word Distance Solution](https://leetcode.com/problems/shortest-word-distance/#/solution)
[Shortest Word Distance 最短单词距离](http://www.cnblogs.com/grandyang/p/5187041.html)
