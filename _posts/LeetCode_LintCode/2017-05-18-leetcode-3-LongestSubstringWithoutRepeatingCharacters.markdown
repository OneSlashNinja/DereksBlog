---
layout: post
title:  "LeetCode 3 - Longest Substring Without Repeating Characters"
date:   2017-05-18 00:10:02 -0400
categories: leetcode, Amazon
---

# Longest Substring Without Repeating Characters

## 一刷

### 代码

自己的version：
```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int start = 0, end = start + 1;
        
        int longestSub = 1;
        
        while(end <= s.length() - 1){
            StringBuilder sb = new StringBuilder();
            sb.append(s.charAt(start));
            end = start + 1;
            
            while(end <= s.length() - 1){
                
                //System.out.println(sb.toString());
                //System.out.println(sb.indexOf(String.valueOf(s.charAt(end))));
                
                if(sb.indexOf(String.valueOf(s.charAt(end))) >= 0){
                    longestSub = Math.max(longestSub, end - start);
                    start = start + sb.indexOf(String.valueOf(s.charAt(end))) + 1;
                    break;
                }
                
                sb.append(s.charAt(end));
                end++;
            }
            //System.out.println(start+","+end);
        }
        
        longestSub = Math.max(longestSub, end - start);
        
        return longestSub;
    }
    
}
```

看了leetcode题解后的brute force：
```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int result = 0;
        
        for(int i = 0; i < s.length(); i++){
            for(int j = i + 1; j <= s.length(); j++){
                if(areAllUnique(s, i, j)){
                    result = Math.max(result, j - i);
                }
            }
        }
        
        return result;
        
    }
    
    private boolean areAllUnique(String s, int start, int end){
        HashSet<Character> set = new HashSet<Character>();
        
        for(int i = start; i < end; i++){
            if(set.contains(s.charAt(i))){
                return false;
            }else{
                set.add(s.charAt(i));
            }
        }
        
        return true;
        
    }
    
}
```

看了leetcode的初步sliding window version：
```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int left = 0, right = 0;
        int longestSub = 0;
        
        HashSet<Character> set = new HashSet<Character>();
        
        while(right < s.length()){
            if(set.contains(s.charAt(right))){
                set.remove(s.charAt(left));
                left++;
            }else{
                set.add(s.charAt(right));
                right++;
                longestSub = Math.max(longestSub, right - left);
            }
        }
        
        return longestSub;
    } 
    
}
```

更加[left, right)的version：
```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int left = 0, right = 1;
        int longestSub = 0;
        
        HashSet<Character> set = new HashSet<Character>();
        
        while(right <= s.length()){
            if(set.contains(s.charAt(right - 1))){
                set.remove(s.charAt(left));
                left++;
            }else{
                set.add(s.charAt(right - 1));
                longestSub = Math.max(longestSub, right - left);
                right++;
            }
        }
        
        return longestSub;
    }   
    
}
```

使用HashMap的version(见分析)：
```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int longestSub = 0;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        
        for(int right = 0, left = 0; right < s.length(); right++){

        	//注意，这里如果map.containsKey(s.charAt(right)) == true并不一定说明
        	//当前的substring中就有重复的元素，因为很可能存的下标已经不在当前的window中了。
            if(!map.containsKey(s.charAt(right))){
                map.put(s.charAt(right), right);
                longestSub = Math.max(longestSub, right - left + 1);
            }else{
                left = Math.max(left, map.get(s.charAt(right)) + 1);
                //重新update元素的位置
                map.put(s.charAt(right), right);
                //根据上面的解释，再加上for一直会使得right++，所以下面的判断必须要，否则会有问题
                longestSub = Math.max(longestSub, right - left + 1);
            }
        }
        
        return longestSub;
    }
    
    
    
}
```

在上一个HashMap的基础上精简的版本：

```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int longestSub = 0;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        
        for(int right = 0, left = 0; right < s.length(); right++){
            if(map.containsKey(s.charAt(right))){
                left = Math.max(left, map.get(s.charAt(right)) + 1);
            }
            
            map.put(s.charAt(right), right);
            longestSub = Math.max(longestSub, right - left + 1);
        }
        
        return longestSub;
    }
    
    
    
}
```

使用int[256]的极值精简版本：
```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer 
     */
    public int lengthOfLongestSubstring(String s) {
        // write your code here
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int longestSub = 0;
        
        int[] map = new int[256];
        
        Arrays.fill(map, -1);
        
        for(int right = 0, left = 0; right < s.length(); right++){
            left = Math.max(left, map[s.charAt(right)] + 1);
            map[s.charAt(right)] = right;
            longestSub = Math.max(longestSub, right - left + 1);
        }
        
        return longestSub;
    }
    
    
    
}
```

