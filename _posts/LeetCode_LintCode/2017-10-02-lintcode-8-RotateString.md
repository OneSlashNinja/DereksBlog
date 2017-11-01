---
layout: post
title:  "lintcode 8 - Rotate String"
date:   2017-10-02 23:49:00.717375
categories: lintcode, Microsoft
---

# Rotate String

## 一刷

### 代码

```java
public class Solution {
    /*
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        
        if(str == null || str.length == 0){
            return;
        }
        
        offset = offset % str.length;
        
        reverse(str, 0, str.length - offset - 1);
        reverse(str, str.length - offset, str.length - 1);
        reverse(str, 0, str.length - 1);
        
    }
    
    private void reverse(char[] str, int start, int end){
        
        while(start < end){
            char ch = str[start];
            str[start] = str[end];
            str[end] = ch;
            start++;
            end--;
        }
        
    }
}
```

### 笔记

一开始没弄明白这题跟rotate有啥关系。

三步翻转法