---
layout: post
title:  "leetcode 168 - Excel Sheet Column Title"
date:   2017-11-03 21:42:52.113123
categories: leetcode, Amazon, Facebook, Bloomberg
---

# Excel Sheet Column Title

## 一刷

### 代码

```java
class Solution {
    public String convertToTitle(int n) {
        
        if(n <= 0){
            return null;
        }
        
        StringBuilder sb = new StringBuilder();
        
        while(n > 0){
            n--;//本题的关键，因为从A开始的26进制没有0的概念，所以每到下一位都得向左位移一次
            int remainder = n % 26;
            
            //此处因为之前向左位移了一次，也不用再'A' + remainder - 1了
            //另外要注意，对于'A' + remainder会变成数字，需要再cast成char
            sb.append((char)('A' + remainder));
            
            n = n  / 26;
        }
        
        return sb.reverse().toString();
        
    }
}
```

### 笔记

一开始一直绕不过来弯，感觉应该就是10进制转换成26进制的题，使用%配合/来完成，但是总感觉哪里不太对。

后来能感觉到是因为这个目标的26进制中并没有0，所以会有问题。失败了之后，觉得"难不成这题不是26进制，而是27进制？"但是试过了之后发现其实也不是

对于十进制，有从0~9是个数字，但是0是个神奇的存在，表示没有，所以"十"是有两个digit也就是10表示的。但是对于Excel的系统则不同，因为没有0，虽然也是26个字母应该是26进制，但是因为没有0，所以26的表示是'Z'而不是'AA'或者'BA'(如果A表示0，则这个表示是正确的)。

所以，**对于每一位**，每次在进行转换的时候，要先将含0的坐标系左移一位(也就是-1),才能和无零的坐标系"对齐"，然后进行转换。


注意Excel Sheet Column Number中就有一个相应的 + 1