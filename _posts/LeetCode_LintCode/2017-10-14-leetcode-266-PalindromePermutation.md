---
layout: post
title:  "leetcode 266 - PalindromePermutation"
date:   2017-10-14 12:56:57.315211
categories: leetcode, Bloomberg
---

# PalindromePermutation

## 一刷

### 代码

对于permutation最一般性的Backtracking解法，不过Time limit exceed。
```java
class Solution {
    public boolean canPermutePalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        boolean[] visited = new boolean[s.length()];
        
        return dfs(s.toCharArray(), sb, visited);
    }
    
    //注意permutation属于跟顺序有关的，所以其中还有很多需要跳到当前处理的index之前的index
    //也就是每次发散出去都是完全再次发散整个解空间，只靠visited来判断是否已经访问过
    private boolean dfs(char[] str, StringBuilder sb, boolean[] visited){
        
        if(sb.length() == str.length){
            return isPalindrome(sb.toString());
        }
        
        boolean hasPalindrome = false;
        
        for(int i = 0; i < str.length; i++){
            if(!visited[i]){
                visited[i] = true;
                sb.append(str[i]);
                hasPalindrome = hasPalindrome || dfs(str, sb, visited);
                sb.deleteCharAt(sb.length() - 1);
                visited[i] = false;
            }
        }
        
        return hasPalindrome;
    }
    
    private boolean isPalindrome(String s){
        int i = 0, j = s.length() - 1;
        
        while(i < j){
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            //注意不要忘写这部分
            i++;
            j--;
        }
        
        return true;
    }
    
}
```

利用permutation性质的版本
```java
class Solution {
    public boolean canPermutePalindrome(String s) {
        int[] charCount = new int[256];
        
        for(int i = 0; i < s.length(); i++){
            charCount[s.charAt(i)]++;
        }
        
        boolean hasOdd = false;
        
        for(int i = 0; i < charCount.length; i++){
            if(charCount[i] % 2 == 0){
                continue;
            }
            
            if(charCount[i] % 2 == 1 && !hasOdd) {
                hasOdd = true;
                continue;
            }
            
            return false;
            
        }
        
        return true;
    }
}
```

基本一样的leetcode题解的版本，代码稍短
```java
public class Solution {
    public boolean canPermutePalindrome(String s) {
        int[] map = new int[128];
        for (int i = 0; i < s.length(); i++) {
            map[s.charAt(i)]++;
        }
        int count = 0;
        for (int key = 0; key < map.length && count <= 1; key++) {
            count += map[key] % 2;
        }
        return count <= 1;
    }
}
```


### 笔记

一开始看到permutation就觉得估计得Backtracking。然后直接黑怼了一个Backtracking的版本，其中因为少写了"i++,j--"而浪费了不少时间debug，之后还犯了对于permutation的Backtracking不需要int start参数的错误。

然后感觉这如果用了Backtracking至少也得是个medium难度的题吧。而这题加了Palindrome居然也就才easy，那肯定另有蹊跷。

然后就想到了，其实对于一个Palindrome，其中一个很重要的性质可以用在这里才判断一个String能不能组成Palindrome:

**不管Palindrome的长度是奇数还是偶数，组成Palindrome的所有字符中，最多有一个字符可以是奇数字符**

于是就有了简单的版本。自己写的版本使用continue稍微有点读起来不是那么清晰。而leetcode版本更精简易读一些。

