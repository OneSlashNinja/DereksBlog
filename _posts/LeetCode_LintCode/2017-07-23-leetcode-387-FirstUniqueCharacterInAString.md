---
layout: post
title:  "leetcode 387 - First Unique Character In A String"
date:   2017-07-23 17:35:13.420882
categories: leetcode, Amazon, Facebook, Microsoft
---

# First Unique Character In A String

## 一刷

### 代码

自己的稍微优化但是比较别扭的O(n)版本
```java
public class Solution {
    public int firstUniqChar(String s) {
        
        int[] indexs = new int[26];
        
        Arrays.fill(indexs, -1);
        
        for(int i = 0; i < s.length(); i++){
            if(indexs[s.charAt(i) - 'a'] == -1){
                indexs[s.charAt(i) - 'a'] = i;
            }else if(indexs[s.charAt(i) - 'a'] >= 0){
                indexs[s.charAt(i) - 'a'] = -2;
            }
        }
        
        int firstUniqueCharIndex = Integer.MAX_VALUE;
        
        for(int i = 0; i < indexs.length; i++){
            if(indexs[i] >= 0){
                firstUniqueCharIndex = Math.min(firstUniqueCharIndex, indexs[i]);
            }
        }
        
        return firstUniqueCharIndex == Integer.MAX_VALUE ? -1 : firstUniqueCharIndex;
    }
}
```

two pass O(n)版
```java
public class Solution {
    public int firstUniqChar(String s) {
        if(s == null || s.length() == 0){
            return -1;
        }
        
        int[] counts = new int[26];
        
        for(int i = 0; i < s.length(); i++){
            counts[s.charAt(i) - 'a']++;
        }
        
        for(int i = 0; i < s.length(); i++){
            if(counts[s.charAt(i) - 'a'] == 1){
                return i;
            }
        }
        
        return -1;
    }
}
```

### 笔记

一开始自己想得有点复杂了, 感觉应该是要使用一个int[26]的数组(题目中说只有lower case)，来表示什么，然后pass一遍string来处理这个数组，之后再通过该数组找到那个first unique character。

这时不禁想，这个int[26]的数组需要包含两个维度的信息:(1)需要知道某个char的频度 (2)还需要知道这个char的index,否则如果直接处理这个int[26],会不知道谁才是first。

那么怎么用一维的数组来表示二维的信息? 于是，机智地想到，因为频度我们只关心几种固定的种类:
(1)该char完全没出现 (2)该char出现了1次 (3)该char出现了1次以上

那么其中(1)可以用-1表示，(2)的情况正好用来表示另一个维度index，(3)用-2来表示。

于是，在第二遍扫描indexs数组的时候就可以去找:*大于等于0的数中，最小的那一个*了。

这种解法第一遍pass需要O(n),第二遍pass只需要O(26)也就是O(1);

---

但是看了别人的答案才发现: **其实不需要记录index信息，数组自己就是该信息的载体，直接第二遍pass仍然使用s来依次找就行**

所以，就非常清晰地变成了two pass:
第一个pass用来记录每个char的频度
第二个pass仍然使用s的顺序来找到第一个频度>0的数
即可。


## 二刷

lintcode上思路又绕了一毛一样的弯版，
注意这回不仅是数据集不仅是26个小写字母，而是整个ASCII集，所以就是想让这个版本正确，也需要int[256]来表示。
```java
public class Solution {
    /*
     * @param s: a string
     * @return: it's index
     */
    public int firstUniqChar(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return -1;
        }
        
        int[] uniqueIndex = new int[256];
        
        Arrays.fill(uniqueIndex, -1);
        
        char[] sChars = s.toCharArray();
        
        
        for(int i = 0; i < sChars.length; i++){
            if(uniqueIndex[sChars[i]] == -1){
                uniqueIndex[sChars[i]] = i;
            }else if(uniqueIndex[sChars[i]] > -1){
                uniqueIndex[sChars[i]] = -2;
            }
        }
        
        int result = -1;
        
        for(int i = 0; i < uniqueIndex.length; i++){
            if(uniqueIndex[i] > -1){
                if(result == -1){
                    result = uniqueIndex[i];
                    continue;
                }
                
                result = Math.min(result, uniqueIndex[i]);
            }
        }
        
        return result;
    }
}
```

又想起来做法的版本
```java
public class Solution {
    /*
     * @param s: a string
     * @return: it's index
     */
    public int firstUniqChar(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return -1;
        }
        
        int[] counts = new int[256];
        
        for(int i = 0; i < s.length(); i++){
            counts[s.charAt(i)]++;
        }
        
        for(int i = 0; i < s.length(); i++){
            if(counts[s.charAt(i)] == 1){
                return i;
            }
        }
        
        return -1;
    }
}
```

居然都忘了这题做过了，一开始的思路和上次做的时候绕的弯一模一样，想用uniqueIndex数组来表示String s中的字符出现的位置，再用特殊字符-1来代表还没出现，-2代表已经duplicate。

而其实出现的顺序已经由s本身天然地维护了，所以我们不需要几率字符出现的位置，而只需要记录字符出现的频次。而后再第二遍顺序扫一遍s，遇到的第一个counts[s.charAt(i)] == 1的就是符合要求的character。
