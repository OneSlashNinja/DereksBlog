---
layout: post
title:  "LeetCode 139 - Word Break"
date:   2017-06-06 00:15:02 -0400
categories: leetcode, Amazon
---

# Word Break

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

直接版
```java
public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        Set<String> wordSet = new HashSet<String>();
        for(String word : wordDict){
            wordSet.add(word);
        }
        
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        for(int i = 1; i <= s.length(); i++){
            for(int j = 0; j < i; j++){
                if(dp[j] && wordSet.contains(s.substring(j,i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
}
```

剪枝版(leetcode上击败了98%人的submit):
```java
public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        
        if(s == null){
            return false;
        }
        
        Set<String> dict = new HashSet<String>();
        for(String word : wordDict){
            dict.add(word);
        }
        
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        int maxDictLength = maxWordLengthInDict(dict);
        
        //注意是从1开始的
        for(int i = 1; i <= s.length(); i++){
            //注意要剪枝j需要从后往前走
            for(int j = i - 1; j >= 0 && i- j <= maxDictLength; j--){
                if(dp[j] && dict.contains(s.substring(j,i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
    
    private int maxWordLengthInDict(Set<String> dict){
        int maxLen = 0;
        for(String word : dict){
            maxLen = Math.max(maxLen, word.length());
        }
        return maxLen;
    }
}
```

### 笔记
