---
layout: post
title:  "lintcode 636 - 132 Pattern"
date:   2017-11-25 20:31:09.635616
categories: lintcode, Snapchat
---

# 132 Pattern

## 一刷

### 代码

加强版的brute force
```java
    public boolean find132pattern(int[] nums) {
        // write your code here
        
        if(nums == null || nums.length == 0){
            return false;
        }
        
        int prefixMin = Integer.MAX_VALUE;
        
        for(int i = 0; i < nums.length; i++){
            prefixMin = Math.min(prefixMin, nums[i]);
            
            if(nums[i] > prefixMin){//如果正好当前元素是最小元素则没必要检查，肯定不会组成该pattern
                for(int j = i + 1; j < nums.length; j++){
                    if(nums[j] < nums[i] && nums[j] > prefixMin){
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
```

经过研究和思考leetcode stack版本后自己写的一遍过的版本
```java
public class Solution {
    /*
     * @param nums: a list of n integers
     * @return: true if there is a 132 pattern or false
     */
    public boolean find132pattern(int[] nums) {
        // write your code here
        
        if(nums == null || nums.length == 0){
            return false;
        }
        
        int len = nums.length;
        Stack<Integer> stack = new Stack<>();
        int[] prefixMin = new int[len];//因为traverse的过程是从后往前的，所以没法使用滚动的prefixMin，需要预存整个数组
        
        prefixMin[0] = nums[0];
        for(int i = 1; i < len; i++){
            prefixMin[i] = Math.min(prefixMin[i - 1], nums[i]);
        }
        
        //这里使用j来表示，是为了更能跟题意中的j对应起来
        for(int j = len - 1; j >= 0; j--){
            
            //如果该条件不满足，则ai < ak < aj中连ai < aj都不满足，就没必要继续进行检查了
            if(nums[j] > prefixMin[j]){
                
                //修正到满足ai < ak这个条件或者栈空为止
                while(!stack.isEmpty() && stack.peek() <= prefixMin[j]){
                    stack.pop();
                }
                
                //经过上面的while的一步，如果此时stack不为空，并且还能满足ak < aj
                //那么就达成了ai < ak < aj的条件，直接返回就可以
                //否则就需要把当前的元素push到栈顶，这样既能维持栈自底向上递增的特性，并且能够相当于缩小ak,给aj更多可能的空间(不过有可能会在下一个while中被pop出去)
                if(!stack.isEmpty() && stack.peek() < nums[j]){
                    return true;
                }else{
                    stack.push(nums[j]);
                }
            }
            
        }
        
        //如果扫过一遍没有找到，则肯定不会有该pattern
        return false;
    }
}
```

### 笔记

本题其实难度depends。如果说暴力算法是easy，那么加强暴力应该是medium，而使用stack的版本难度则大概应该是hard。

本题首先要明确的条件是i, j, k三个index并不一定是相连的，否则该题就非常好解了。实际上i, j, k三点位置上只要满足i < j < k就行。

所以，可以想到，brute force的解法肯定是三层循环，内层的起点是从外层当前循环的位置开始的下一个。对于每个i, j, k比较是否足要求就可以了。

这种暴力方法的时间复杂度是: O(n^3), 而空间复杂度是O(1)

那么有没有更好的解法呢? 这题虽然自己一开始没有写出更优化的代码，但是自己认为找到了正确解题的思维方式。

那就是，对于整个数组，看成三个部分:
**nums[i], nums[i]左边的部分和nums[i]右边的部分。从而把"ai < ak < aj"这个条件拆分为"ai < ak"和"ak < aj"这两个部分，分而治之。**

一开始的思路是像"trap rain water"那题一样，用空间换时间，进行两边traverse分别构造prefixMin和prefixMax，然后分别和i进行比较即可。
但是发现，**对于要满足`i < j < k and ai < ak < aj`这个条件，prefixMin的数组肯定是能用的上的，因为要满足条件并且要让k的范围越广，那ai就越小越好。**
但是ak作为右边数组的特殊值，并不是某个极值能表示的，太大了可能"ak < aj"这个条件不能满足，太小了又可能"ai < ak"这个条件不能满足。

看了leetcode的solution后发现，自己的思路其实是对的，只不过根据上面的分析, **k既然不能是极值，那么和j一样，也应该是一个动态的寻找过程**。

所以，先对i找极值(极小值)，然后对j和k动态地进行两层动态寻找，于是就有了加强版的brute force。时间复杂度也因此能提到O(n^2).

对于空间复杂度，其实思考会发现并不需要维护一个prefixMin的array，只需要一个滚动的变量即可，on the fly地进行更新。所以空间复杂度是O(1)。

而本题在leetcode solution中还提到了非常多种解法:[leetcode solution -  456. 132 Pattern](https://leetcode.com/problems/132-pattern/solution/)

其中除了上面提到的两种解法外，还比较值得一提的就是**stack**的版本。

其实stack的版本一开始感觉很难明白，但其实思路还是和刚才提到的一样，将整个数组分为[nums[i]左边, nums[i], nums[i]右边]三种情况:
1. 使用一个prefixMin来确定左边
2. i代表当前元素
3. stack中其实存储的是nums[i]右边的情况, 使用空间换时间，利用特殊的结构，来将动态的搜索变为直接的查找比较。

而其中的步骤和关键点就是:
1. 先构建prefixMin，这回因为要从后往前走，所以没法使用滚动的prefixMin了，需要额外的数组。
2. **从后往前traverse**，去看**min[j], nums[j], stack顶**三者的关系：
    * 首先，最外层的条件应该是`(nums[j] > min[j])`，也就是看`ai < ak < aj`中是否满足`ai < aj`的情况，这个情况最容易检查。如果这个都不满足，那就没必要进行下面的检查。
    * 如果stack不为空并且`stack.peek() <= min[j]`，则说明, **对于stack栈顶的元素不满足ai < ak的条件，需要一直pop到满足或者栈空为止(因为stack维护了一个自底向上递增的序列)**
    * 然后在判断，如果stack是空的，或者stack顶的元素比nums[j]大，则说明,**对于当前的j, 不可能有满足ak < aj的情况(因为stack维护了一个自底向上递增的序列)**,那么把当前nums[i]就push到stack顶上，维持当前stack的性质，并放宽对于ak < aj的要求。
    * 如果上面的条件都能满足，则找到了一个pattern，直接返回即可。

因为stack中能push和pop的元素最多是整个stack，所以加上处理的时候，都是一遍扫过，时间复杂度是**O(n)**。
而因为使用stack