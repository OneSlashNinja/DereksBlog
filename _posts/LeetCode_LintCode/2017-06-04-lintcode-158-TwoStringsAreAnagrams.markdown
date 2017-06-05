---
layout: post
title:  "LeetCode 158 - Two Strings Are Anagrams"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Two Strings Are Anagrams

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

排序
```java
public class Solution {
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    public boolean anagram(String s, String t) {
        // write your code here
        
        if(s == null || t == null){
            return false;
        }

        //做一个剪枝pruning
        if(s.length() != t.length()){
            return false;
        }
        
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        
        return (new String(sChars)).equals(new String(tChars));
        
    }
};
```

计数排序
```java
public class Solution {
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    public boolean anagram(String s, String t) {
        // write your code here
        
        if(s == null || t == null){
            return false;
        }
        
        //pruning
        if(s.length() != t.length()){
            return false;
        }
        
        int[] sMap = new int[256];
        int[] tMap = new int[256];
        
        for(int i = 0; i < s.length(); i++){
            sMap[s.charAt(i)]++;
        }
        
        for(int i = 0; i < t.length(); i++){
            tMap[t.charAt(i)]++;
        }
        
        for(int i = 0; i < 256; i++){
            if(sMap[i] != tMap[i]){
                return false;
            }
        }
        
        return true;
    }
};
```


### 笔记

这种对于两个String的anagram的比较，主要就是排序和使用"计数排序"。

假设字符串的长度为n(如果字符串长度不相等，那么肯定不是anagram，可以直接被当成剪枝条件了),排序的话则时间复杂度是O(nlogn),计数排序只统计每个字符的出现频次则只需要O(n)的时间复杂度。

对于多个字符串的anagram，也可以使用计数排序的方法，把计数排序统计的结果转换成一个相应的字符串，相当于计算一个hashcode。具体过程参考**anagrams**那题的笔记。