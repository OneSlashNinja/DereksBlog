---
layout: post
title:  "LeetCode 1 - 2 Sum"
date:   2017-05-16 17:55:02 -0400
categories: leetcode, Amazon
---

# 2 sum

## 一刷

### 代码

version(HashMap, 第一次写错,修改两处之后勉强过的version)
```java
public class Solution {
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        
        if(numbers == null || numbers.length == 0){
            return null;
        }
        
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < numbers.length; i++){
            map.put(target - numbers[i], i);
        }
        
        for(int i = 0; i < numbers.length; i++){
            if(map.containsKey(numbers[i]) && map.get(numbers[i]) != i){
                result[0] = Math.min(map.get(numbers[i]) + 1, i + 1);
                result[1] = Math.max(map.get(numbers[i]) + 1, i + 1);
            }
        }
        
        
        return result;
    }
}
```

version(HashMap,写对的version)：
```java
public class Solution {
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        
        if(numbers == null || numbers.length == 0){
            return null;
        }
        
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < numbers.length; i++){
            if(map.containsKey(numbers[i])){
                result[0] = map.get(numbers[i]) + 1;
                result[1] = i + 1;
                break;
            }
            map.put(target - numbers[i], i);
        }

        return result;
    }
}
```

### 笔记

该题目用HashMap的第一个version又犯了前面同样的错：

可以看出，虽然程序过了，但是这一段有两处很繁琐：
if(map.containsKey(numbers[i]) && map.get(numbers[i]) != i){
    result[0] = Math.min(map.get(numbers[i]) + 1, i + 1);
    result[1] = Math.max(map.get(numbers[i]) + 1, i + 1);
}

第一个是要判断map.get(numbers[i]) != i
第二个是要判断map.get(numbers[i]) + 1和 i + 1谁大。

而第二个版本不仅一层循环，并且完全不用判断这两个地方。为什么呢？

想先整个for循环一遍数组构建出整个完整地HashMap，然后再去看是否又符合要求的项。这样分步骤的思路是没错，但是忽略了一点本题的要求：
要求[i,j]i是小于j的(不能大于，不能等于)，i必须是在j的前面。而要满足这个条件，在构建HashMap的过程中动态地去检测就能完美实现。和上面Subarray max sum异曲同工。

另外本题也可以用two pointers的方法做，具体做法看two sum closest。

---

## 二刷

### 代码

```java
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] results = new int[]{-1, -1};
        
        if(nums == null || nums.length < 2){
            return results;
        }
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                results[0] = map.get(nums[i]);
                results[1] = i;
                return results;
            }
            map.put(target - nums[i], i);
        }
        
        return results;
    }
}
```

map中存直接value的版本
```java
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] results = new int[]{-1, -1};
        
        if(nums == null || nums.length < 2){
            return results;
        }
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                results[0] = map.get(target - nums[i]);
                results[1] = i;
                return results;
            }
            map.put(nums[i], i);
        }
        
        return results;
    }
}
```

### 笔记

基本是5分钟一遍通过，主要就是三个关键点：
(1) HashMap
(2) 在循环的过程中动态构建，这样就不会出现同一个元素使用两次的情况。
(3) 存的key是值，value是index，并且存在HashMap中的key是(target - nums[i])后者是(nums[i])都是可以的，只要最后和check的时候对应起来就可以。