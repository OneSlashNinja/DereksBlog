---
layout: post
title:  "leetcode 205 - Isomorphic Strings"
date:   2017-07-22 22:38:57.262851
categories: leetcode, Linkedin
---

# Isomorphic Strings

## 一刷

### 代码

双HashMap的版本
```java
public class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        if(s == null || t == null || s.length() != t.length()){
            return false;
        }

        HashMap<Character, Character> stot = new HashMap<>();
        HashMap<Character, Character> ttos = new HashMap<>();

        int len = s.length();

        for(int i = 0; i < len; i++){
            if(!stot.containsKey(s.charAt(i))){
                stot.put(s.charAt(i), t.charAt(i));
            }else if(stot.get(s.charAt(i)) != t.charAt(i)){
                return false;
            }

            if(!ttos.containsKey(t.charAt(i))){
                ttos.put(t.charAt(i), s.charAt(i));
            }else if(ttos.get(t.charAt(i)) != s.charAt(i)){
                return false;
            }
        }

        return true;

    }
}
```

### 笔记

第一遍写的时候忽略了一一对应的条件，只记录了单向的mapping，所以出错了。

所以这题一定要注意**字母之间的对应是一一对应的，所以需要两个map来记录两个方向的对应，验证的时候也需要比较两个方向**

第二种方法写起来更简单，并且使用了int[]来取代HashMap，关键思路就是,记录上一次字符出现的位置，如果s和t中同一个位置的两个字符对应的上一次出现的位置不一样，那么说明不是一一对应关系。

