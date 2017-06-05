---
layout: post
title:  "LeetCode 655 - Big Integer Addition"
date:   2017-06-04 00:15:02 -0400
categories: lintcode, Amazon
---

# Big Integer Addition

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

没有考虑到题目中强调的**"Big"**而强行将String转int，相加后再转String的版本 
```java
public class Solution {
    /**
     * @param num1 a non-negative integers
     * @param num2 a non-negative integers
     * @return return sum of num1 and num2
     */
    public String addStrings(String num1, String num2) {
        // Write your code here
        
        if(num1 == null || num2 == null){
            return "";
        }
        
        long numInt1 = atoi(num1);
        long numInt2 = atoi(num2);
        
        return itoa(numInt1 + numInt2);
        
    }
    
    
    private long atoi(String str){
        long result = 0;
        
        for(int i = 0; i < str.length(); i++){
            result = result * 10 + (str.charAt(i) - '0');
        }
        
        return result;
    }
    
    private String itoa(long num){
        
        if(num == 0){
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        
        Stack<Character> stack = new Stack<Character>();
        
        while(num > 0){
            stack.push((char)(num % 10 + '0'));
            num = num / 10;
        }
        
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }
        
        return sb.toString();
        
    }
}

```

三个Stack版本
```java
public class Solution {
    /**
     * @param num1 a non-negative integers
     * @param num2 a non-negative integers
     * @return return sum of num1 and num2
     */
    public String addStrings(String num1, String num2) {
        // Write your code here
        
        if(num1 == null || num2 == null){
            return "";
        }
        
        Stack<Character> num1Digits = new Stack<Character>();
        Stack<Character> num2Digits = new Stack<Character>();
        Stack<Character> resultDigits = new Stack<Character>();
        
        //既然使用了stack，就注意一定要思考清楚方向
        for(int i = 0; i < num1.length(); i++){
            num1Digits.push(num1.charAt(i));
        }
        
        for(int i = 0; i < num2.length(); i++){
            num2Digits.push(num2.charAt(i));
        }
        
        boolean carry = false;
        
        while(!num1Digits.isEmpty() || !num2Digits.isEmpty()){
            int digit1 = num1Digits.isEmpty()? 0 : num1Digits.pop() - '0';
            int digit2 = num2Digits.isEmpty()? 0 : num2Digits.pop() - '0';
            
            int result = digit1 + digit2 + (carry ? 1 : 0);
            
            resultDigits.push((char)(result % 10 + '0'));
            carry = result / 10 > 0;
        }
        
        if(carry){
            resultDigits.push('1');
        }
        
        StringBuilder sb = new StringBuilder();
        
        while(!resultDigits.isEmpty()){
            sb.append(resultDigits.pop());
        }
        
        return sb.toString();
    }
    
}
```

//将两个stack使用index替代版本
```java
public class Solution {
    /**
     * @param num1 a non-negative integers
     * @param num2 a non-negative integers
     * @return return sum of num1 and num2
     */
    public String addStrings(String num1, String num2) {
        // Write your code here
        
        if(num1 == null || num2 == null){
            return "";
        }
        
        Stack<Character> resultDigits = new Stack<Character>();
        
        boolean carry = false;
        
        int index = 0;
        
        while(index < num1.length() || index < num2.length()){
            int digit1 = index < num1.length() ? num1.charAt(num1.length() - 1 - index) - '0' : 0;
            int digit2 = index < num2.length() ? num2.charAt(num2.length() - 1 - index) - '0' : 0;
            
            int result = digit1 + digit2 + (carry ? 1 : 0);
            
            resultDigits.push((char)(result % 10 + '0'));
            carry = result / 10 > 0;
            index++;
        }
        
        if(carry){
            resultDigits.push('1');
        }
        
        StringBuilder sb = new StringBuilder();
        
        while(!resultDigits.isEmpty()){
            sb.append(resultDigits.pop());
        }
        
        return sb.toString();
    }
    
}
```

### 笔记

这题还是学到了蛮多东西的。

刚开始看到这道题并没有注意到"Big"这个关键点，所以很天真地觉得这题其实就是把两个input的String先都转换成为int，然后把相加的结果再转换成String的一道题。结果就发现很快溢出了，然后换了long也不行，因为题目中说了**The length of both num1 and num2 is < 5100**,long也是handle不了这么长的数据的。

而且你别看，虽然上面的这个方法失败了，但还是很有学问的，相当于上面的这种写法需要两个基础操作:
(1)**int to string**
(2)**string to int**

而这中转换方式都各有自己的技巧，需要注意。


在发现不能把数字作为整体来处理后，就感觉这题应该有点像 add two number中需要单个单个digit地处理。
再结合构造数字时的特点，想到使用3个stack来“倒腾”这些digit，最后能够生成需要的结果。关键的技巧和add two number是一样的。

在使用三个stack的基础上，就发现想到其实前两个stack的使用是没有必要的，只要使用一个index就可以代替，大大节省空间。

不管哪种方法，最后退出while循环后要注意还要看看是否还有carry，如果有需要添加"1".