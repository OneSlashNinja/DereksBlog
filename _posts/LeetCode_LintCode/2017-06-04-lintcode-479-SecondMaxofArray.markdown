---
layout: post
title:  "Lintcode 479 - Second Max of Array"
date:   2017-06-04 00:15:02 -0400
categories: lintcode, Amazon
---

# Second Max of Array

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

错误：
```java
public class Solution {
    /**
     * @param nums: An integer array.
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        /* your code */
        
        int max = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        
        for(int i = 0; i < nums.length; i++){
            //如果是直接找最大是可以用下面的Math.max()来找的
            //如果翻译成普通的if的话是if(nums[i] > max){max = nums[i];}
            //但是这题不能直接用Math.max()，因为if中其实还有别的操作，还需要把原来max中的元素“顶”到second中
            //而且注意，需要先把原来的值填进second
            //if(nums[i] > max){second = max; max = nums[i];}
            max = Math.max(nums[i], max);
            if(nums[i] < max && nums[i] > second){
                second = nums[i];
            }
        }
        
        return second;
    }
}
```

正确
```java
public class Solution {
    /**
     * @param nums: An integer array.
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        /* your code */
        
        int max = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > max){
                second = max;
                max = nums[i];
            }else if(nums[i] > second){
                second = nums[i];
            }
        }
        
        return second;
    }
}
```

正确翻译版
```java
public class Solution {
    /**
     * @param nums: An integer array.
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        /* your code */
        
        int max = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        
        for(int i = 0; i < nums.length; i++){

            if(nums[i] > max){second = max; max = nums[i]; continue;}
            if(nums[i] <= max && nums[i] > second){
                second = nums[i];
            }
        }
        
        return second;
    }
}
```



### 笔记

一开始觉得应该max的数还是直接使用max = Math.max(nums[i], max);去找，然后second就看是不是比目前的second大而比max小。但是会发现这样的问题是，有些max在后来被更大的数取代后会变成第二大的数，但是在这个时候就已经对这个数失去tracking了。

一度认为必须使用排序这样的方法才能获取上面提到的缺失的tracking。

结果发现其实每次只要在找到更大的max时，要同时把原来的max顶到second的位置其实就可以保持tracking。

要注意的是哪个else if使用的很巧妙。否则，如果硬要翻译成自己一开始错误版本的正确版，需要配合一个continue才行。