### 笔记
这是一道非常神奇的题。
虽然难度是medium，而且大概的思路一说你也能理解，但是要写对非常难。

而且更神奇的是之前的各个那些大神在其他题上的实现都大同小异，但是似乎对这道题的解题却是千奇百怪。
喜刷刷的思路很奇怪，居然要在for循环中再用一个for进行hashtable的删除？什么鬼？
水中的鱼的思路很直接：

“
从左往右扫描，当遇到重复字母时，以上一个重复字母的index +1，作为新的搜索起始位置。
直到扫描到最后一个字母。
”

但是按照他的思路实现的话(自己的第一个version)，会有不少的问题，不简洁，后面讲。

Grandyang的第一个版本代码看起来很简洁，但是和水中的鱼的方式又很相反的地方：
水中的鱼是每碰到一个重复的char时触发一次longestSub的计算，而Grandyang则是相反，没有碰到重复的时候才触发longestSub的计算。

九章算法的版本思路像是leetcode中第一个sliding window的变种，但是变种地非常别捏。
而且你说你用了int[]当map你还不好好利用是int的特点，value只是1或者0，那你为啥不直接用个boolean[]就得了。

而所有的分析和答案中，最清晰的也就是leetcode上的解释，循序渐进解释了整个思路的演进。非常好:

https://leetcode.com/articles/longest-substring-without-repeating-characters/


在自己的第一个version的实现中，有非常多蹩脚且关键的缺陷：

(1)非常关键！！对于碰到判断重复或者去重的题目，要敏感地神经反射地想到是否可以使用HashMap或者HashSet。(如果不行，看看能不能排序等)。
而这道题就是非常适合使用HashMap或者HashSet。并且！如果输入集是一个有限集，比如对于这道题，可以问清楚：
输入是只限定于26个字母，还是ASCII码，还是更多？
如果说只是26个字母，那么我们用int[] map = new int[26];就可以充当HashMap来使用。
如果说是ASCII码，那么因为ASCII码有256个(也要记住)，则我们可以使用int[] map = new int[256];就可以充当HashMap来使用。
而如果说比ASCII码还要多，那么这是我们可以退而求其次，使用HashMap。

使用int[]来替代HashMap对于时间和空间上来说都有好处：
<1>因为是直接通过下标1对1的map，所以时间上来说是guaranteed O(1)时间，相比HashMap:
We talk about this by saying that the hash-map has O(1) access with "high probability"

<2>相比于HashMap，使用空间多少并不确定，int[]使用的是确定的extra space。

而自己实现的第一个version中，判断是不是重复还是通过stringBuilder来看某个char是不是在其中，显得很不简洁。

(2)虽然知道是一前一后两个指针来确定一块区域(sliding window)，但是怎么去移动这一前一后处理的并不好。

(3)因为使用了水中的鱼的思路，所以在循环结束后还需要再把longestSub = Math.max(longestSub, end - start);比较一次。
这样就显得很不简洁。

并且要注意是sb.indexOf(String.valueOf(s.charAt(end))) >= 0而不是
sb.indexOf(String.valueOf(s.charAt(end))) > 0


那么接下来说说leetcode的brute force版本，该brute force版本虽然会超时，但也是很具有研究性和讲究的。

首先说，该brute force也是基于使用HashSet来判断是否有重复的，大致思路其实也是sliding window，只不过这个sliding window穷举了很多冗余的部分。大致的实现过程是这样的：
将程序分为两个method：
(1)一个method用来判断string从start到end的部分是否是unique的。
(2)有了上面的方法，就可以使用两层循环，然后相当于外层循环是left指针，内层循环是right指针，然后穷举的去试每个0<=i<j<=n，去看当前[i,j)段是否满足unique，如果满足，则看看当前段的长度和之前最长谁长，从而更新最长。

这个brute force版本不仅分出一个private的areAllUnique使得程序很清晰并且解耦和还教了怎么用HashSet来判断当前段落的重复。
而各更重要的一点是，从这个实现中我们需要看到一点很容易忽略的：
0<=i<j<=n
[i,j)

对于这种sliding window或者说双指针的题，对于到底谁是inclusive，谁是exclusive一定要在全局是统一的，要在一开始就心里有数再开始实现。比如，本实现中因为选的是[i, j)的方式，所以：
for(int j = i + 1; j <= s.length(); j++)既不能写成
for(int j = i + 1; j < s.length(); j++) 因为j最后是要exclusive的，所以需要延伸到s之外一格。
也不能写成for(int j = i; j < s.length();j++)这样的话j就是inclusive的了。

