---
layout: post
title:  "lintcode 656 - Big Integer Multiplication"
date:   2017-11-25 00:47:26.133777
categories: lintcode, Facebook,Twitter,Snapchat
---

# Big Integer Multiplication

## 一刷

### 代码

```java
public class Solution {
    /*
     * @param num1: a non-negative integers
     * @param num2: a non-negative integers
     * @return: return product of num1 and num2
     */
    public String multiply(String num1, String num2) {
        // write your code here
        
        if(num1 == null || num2 == null){
            return null;
        }
        
        int len1 = num1.length(), len2 = num2.length();
        //乘积的长度不会超过len1 + len2. 想象9999x9999 = 99980001
        int len3 = len1 + len2;
        int[] buff = new int[len3];
        
        //这里的carry和加法时候的就不一样了，加法时候carry最多是1，可以用一个Boolean代替，但是这里乘法就必须用int
        int i, j, carry, product;
        
        for(i = len1 - 1; i >= 0; i--){
            carry = 0;
            for(j = len2 - 1; j >= 0; j--){
                //这里还要加buff[i + j + 1]是为了加前一遍循环产生的值
                //之所以是[i + j + 1]而不是[i + j]完全是因为两个数组都是以0为底，而目标的buff应该是以i为坐标，再偏移j位，但是j也是以0为底，所以需要+ 1才能到达正确的位置
                product = carry + buff[i + j + 1] + 
                Character.getNumericValue(num1.charAt(i)) * 
                Character.getNumericValue(num2.charAt(j));
                
                buff[i + j + 1] = product % 10;
                carry = product / 10;
            }
            //不要忘了有可能会有leading的数字
            buff[i + j + 1] = carry;
        }
        
        i = 0;
        
        //这里如果不思考的话肯定应该是i < len3, 但是你会发现如果是num1和num2都为"0"的情况则这里最后会输出空串""
        //所以应该到最后一个字符的时候，不管是不是0，都不能再trim了，所以条件应该是i < len3 - 1
        while(i < len3 - 1 && buff[i] == 0){
            i++;
        }
        
        StringBuilder sb = new StringBuilder();
        
        for(; i < len3; i++){
            sb.append(buff[i]);
        }
        
        return sb.toString();
    }
}
```

### 笔记

这题属于实现型的题目，没有什么"一语惊醒梦中人"的关键思路，主要就是实现的细节。

具体的程序流程其实很像是在模仿我们手动在做多位数乘法时候的过程。

首先，关键的一点是，**不管数字多大，一个n位数乘以一个m位数，长度肯定超不过(m + n)位数**。想象9999x9999 = 99980001

那么我们就可以使用一个`int[] buff = new int[len3]`来作为模拟我们手动做乘法时的buff。

然后就是两层循环，从低位(**但是因为String是反的，所以是从string的末尾开始**)针对两个数一位一位地进行相乘，乘完一层后放进buff里面，然后移一位继续进行相乘。

最后两层循环结束后，buff里的数字就是最终的结果，但是我们需要手动trim一下，这里注意Corner case, "0" x "0"的情况。

最后使用StringBuilder进行append然后输出。

注意为什么是buff[i + j + 1]而不是buff[i + j]


参考:
[九章 - 大整数乘法 · Multiply Strings](https://www.jiuzhang.com/solution/multiply-strings/)