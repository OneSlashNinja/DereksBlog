---
layout: post
title:  "LeetCode 17 - Letter Combinations of a Phone Number"
date:   2017-05-26 00:15:02 -0400
categories: leetcode, Amazon
---

# Letter Combinations of a Phone Number

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
    public List<String> letterCombinations(String digits) {
        
        List<String> result = new ArrayList<String>();

        if(digits == null || digits.length() == 0){
            return result;
        }

        HashMap<Character, String> map = new HashMap<Character, String>();

        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        StringBuilder sb = new StringBuilder();

        dfs(digits, 0, map, sb, result);

        return result;
    }

    private void dfs(String digits, int currentIndex, HashMap<Character, String> map, StringBuilder sb, List<String> result){
        if(currentIndex == digits.length()){
            result.add(sb.toString());
            return;
        }

        char currentDigit = digits.charAt(currentIndex);
        String mappedChars = map.get(currentDigit);

        for(int i = 0; i < mappedChars.length(); i++){
            sb.append(mappedChars.charAt(i));
            dfs(digits, currentIndex + 1, map, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }

    }

}
```


### 笔记
