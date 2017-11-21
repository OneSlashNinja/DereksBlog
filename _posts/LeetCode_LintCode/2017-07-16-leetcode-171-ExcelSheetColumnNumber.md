---
layout: post
title:  "LeetCode 171 - Excel Sheet Column Number"
date:   2017-07-16 00:15:02 -0400
categories: leetcode, Microsoft
---

# Excel Sheet Column Number

## 一刷

### 代码

```java
public class Solution {
    public int titleToNumber(String s) {
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        char[] charArr = s.toCharArray();
        
        int colNum = 0;
        
        for(int i = 0; i < charArr.length; i++){
            colNum *= 26;
            colNum += charArr[i] - 'A' + 1;
        }
        
        return colNum;
    }
}
```

### 笔记

这题还真是没啥好说的，基本就是简单的进制转换。注意利用从左到右是从大位到小位然后乘以进制的方法来转换。

要注意为什么+1.这里比较好理解，但是对于"Excel Sheet Column Number"题目中的反向转换则会很迷惑。