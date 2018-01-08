---
layout: post
title:  "leetcode 283 - Move Zeros"
date:   2017-07-22 21:00:42.357773
categories: leetcode, Facebook,Bloomberg
---

# Move Zeros

## 一刷

### 代码

优化版
```java
public class Solution {
    public void moveZeroes(int[] nums) {
        
        int lastElemNotZero = 0;
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[lastElemNotZero] = nums[i];
                lastElemNotZero++;
            }
        }
        
        for(int i = lastElemNotZero; i < nums.length; i++){
            nums[i] = 0;
        }
        
    }
}
```

最优版
```java
public class Solution {
    public void moveZeroes(int[] nums) {
        
        //r是快指针，l是慢指针
        //可以保证l的左边(注意是左边，l只有在碰到0了之后才能保证指的是0)全部都是非0的数字
        //l就像一个筛子，0穿不过去，只有非零才能穿过去
        //在l和r移动的过程中，所有的0就会"堆积"在l和r之间的位置，直到r走完了，所有的0就堆到了最后

        //在遇到第一个0之前，l和r都是一起移动的
        //从遇到第一个0开始，每次for循环中的if结束后，l所指的就肯定是0，这就构成了当nums[r] != 0时能让r跟l换位置的条件。记得swap后l++，这是慢指针移动的唯一条件。
        for(int r = 0, l = 0; r < nums.length; r++){
            if(nums[r] != 0){
                int temp = nums[r];
                nums[r] = nums[l];
                nums[l] = temp;
                l++;
            }
        }
        
    }
}
```

### 笔记

这题最粗暴的方法就是使用和原数组同样大小的数组，然后从前往后记录非0的数字，然后剩下的位置再全部填充0，然后再copy回去。这样的话空间复杂度是O(n), 时间复杂度是O(n)。

但是明显能感觉到其实空间上是可优化的。

两种优化的方案其实关键点都是**快慢指针**

第一个方案是：慢指针lastElemNotZero用来指向最后一个非零的元素的**下一个**位置，以备下一个非零的元素能够填到合适的位置。而i的作用则是扫描整个数组，去寻找那些非零的元素。

而这里的一个关键点是: 一开始自己觉得如果直接把后面的值写到前面来，会不会造成信息丢失?但你会发现，非零元素的信息是不会丢失的，丢失的是0的信息。但是0都是一样的，所以我们不需要记录每个0，只需要记录0的个数也就可以了。而lastElemNotZero其实就间接地记录了0的个数。这也是为什么lastElemNotZero需要被单独提出来初始化，而后被用在后面一个for循环中。而不是像后面一种方案里可以直接在for循环中初始化。

这个版本不需要额外空间，所以空间复杂度是O(1),时间复杂度是(n)。
不过这个solution对于 [0, 0, 0, ..., 0, 1]这样的情况其实仍然是有多余操作的，按道理最优的方案是第一个位置的0和最后一个位置的1交换就可以，而不是后面n-1个位置都还需要再=0一遍。


那么最优的方案就是用来解决这个问题的。

比起直接把非零的元素assign到lastElemNotZero上，使用swap来代替。这样的话你会发现，所有之前的元素都已经是归位的了，0会被"挤"到后面的部分，所以j到i之间的元素全部是0，所以整整扫一遍就能完成，虽然同样是O(n)，但是是最优的O(n)。


具体的分析请参考LeetCode Solution:
[LeetCode - Move Zeros Solutions](https://leetcode.com/problems/move-zeroes/#/solution)