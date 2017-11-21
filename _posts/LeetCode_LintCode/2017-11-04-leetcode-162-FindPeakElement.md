---
layout: post
title:  "leetcode 162 - Find Peak Element"
date:   2017-11-04 10:37:41.162678
categories: leetcode, Google, Microsoft
---

# FindPeakElement

## 一刷

### 代码

第一次刷lintcode的版本
```java
class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        
        if(A == null || A.length == 0){
            return -1;
        }
        
        int start = 0, end = A.length - 1;
        int mid;
        
        while(start + 1 < end){
            mid = start + (end - start) / 2;
            
            if(A[mid] > A[mid - 1] && A[mid] > A[mid + 1]){
                return mid;
            }else if(A[mid] < A[mid - 1]){
                end = mid;
            }else{
                start = mid;
            }
            
        }
        
        if(A[start] > A[start - 1] && A[start] > A[start + 1]){
            return start;
        }
        
        if(A[end] > A[end - 1] && A[end] > A[end + 1]){
            return end;
        }
        
        return -1;
    }
}

```

## 二刷

leetcode
```java
class Solution {
    public int findPeakElement(int[] nums) {
        if(nums == null || nums.length == 0){
            return -1;
        }
        
        int l = 0, r = nums.length - 1;
        
        while(l < r){
            int mid = l + (r - l) / 2;
            
            //因为l < r的条件限制，这里即使是[1]这样的数组，mid+1也不会越界
            //另外，本题中因为说了peak只有一个，所以等号写在哪边也都无所谓
            if(nums[mid] >= nums[mid + 1]){
                r = mid;
            }else{
                //这里是mid + 1,你懂
                l = mid + 1;
            }
        }
        
        return l;
    }
}
```

### 笔记


这题一刷二刷的不同就看出了沧海桑田，在明白了binary search的三种form后，就可以任意挑选趁手的来进行相应的search了。

对于这道题，因为只是锁定一个点，并且说了只需要找到一个peak就行，并且相邻的两个元素肯定不等。那么找该元素就可以使用binary search中锁定一点的版本。

注意:

1. 判断的条件是**nums[mid] >= nums[mid + 1]**, 和普通的搜索不太一样，并不是找明确的target

2. 因为不会有相等的peak，所以等号在哪儿并没有关系

3. 注意该版本r = mid, l = mid + 1

4. 因为l和r不会重合，所以使用nums[mid + 1]并不会有越界的危险

5. 使用l和r作为start和end的缩写能剩不少时间，尤其是在白板上