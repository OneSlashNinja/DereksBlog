---
layout: post
title:  "LeetCode 20 - Valid Parentheses"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Valid Parentheses

## 一刷

### 代码
自己的version:

```java
public class Solution {
    /**
     * @param s A string
     * @return whether the string is a valid parentheses
     */
    public boolean isValidParentheses(String s) {
        // Write your code here

        if(s == null || s.length() == 0){
        	return true;
        }

        Stack<Character> stack = new Stack<Character>();

        for(int i = 0; i < s.length(); i++){

        	char ch = s.charAt(i);
        	if(ch == '[' || ch == '{' || ch == '(' ){
        		stack.push(ch);
        		continue;
        	}

        	if(stack.size() == 0){
        		return false;
        	}

        	char topChar = stack.pop();

        	if(topChar == '[' && ch != ']'){
        		return false;
        	}
        	if(topChar == '{' && ch != '}'){
        		return false;
        	}
        	if(topChar == '(' && ch != ')'){
        		return false;
        	}
        }

        if(stack.size() == 0){
        	return true;
        }else{
        	return false;
        }
    }
}

```

### 笔记

本题自己一遍AC，连语法错误都没有，只要想到是Stack，就全明了了。引用下喜刷刷的笔记

"
括号匹配问题用stack解再合适不过。括号组合是否有效，主要看右括号。右括号的数量必须要等于相应的左括号。而左右括号之间也必须是有效的括号组合。

1. 当前括号是左括号时，压入stack。
2. 当前括号是右括号时，stack.top()如果不是对应的左括号，则为无效组合。否则，pop掉stack里的左括号。
3. 所有字符都判断处理过后，stack应为空，否则则无效。
"

---

## 二刷

### 代码

```java
public class Solution {
    public boolean isValid(String s) {
        
        if(s == null || s.length() == 0){
            return true;
        }
        
        Stack<Character> charStack = new Stack<Character>();
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(ch == '{' || ch== '(' || ch == '['){
                charStack.push(ch);
                continue;
            }
            
            if(charStack.isEmpty()){
                return false;
            }
            
            if((ch == '}' && charStack.peek() != '{') || 
                (ch == ')' && charStack.peek() != '(') ||
                (ch == ']' && charStack.peek() != '[')){
                    return false;
                }
                
            charStack.pop();
        }
        
        if(charStack.isEmpty()){
            return true;
        }else{
            return false;
        }
        //其实可以简化为return charStack.isEmpty();
        
    }
}
```

### 笔记

基本和第一个遍没有什么区别，只要明白是stack，基本就不会出错，主要就在于for循环中利用continue和return来直接跳过后面的代码，从而避免大块的if和else。

另外要注意的一点是在Java中：
Stack是Class，而Set只是Interface，具体实例化的时候需要使用HashSet作为Class。

另外，既可以使用charStack.isEmpty()，也可以使用charStack.size() > 0;