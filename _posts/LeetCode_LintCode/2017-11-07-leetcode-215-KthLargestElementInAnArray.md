---
layout: post
title:  "leetcode 215 - Kth Largest Element In An Array"
date:   2017-11-07 23:51:15.364824
categories: leetcode, Google, Microsoft, Amazon, Bloomberg, Apple, PocketGame
---

# Kth Largest Element In An Array

## 一刷

### 代码

Quick Select
```java
import java.util.Random;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        //shuffle(nums);
        return quickSelect(nums, 0, nums.length - 1, nums.length - k);//找第k大其实就是找第(n - k + 1)小，但是因为坐标以0为底，需要再-1
    }
    
    private int quickSelect(int[] nums, int start, int end, int k){
        
        //因为最后条件的限定，不会像quicksort那样产生start > end的情况，最多只会相等
        if(start == end){
            return nums[start];
        }
        
        int l = start, r = end;
        int mid = start + (end - start) / 2;
        int pivot = nums[mid];
        
        while(l <= r){
            while(nums[l] < pivot){
                l++;
            }
            while(nums[r] > pivot){
                r--;
            }
            
            if(l <= r){
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                l++;
                r--;
            }
        }
        
        if(r >= k && start <= r){//注意此时即使r == k也并不代表r所在的位置就是第k大做在的位置，因为该范围内的元素还都是无序的，只能说k肯定是在该范围内了
            return quickSelect(nums, start, r, k);
        }else if(l <= k && end >= l){//同理
            return quickSelect(nums, l, end, k);
        }else{//这种情况就是l和r在最后相隔空了一个位置，而相隔空着的那么位置正好就是k
            return nums[k];
        }
        
    }
    
    //进行Shuffle的话可以有效避免worst case的产生
    private void shuffle(int[] nums){
        
        Random random = new Random();
        
        for(int i = nums.length - 1; i >= 0; i--){
            int randomIdx = random.nextInt(i + 1);
            int temp = nums[i];
            nums[i] = nums[randomIdx];
            nums[randomIdx] = temp;
        }
        
    }
}
```

参考:[九章 - Kth Largest Element In An Array](https://www.jiuzhang.com/solution/kth-smallest-numbers-in-unsorted-array/)

### 笔记

对该题的最全面的分析在[leetcode的讨论](https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/)中讲的很好，也完全就是面试中应该和面试官讨论的该题的利弊。
因为该题其实要做出来并不难，但是如何最有效，并且哪些方法有哪些方面的优势，其实才是关键。

那么说具体的讨论过程应该是怎样的呢？

1. 可以先说the most straight forward way is to sort, if we use **quick sort**, the average time complexity would be O(nlogn), in worst case it would be O(n^2)， if we use merge sort, guaranteed time complexity would be O(nlogn), but it would take O(n) extra space.

2. 然后再说，another way is to use **minHeap**(注意最大反而是用minHeap，另外如果是找第k小那就是相反用maxHeap), 这样可以guarantee time complexity降到O(nlogk), 空间复杂度降到O(k).

3. 再说，其实，如果只是找第k大，可以利用quick sort的partition过程，每次abandon没有用的一半。quick select，虽然worst case会是O(n^2),但是最佳情况会是O(n)时间。并且使用**shuflle**提前将array打乱后能有效避免worst case的发生。

4. 最后再提，记得当时在master上算法课的时候老师提过一种**median of median**的算法(其实叫[BFPRT](https://segmentfault.com/a/1190000008322873)，假装不知道)，然后说个大概思路应该就可以, 该算法可以保证O(n)的复杂度。估计最重会让写quick select的版本。

那么，在写quick select的时候有哪些需要注意的地方呢？

首先，和quick sort(quick sort的分析见自己笔记)相比，其实很多地方都是一模一样的，那么哪些地方需要注意以及哪些地方有不同？

1. quick sort没有返回值，而quick select是有返回值的。最终第k大的值会一层一层返回上去。另外要注意的是， quick select只能返回第k大的值，而不能返回其原坐标。(quick select的过程会打乱整个原数组的顺序，也没法返回坐标。如果硬要返回坐标，可以copy一份原数组，然后找到值之后再线性扫一遍？)

2. 触底的条件变成了if(start == end)而不是quick sort中的if(start >= end)，因为start > end的情况会被函数最后的判断条件过滤掉。

3. 注意最后判断的条件是本题的关键，舍弃没有必要查找的一部分，再另一部分中继续搜索，并且最后narrow到只有一个值的时候就可以肯定是第k大。其中，很容易弄错，并且要想清楚的两点是:
    * 当r == k && start <= r时并不表示就找到第r所在的元素就是第k大，因为所在的范围内是无序的，所以只能是肯定k会在该范围内，还需要继续narrow范围。
    * 最后的else情况其实就是当l和r指向了同一个元素，然后经过swap再l++,r--后交错空了1位，而正好k就是那1位的情况。这种情况下，是可以肯定第k大就是k所在的位置的元素的。

4. 另外注意其实因为数组排序是按升序排列的，所以其实如果要让找**第k小**的元素会比较好找。直接`return quickSelect(nums, 0, nums.length - 1, k - 1);`就行(注意是k - 1, 因为第k小其实是:在排好序的数组中下标为k-1的那个)， 而其实第k大不需要改动quickSelect函数，因为**第k大其实就是第(n - k + 1)小**的元素，再加上需要坐标左移一位，所以就是`quickSelect(nums, 0, nums.length - 1, nums.length - k);`

如果对于整个程序的运作不了解或者生疏了，可以手动跑一个case试试，这里推荐使用:

1 3 2 4 7 6 5

可以试着找第3小，第4小，第5小的元素。会分别落入quickselect函数中最后三种条件中。