而result = Math.max(result, j - i);就不能写成
result = Math.max(result, j - i + 1);

更甚至private boolean areAllUnique(String s, int start, int end)中也是
for(int i = start; i < end; i++){而不是
for(int i = start; i <= end; i++){

所以从上面可以看出，一旦确定了start和end的哪个是inclusive哪个是exclusive，就一定要在脑中潜意识地记住，然后在处理两者的时候都遵循该形式。



并且，该brute force方法为什么最后复杂度为O(n^3)的推导也非常值得研究（具体看leetcode的分析），要记住等差数列求和公式是：
Sn = n(a1 + an) / 2


在brute force的基础上进行改进，使用真正的sliding window，就写出了第一个sliding window的version，这个version有以下特点：
(1)解决了部分冗余，相当于在增量的基础上如果发现了重复就开始进行调整，而不是去试每一个可能性。但可以发现，因为left和right在每次while的判断中只移动left或者right一格，所以仍有提升的空间。
(2)leetcode的版本有些冗余，因为知道left<right<=n.所以可以直接写成while(right < s.length()){而不是
while(left < s.length() && right < s.length()){
(3)虽然仍然是[left, right)。但是似乎leetcode的写法并不是很统一，只是因为while和for循环相比，可以不是在最结尾就对right进行++，所以感觉上相当于
只有
right++;
longestSub = Math.max(longestSub, right - left);
这一部分的时候right是[left, right)的。
其他部分都像是[left, right]的。

也可以看出来while循环比起for更容易混淆到底什么时候是[i, j]，什么时候是[i, j)

(4)因为在有重复的时候不能进行longestSub的判断，所以只是在判定没有重复的时候才进行longestSub = Math.max(longestSub, right - left);

上述版本的version已经可以优化到O(n)级别的了，不过可能是2n，所以其实还可以优化。

那么观察这个version我们可以发现一点，因为我们用的是HashSet，所以只能存储某个char是否已经在当前的substring中。而如果我们优化存储的数据结构，使得我们不仅可以知道某个char是否已经在subString中，还能知道其在substring中的什么位置，那么我们便可以利用这个位置，直接将window的左侧挪动到最合适的位置。那么这个数据结构可以是HashMap。也可以像上面所讲的，如果知道输入集是有限集，那么可以直接用一个int[]来代替hashmap。


使用HashMap的version乍一看似乎和之前的HashSet只是细微的区别，但其实区别还挺大的。：
(1)就像刚才说的，前面的HashSet会删除已在当前substring中的char，而HashMap的version并不会删除元素，如果hashMap中已经存在right所指的元素，就需要判断存在的元素是否在window中，再加上因为使用的是for循环而不是while循环，每次right都会自动地++，所以，不管contain的判断结果是怎么样的，都需要重新计算longest的长度。

根据这个版本，提取出公共的部分，就可以写出精简的版本。


最后，就是使用int[256]来代替HashMap的版本。

首先，注意Java中要把一个数组的所有元素都初始化为某个值的语法为：
Arrays.fill(map, -1);

再一个，在这个版本中，可以看到，上一版本因为使用hashMap，所以在for中仍然有一个if判断：
if(map.containsKey(s.charAt(right))){
    left = Math.max(left, map.get(s.charAt(right)) + 1);
}
因为map.get(...)中填的是一个没有的key是会报错的。

而这里我们使用的int[]，所以每个字符都有对应的位置，如果之前没有，就会是-1
所以我们索性连这个if都可以省略了，用一个Math.max()来将其代替。

注意是left = Math.max(left, map.get(s.charAt(right)) + 1);而不是
left = Math.max(left, map.get(s.charAt(right)));

最后就有了极值简洁的版本，并且时间和空间效率都非常高：
Time complexity : O(n)O(n). Index jj will iterate nn times.

Space complexity (HashMap) : O(min(m, n))O(min(m,n)). Same as the previous approach.

Space complexity (Table): O(m)O(m). mm is the size of the charset.



说了这么多，那么这道题最核心的地方是什么？
(1)对于检测重复和去重复的题，一定要有下意识去想是否能用HashSet或者HashMap？
如果能用，那么输入集是否是有限集？如果是，甚至可以用int[]来代替HashMap。

(2)sliding window的左右指针在什么情况下移动？移动到哪儿？是inclusive还是exclusive？

---

## 二刷

### 代码

**错误代码**
```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        boolean[] existedChars = new boolean[256];
        
        int longestNonRepeatLength = 0;
        
        for(int i = 0; i < s.length(); i++){
            char currentChar = s.charAt(i);
            if(existedChars[currentChar]){
                break;
            }
            existedChars[currentChar] = true;
            longestNonRepeatLength++;
        }
        
        return longestNonRepeatLength;
        
    }
}
```

**错误代码2**

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int[] existedCharsIndex = new int[256];
        Arrays.fill(existedCharsIndex, -1);
        
        int longestNonRepeatLength = 0;
        int currentStartIndex = 0;
        int currentNonRepeatLength = 0;
        
        for(int i = 0; i < s.length(); i++){
            char currentChar = s.charAt(i);
            if(existedCharsIndex[currentChar] >= currentStartIndex){
                currentStartIndex = i;
                longestNonRepeatLength = Math.max(currentNonRepeatLength, longestNonRepeatLength);
                currentNonRepeatLength = 1;
            }else{
                currentNonRepeatLength++;
            }
            
            existedCharsIndex[currentChar] = i;
        }
        
        longestNonRepeatLength = Math.max(currentNonRepeatLength, longestNonRepeatLength);
        
        return longestNonRepeatLength;
        
    }
}
```

**再看过Leetcode讲解后的使用set的版本**

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        Set<Character> charSet = new HashSet<Character>();
        
        int start = 0, end = 0;
        int longestLength = 0;
        
        while(end < s.length()){
            //注意如果发现当前字符已经存在，需要先remove，然后移动的是start
            //如果不存在，则先add，然后移动end，而且还需要做一次是否最长的判断
            if(charSet.contains(s.charAt(end))){
                charSet.remove(s.charAt(start));
                start++;
            }else{
                charSet.add(s.charAt(end));
                end++;
                longestLength = Math.max(longestLength, end - start);
            }
        }
        
        longestLength = Math.max(longestLength, end - start);
        
        return longestLength;
    }
}
```

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        if(s == null || s.length() == 0){
            return 0;
        }
        
        int[] charIndexMap = new int[256];
        Arrays.fill(charIndexMap, -1);
        int lengthOfLongest = 0;
        
        for(int start = 0, end = 0; end < s.length(); end++){
            //注意:(1) 是charIndexMap[s.charAt(end)] + 1，因为要锁定到重复的那个字符后，跳过去，从下一个开始
            //(2)不是start = charIndexMap[s.charAt(end)] == -1 ? start : charIndexMap[s.charAt(end)] + 1;
            start = Math.max(start, charIndexMap[s.charAt(end)] + 1);
            charIndexMap[s.charAt(end)] = end;
            lengthOfLongest = Math.max(lengthOfLongest, end - start + 1);
        }
        
        return lengthOfLongest;
    }
}
```

### 笔记

二刷的第一遍写错了是因为完全没考虑到如果substring是可能起点不是第一个character的。
第二遍写错了，先是一些条件上的错误，然后发现致命的一点就是像"dvdf"这个输入，自己写成程序碰到"dvd"这个重复后就会直接从第二个d开始计算，但其实这样就会漏掉"vdf"。

然后再复习了一遍自己之前的笔记和leetcode的讲解，发现其中一个重点是想到了的：
(1)因为是和判断重复有关，所以应该条件反射地想到使用HashMap，甚至因为输入是有限集，甚至可以用数组来代替。

但是另一个重点，也就是sliding window并没有想到或者说运用好。

其实sliding window这个概念，用set来实现的那个版本体现的最好，因为不管是window的left还是right，都是一格一格真的在"sliding"的感觉。

该题的brute force解法的时间复杂度注意是**O(n^3)**

最后一个最精简版本虽然很短，但其实要写完全正确也是几个tricky的地方的，主要是start的定位：
(1)首先start的定位如果说发现有重复于end位置的字符，那么要找到这个位置，**然后跳过**，所以是charIndexMap[s.charAt(end)] + 1而不是直接的charIndexMap[s.charAt(end)]
(2)即使charIndexMap[s.charAt(end)]不为-1，也是可能比当前的start小的，那么这种情况下start就**不能往回跳**，所以`start = charIndexMap[s.charAt(end)] == -1 ? start : charIndexMap[s.charAt(end)] + 1`的写法是错误的，正确的是需要比大小`start = Math.max(start, charIndexMap[s.charAt(end)] + 1);`

**如果看不出来程序到底错在哪儿，最好的办法就是手动在纸上跑test case**

最后就是再注意如果要初始化一个数组的所有值为某一个特定的value，Java中可以使用:
`Arrays.fill(array, val)`