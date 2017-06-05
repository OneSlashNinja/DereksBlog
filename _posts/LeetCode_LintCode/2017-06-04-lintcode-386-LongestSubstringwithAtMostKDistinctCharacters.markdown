---
layout: post
title:  "Lintcode 386 - Longest Substring with At Most K Distinct Characters"
date:   2017-06-04 00:15:02 -0400
categories: lintcode, Amazon
---

# Longest Substring with At Most K Distinct Characters

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

错误版本
```java
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        
        if(s == null || s.length() == 0 || k == 0){
            return 0;
        }
        
        if(k >= s.length()){
            return s.length();
        }
        
        int left = 0, right = -1;
        int[] charCount = new int[256];
        int count = 0; // unique characters between left and right
        int maxCount = 0; //longest substring count
        
        while(right < s.length() - 1){
            if(count < k){
                right++;
                if(charCount[s.charAt(right)] == 0){
                    count++;
                }
                charCount[s.charAt(right)]++;
                maxCount = Math.max(maxCount, right - left + 1);
            }else{
                charCount[s.charAt(left)]--;
                if(charCount[s.charAt(left)] == 0){
                    count--;
                }
                left++;
            }
        }
        
        return maxCount;
    }
}
```

正确版本:

```java
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        
        if(s == null || s.length() == 0 || k == 0){
            return 0;
        }
        
        if(k >= s.length()){
            return s.length();
        }
        
        int left = 0, right = -1;
        int[] charCount = new int[256];
        int count = 0; // unique characters between left and right
        int maxCount = 0; //longest substring count
        
        while(right < s.length() - 1){
            
            if(count == k && charCount[s.charAt(right + 1)] == 0){
                charCount[s.charAt(left)]--;
                if(charCount[s.charAt(left)] == 0){
                    count--;
                }
                left++;
            }else{
                right++;
                if(charCount[s.charAt(right)] == 0){
                    count++;
                }
                charCount[s.charAt(right)]++;
                maxCount = Math.max(maxCount, right - left + 1);
            }
            
        }
        
        return maxCount;
    }
}
```

使用经典substring模板正确版本
```java
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        
        if(s == null || s.length() == 0 || k == 0){
            return 0;
        }
        
        if(k >= s.length()){
            return s.length();
        }
        
        int[] charCount = new int[256];
        int count = 0; // unique characters between left and right
        int maxCount = 0; //longest substring count
        
        for(int left = 0, right = 0; right < s.length(); right++){
            
            if(charCount[s.charAt(right)] == 0){
                count++;
            }
            charCount[s.charAt(right)]++;
            
            while(count > k){
                charCount[s.charAt(left)]--;
                if(charCount[s.charAt(left)] == 0){
                    count--;
                }
                left++;
            }
            
            maxCount = Math.max(maxCount, right - left + 1);
        }
        
        return maxCount;
    }
}
```

### 笔记

这题一开始并没有使用substring的模板方法进行解，使用了另一种只用了一个while循环的方法。但是很多地方比较tricky：

比如说第一个错误的版本：
就是因为当substring中unique的字符的长度已经到达k时，程序就会认为应该开始缩减左边的窗口了。但是其实右边的窗口的下一个字符很有可能还是重复的字符。所以需要额外的判断，于是写出了第二个版本的正确版本。

但是这种只用了一个while的版本会发现，初始的left和right的位置，while中的条件也很奇怪是right < s.length() - 1，并且到底该移动哪一边，什么时候移动，以及在已经达到k个不同字符时的处理怎么样都会比较难记。


而使用了经典的substring的模板后，因为right每次都要固定挪动一位，left则相应地利用while调整位置，更加直观和便于理解。