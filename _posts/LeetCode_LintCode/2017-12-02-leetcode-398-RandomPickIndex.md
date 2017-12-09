---
layout: post
title:  "leetcode 398 - Random Pick Index"
date:   2017-12-02 21:18:01.163742
categories: leetcode, Facebook
---

# Random Pick Index

## 一刷

### 代码

根据思路自己写出来的Reservoir Sampling算法
```java
class Solution {

    private int[] nums;
    private Random rand;
    
    public Solution(int[] nums) {
        this.nums = nums;
        this.rand = new Random();
    }
    
    public int pick(int target) {
        
        int result = -1;
        int count = 0;//count表示目前为止已经遇见了几个和target等值的元素
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == target){
                result = rand.nextInt(++count) == 0 ? i : result;
            }
        }
        
        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```

### 笔记

这题和Linked List Random Node类似，Linked List Random Node中的限制条件是不知道LinkedList的长度，而该题则是不允许使用额外的空间。

如果让使用额外的空间，那么一切好说，算法就是: 
1. 遍历一遍原数组，使用额外数组temp来盛放所有和target值一样的元素
2. 产生一个范围是[0...temp.length - 1]随机数,取temp中该位置的元素即可

但是如果不允许使用额外空间该怎么办呢? 答案是**Reservoir Sampling**, 可以看出Reservoir Sampling真是一个神奇的算法，不仅可以使用在不知道样本总量的情况下，并且还能在某些情况下帮助节省空间。

具体的算法就是:
遍历整个array，维护一个count，该count表示**目前为止已经遇见了几个和target等值的元素**
当碰到array[i] == target的情况，则以**(1 / count)**的概率留下该元素作为结果。

这样，就只需要一个count

具体对于Reservoir Sampling的研究和证明，见自己的笔记。

参考见:
[leetcode discuss - simple-reservoir-sampling-solution](https://discuss.leetcode.com/topic/58301/simple-reservoir-sampling-solution)
[Grandyang - Random Pick Index 随机拾取序列](http://www.cnblogs.com/grandyang/p/5875509.html)
[数据工程师必知算法：蓄水池抽样](http://blog.jobbole.com/42550/)