---
layout: post
title:  "LeetCode 5 - Longest Palindromic Substring"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Longest Palindromic Substring

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

Brute Force
```java
public class Solution {
    public String longestPalindrome(String s) {
        if(s == null){
            return null;
        }

        int longestPalindromeLen = 0;
        int longestPalindromeIndex = 0;

        for(int i = 0; i < s.length(); i++){
            for(int j = i; j < s.length(); j++){
                if(isPalindrome(s, i, j) && (j - i + 1) > longestPalindromeLen){
                    longestPalindromeLen = (j - i + 1);
                    longestPalindromeIndex = i;
                }
            }
        }

        return s.substring(longestPalindromeIndex, longestPalindromeIndex + longestPalindromeLen);

    }

    private boolean isPalindrome(String s, int leftIndex, int rightIndex){
        while(leftIndex < rightIndex){
            if(s.charAt(leftIndex) == s.charAt(rightIndex)){
                leftIndex++;
                rightIndex--;
            }else{
                return false;
            }
        }

        return true;
    }
}
```

DP解法
```java
public class Solution {
    public String longestPalindrome(String s) {
        if(s == null){
            return null;
        }

        int startIndex = -1;
        int longestPalindromeLen = 0;

        boolean[][] dp = new int[s.length()][s.length()];

        //i is the length of the string
        for(int i = 0; i < s.length(); i++){
            //j is the start index of the string
            for(int j = 0; j < s.length - i; j++){
                if(i == 0){
                    dp[i][i + j] = true;
                }
            }
        }
    }
}
```

center-spread version:
```java
public class Solution {

    private int startIndex = -1;
    private int longestPalindromeLen = 0;

    public String longestPalindrome(String s) {

        if(s == null){
            return null;
        }

        for(int i = 0; i < s.length(); i++){
            longestSpreadPalindrome(s, i, 0);
            longestSpreadPalindrome(s, i, 1);
        }

        return s.substring(startIndex, startIndex + longestPalindromeLen);

    }

    private void longestSpreadPalindrome(String s, int centerIndex, int offset){
        int left = centerIndex, right = centerIndex + offset;
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }

        //此时的left和right一定是不相等的，所以搜需要缩一层
        //所以其实是长度其实是(right - 1) - (left + 1) + 1
        if(right - left - 1 > longestPalindromeLen){
            longestPalindromeLen = right - left - 1;
            startIndex = left + 1;
        }

    }
}
```

### 笔记

Brute force解法:
注意时间复杂度是O(n^3)
注意Java的字符串截取是substring(startIndex, endIndex). 左闭右开，并且substring中的string没有首字母大写。
Brute force的解法会超时


Center Spread解法:
(1)比较巧妙的一点是利用offset就解决了分情况讨论中心到底是以一个元素展开还是两个元素展开的问题。
(2)需要注意的一点是在longestSpreadPalindrome中，当跳出while循环后，可以肯定的是此时的left和right所处的元素是不一样的，所以需要算left+1到right-1这段。
(3)根据(2),其实当offset为1时，如果初始的left和right就不相等，那么left和right元素再"一缩",其实会出现left甚至在right之后的情况，这不过这种情况会因为和全局变量longestPalindromeLen比较而被屏蔽掉，否则可能会有溢出的问题。
(4)写之前感觉全局变量可以避免，比如longestSpreadPalindrome的返回值改成String或者专门再设一个Class，其中包含startIndex和longestLen这样的信息。但是发现似乎因为(3)中说的原因，还真不能去除。而且如果去除的话，空间的使用也会增加。这可能也是该方法比DP的空间效率高所需要付出的代价。