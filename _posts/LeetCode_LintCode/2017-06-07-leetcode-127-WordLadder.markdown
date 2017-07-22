---
layout: post
title:  "LeetCode 127 - Word Ladder"
date:   2017-06-07 00:15:02 -0400
categories: leetcode, Amazon
---

# Word Ladder

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

```java
public class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
        if(beginWord == null || endWord == null || beginWord.length() != endWord.length()){
            return 0;
        }
        
        Set<String> wordSet = new HashSet<String>();
        for(String word : wordList){
            if(word.length() == beginWord.length()){
                wordSet.add(word);
            }
        }
        
        Queue<String> wordQueue = new LinkedList<String>();
        
        Set<String> visited = new HashSet<String>();
        
        wordQueue.offer(beginWord);
        visited.add(beginWord);
        
        int shortestTransform = 1;
        
        while(!wordQueue.isEmpty()){
            
            int currentSize = wordQueue.size();
            shortestTransform++;
            
            for(int i = 0; i < currentSize; i++){
                String polledWord = wordQueue.poll();
                for(int j = 0; j < polledWord.length(); j++){
                    for(int k = 0; k < 26; k++){
                        if(polledWord.charAt(j) == ('a' + k)){
                            continue;
                        }
                        
                        char[] polledWordCharArr = polledWord.toCharArray();
                        polledWordCharArr[j] = (char)('a' + k);
                        String newStr = new String(polledWordCharArr);
                        
                        if(wordSet.contains(newStr) && !visited.contains(newStr)){
                            if(newStr.equals(endWord)){
                                return shortestTransform;
                            }
                            
                            visited.add(newStr);
                            wordQueue.offer(newStr);
                        }
                    }
                }
            }
            
        }
        
        return 0;
        
    }
    
}
```


### 笔记
