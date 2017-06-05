---
layout: post
title:  "LeetCode 42 - Trapping Rain Water"
date:   2017-05-30 00:00:02 -0400
categories: leetcode, Amazon
---

# Title

## 一刷

### 代码
看答案后自己写的version：
```java
public class Solution {
    /**
     * @param heights: an array of integers
     * @return: a integer
     */
    public int trapRainWater(int[] heights) {
        // write your code here
        
        if(heights == null || heights.length == 0){
            return 0;
        }
        
        int[] leftMax = new int[heights.length];
        int[] rightMax = new int[heights.length];
        
        leftMax[0] = heights[0];
        rightMax[heights.length - 1] = heights[heights.length - 1];
        
        for(int i = 1; i < heights.length; i++){
            leftMax[i] = Math.max(leftMax[i - 1], heights[i]);
        }
        
        for(int i = heights.length - 2; i >= 0; i--){
            rightMax[i] = Math.max(rightMax[i + 1], heights[i]);
        }
        
        int totalRainAmount = 0;
        
        for(int i = 0; i < heights.length; i++){
            //cong'qian'mian从前面从前面Math.min(leftMax[i], rightMax[i]) - heights[i] >= 0
            //if(Math.min(leftMax[i], rightMax[i]) > heights[i]){
                totalRainAmount += Math.min(leftMax[i], rightMax[i]) - heights[i];
            //}
        }
        
        return totalRainAmount;
    }
}
```

### 笔记
这道题的基本思路是想办法计算出每一块的水的容量，然后扫一遍heights数组，相加起来即可。
而每一块的水的容量，跟其左右分别的max的height中较小的那个有关，所以需要知道每个位置左右最大的那个height。

那么，就可以用空间换时间，声明两个和heights一样大小的数组，分别用来记载在某个位置左边的max和右边的max各是多少。从而避免在每个位置都得重新计算max。

所以，整个程序就是扫三遍heights：
第一遍用来计算出整个leftMax数组
第二遍用来计算出整个rightMax数组
第三遍用前两遍的结果，来整合出所有trapped rain water(其实很多版本中把第二三遍合并了)

所以，该算法的时间复杂度和空间复杂度都是O(n)

那么说这又是一道看着感觉和最大直方图或者water container有点像的题，那么为什么这道题的做法又不一样呢？

和water container不一样是因为water container竖着的是line，是不占“面积”的，它只是制约面积。而trap rain water和最大直方图属于不仅每一块占面积，而且也制约所要求得面积的。

而trap rain water和最大直方图的解法的不一样在于：
trap rain water的某一块是和它左右两边max的有关系(包括它自己)，
而最大直方图的某一块是和它能延伸到的最远位置有关系，也就是左右第一个比它小的，而这种关系没有办法像trap rain water中的那样用空间换时间，通过一遍扫描就能够计算出所有点相应的左第一个小于它的。

---

## 二刷

### 代码

使用额外两个数组版
```java
public class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }
        
        int arrLen = height.length;
        int[] leftMax = new int[arrLen];
        int[] rightMax = new int[arrLen];
        
        leftMax[0] = -1;
        for(int i = 1; i < arrLen; i++){
            leftMax[i] = Math.max(leftMax[i - 1], height[i - 1]);
        }
        
        rightMax[arrLen - 1] = -1;
        for(int i = arrLen - 2; i >= 0; i--){
            rightMax[i] = Math.max(rightMax[i + 1], height[i + 1]);
        }
        
        int trappedWater = 0;
        
        for(int i = 0; i < arrLen; i++){
            //因为这次的leftMax和rightMax是不包含i所在元素自身的，所以是需要这个if比较的
            if(Math.min(leftMax[i], rightMax[i]) - height[i] > 0){
                trappedWater += Math.min(leftMax[i], rightMax[i]) - height[i];
            }
        }
        
        return trappedWater;
    }
}
```
时间O(n)空间O(1)版
```java
public class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }
        
        int left = 0, right = height.length - 1;
        
        int leftMax = 0, rightMax = 0;
        
        int trappedWater = 0;
        
        while(left < right){
            //这个比较非常重要
            //经过思考可以得出发现，这个if比较中height[left]和height[right]较大的一个一定是在
            //height[left], height[right], maxLeft, rightRight这四个变量中最大的一个
            //这是因为指向这个最大值的指针会一直不动，迫使另一边一直挪动，直到对面找到一个更大的值
            if(height[left] <= height[right]){
                if(leftMax < height[left]){
                    leftMax = height[left];
                }else{
                    //到这里，根据之前对于if的分析，我们可以肯定的是height[right] >= leftMax >= height[left]
                    //所以取两边较小的值为盛水的高度
                    trappedWater += leftMax - height[left];
                }
                left++;
            }else{
                if(rightMax < height[right]){
                    rightMax = height[right];
                }else{
                    trappedWater += rightMax - height[right];
                }
                right--;
            }
        }
        
        return trappedWater;
    }
}
```

### 笔记
注意这次自己的使用额外空间版本在学习了“Product of Array Except Self”那题中如何正确地填入prefix数组和postfix数组后于原来一刷时候的不同


对于时间O(n)空间O(1)的版本，其实思想和使用了两个额外数组的版本没有差别，都是利用了**某一块位置有多少积水取决于左边和右边的max中的min**，但是不同的是这种后者的算法利用**首尾two pointer，使得但凡扫过的区域的max都在之后不会再用了，所以将两个额外的max数组精简到两个单独的变量leftMax和rightMax**，这样一遍扫描就可以计算出结果。

其中最巧妙的一点就是注释中的那个并不明显的部分，在if的比较中其实就确定了height[left],height[right]中的哪一个会是height[left],height[right],leftMax,rightMax中最大的，这就使得那个较大者变成了一个可以完全当成“高墙”的存在，把另一边的max当成决定容积的那一块板即可。