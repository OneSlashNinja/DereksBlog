---
layout: post
title:  "leetcode 244 - ShortestWordDistance3"
date:   2017-07-18 23:22:36.290730
categories: leetcode, Linkedin
---

# ShortestWordDistance3

## 一刷

### 代码

自己写的版本
```java
public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        
        if(words == null || words.length == 0 || word1 == null || word2 == null){
            return -1;
        }
        
        int lastMatchIndex = -1;
        int shortest = Integer.MAX_VALUE;
        
        boolean areSameWord = word1.equals(word2);
        
        for(int i = 0; i < words.length; i++){
            if(areSameWord){
                if(word1.equals(words[i])){
                    if(lastMatchIndex >= 0){
                        shortest = Math.min(shortest, Math.abs(i - lastMatchIndex));
                    }
                    lastMatchIndex = i;
                }
            }else{
                if(words[i].equals(word1)){
                    if(lastMatchIndex >= 0 && words[lastMatchIndex].equals(word2)){
                        shortest = Math.min(shortest, Math.abs(i - lastMatchIndex));
                    }
                    lastMatchIndex = i;
                }else if(words[i].equals(word2)){
                    if(lastMatchIndex >= 0 && words[lastMatchIndex].equals(word1)){
                        shortest = Math.min(shortest, Math.abs(i - lastMatchIndex));
                    }
                    lastMatchIndex = i;
                }
                
            }
        }
        
        return shortest;
    }
}
```

简化版本
```java
public class Solution {
        public int shortestWordDistance(String[] words, String word1, String word2) {
            int index = -1;
            int min = words.length;
            for (int i = 0; i < words.length; i++) {
                if (words[i].equals(word1) || words[i].equals(word2)) {
                    if (index != -1 && (word1.equals(word2) || !words[index].equals(words[i]))) {
                        min = Math.min(i - index, min);
                    }
                    index = i;
                }
            }
            return min;
        }
    }
```

### 笔记

相当于是Shortest Word Distance的另一种follow up。如果word1和word2相等的话，则需要找list中两个位置不同的但是最近的word。

自己的思路是对的，感觉可以利用Shortest Word Distance 1题解中提到的只是用一个index变量来表示上一个match的word的位置，然后根据是不是word1和word2是同一个word来进行区分。

写出了第一个版本，不过发现其实有蛮多的地方可以合并，leetcode上的简化版本其实也是同样的思路。

[leetcode Shortest Word Distance III discuss](https://discuss.leetcode.com/topic/29963/short-java-solution-10-lines-o-n-modified-from-shortest-word-distance-i)
