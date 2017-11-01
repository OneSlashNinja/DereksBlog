---
layout: post
title:  "leetcode 151 - Reverse Words In a String"
date:   2017-10-12 21:15:01.746444
categories: leetcode, Bloomberg
---

# Reverse Words In a String

## 一刷

### 代码

自己的版本:
```java
public class Solution {
    
    public String reverseWords(String s) {
        //不用写s = s.trim();下面的程序会自动处理leading和trailing的空格
        
        Stack<String> wordsStack = new Stack<String>();
        
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == ' '){
                if(sb.length() != 0){
                    wordsStack.push(sb.toString());
                    //注意clear一个StringBuilder的方法就是sb.setLength(0);
                    sb.setLength(0);
                }
            }else{
                sb.append(s.charAt(i));
            }
        }
        
        //注意最后一个word的后面很可能不会再带一个' '，所以在跳出了for循环后需要再单独判断一次
        if(sb.length() != 0){
            wordsStack.push(sb.toString());
        }
        
        StringBuilder resultBuilder = new StringBuilder();
        
        while(!wordsStack.isEmpty()){
            resultBuilder.append(wordsStack.pop());
            
            //这里比较巧妙地可以使得每个word的结尾都能加上' '
            if(!wordsStack.isEmpty()){
                resultBuilder.append(' ');
            }
        }
        
        return resultBuilder.toString();
    }
    
    
}
```

leetcode中不使用trim, split, StringBuilder的三步翻转法
```java
public class Solution {
  
  public String reverseWords(String s) {
    if (s == null) return null;
    
    char[] a = s.toCharArray();
    int n = a.length;
    
    // step 1. reverse the whole string
    reverse(a, 0, n - 1);
    // step 2. reverse each word
    reverseWords(a, n);
    // step 3. clean up spaces
    return cleanSpaces(a, n);
  }
  
  void reverseWords(char[] a, int n) {
    int i = 0, j = 0;
      
    while (i < n) {
      //i < j 的作用是让i先追上j,因为j之前的部分都是已经处理了的，后面的i < n && a[i] == ' '才是让i跳到下一个word的起始位置
      while (i < j || i < n && a[i] == ' ') i++; // skip spaces

      //j < i是让j先追上i，因为i之前已经是处理过了的，后面的j < n && a[j] != ' '是让j停留在下一个word的结束位置的后一格，也就是空格
      while (j < i || j < n && a[j] != ' ') j++; // skip non spaces

      reverse(a, i, j - 1);                      // reverse the word
    }
  }
  
  // trim leading, trailing and multiple spaces
  String cleanSpaces(char[] a, int n) {
    int i = 0, j = 0;
    
    //快慢指针，j为快指针，用来扫描整个a，i为慢指针，用来圈地，表示最后实际应该返回的String。
    //因为j走的肯定比i快，所以改变i所在位置的char并不会影响到j位置的判断
    while (j < n) {
      while (j < n && a[j] == ' ') j++;             // skip spaces
      while (j < n && a[j] != ' ') a[i++] = a[j++]; // keep non spaces
      while (j < n && a[j] == ' ') j++;             // skip spaces， 注意这一行和第一行完全一样
      if (j < n) a[i++] = ' ';                      // keep only one space
    }
  
    return new String(a).substring(0, i);
  }
  
  // reverse a[] from a[i] to a[j]
  private void reverse(char[] a, int i, int j) {
    while (i < j) {
      char t = a[i];
      a[i++] = a[j];
      a[j--] = t;
    }
  }
  
}
```

### 笔记

这题不知道为什么踩的人比顶的人多大概5倍？

自己写的版本较为简单，不过需要使用Stack配合StringBuilder。

基本思路就是：使用StringBuilder作为一个String的暂时容器，然后从左向右扫描整个String，如果碰到空格，则看当前StringBuilder中有没有实际的字符串，如果有，则作为一个String压入Stack中。

注意最后循环结束后仍需要检测StringBuilder是否为空。

之后就pop整个stack，然后组合起来便是倒过来的顺序。


而如果指定，不能够使用trim(), split(), 和StringBuilder呢？

那么可以使用**two pointer + 像之前rotate string中的三步翻转法**

大致思路就是:
1. 先翻转整个string
2. 再将每个word翻转
3. 去除头尾和中间额外的空格

