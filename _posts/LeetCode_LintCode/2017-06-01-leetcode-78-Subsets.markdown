---
layout: post
title:  "LeetCode 78 - Subsets"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Subsets

## 一刷

### 代码

Backtracking version
```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsets(int[] nums) {
        // write your code here
        if(nums == null || nums.length == 0){
            return null;
        }
        
        Arrays.sort(nums);
        
        ArrayList<ArrayList<Integer>> results = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        subsetsHelper(results, list, nums, 0);
        
        return results;
    }
    
    private void subsetsHelper(ArrayList<ArrayList<Integer>> results, 
                                ArrayList<Integer> list, int[] nums, int depth){
        results.add(new ArrayList<Integer>(list));
        
        for(int i = depth; i < nums.length; i++){
            list.add(nums[i]);
            subsetsHelper(results, list, nums, i + 1);
            list.remove(list.size() - 1);
        }
    }
}
```

### 笔记

这道题一看题目“return all possible...”就是需要搜索所有可行的解，所以应该使用Backtracking(也就是DFS+recursion)。

另外本题有个位操作的版本也值得日后研究下。


其他注意点：
(1)results.add(new ArrayList<Integer>(list));
首先，不能直接results.add(list);这样会产生shallow copy的问题。
最后会把很多个list这个reference的副本添加进results，而且随着程序的进行list一直是在改变的。
而我们需要的是deep coy，所以需要new一个新的空间，而注意这里的使用方法，相当于先new一个ArrayList然后从list中一个一个copy到新的ArrayList的简写。

在Java的ArrayList的构造函数中，有一个Constructor

ArrayList(Collection<? extends E> c)
Constructs a list containing the elements of the specified collection, in the order they are returned by the collection's iterator.

(2)list.remove(list.size() - 1);
不能写成list.remove(nums[i]);
查Java的API知道：
remove(int index)
Removes the element at the specified position in this list.
remove中的参数是list中要被remove元素的index，而不是具体值(想想也知道，可能有duplicate会在不同的index)。而该题中我们知道，在这三行：
list.add(nums[i]);
subsetsHelper(results, list, nums, i + 1);
list.remove(list.size() - 1);
中，不管subsetsHelper经过了怎样的深入，list最后还是会回溯到刚刚list.add(nums[i]);后的状态，所以nums[i]肯定是在最后一个index，也即是list.size() - 1

(3)subsetsHelper(results, list, nums, i + 1);
其实最后一个参数不应该叫depth,如果是depth那么应该每深一层次的递归，就会depth + 1(也的确在这里写错了。)
而实际是赋的i + 1而不是depth + 1;
所以实际上最后一个参数表示的是下界。

---

## 二刷

### 代码

```java
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        if(nums == null || nums.length == 0){
            return results;
        }
        
        List<Integer> currentList = new ArrayList<Integer>();
        
        backtrackingHelper(results, currentList, 0, nums);
        
        return results;
    }
    
    private void backtrackingHelper(List<List<Integer>> results, List<Integer> currentList, int currentIndex, int[] nums){
        //不需要条件就可以将currentList加入到结果集中
        results.add(new ArrayList<Integer>(currentList));
        
        for(int i = currentIndex; i < nums.length; i++){
            currentList.add(nums[i]);
            backtrackingHelper(results, currentList, i + 1, nums);
            currentList.remove(currentList.size() - 1);
        }
        
    }
}
```


### 笔记

一开始有点忘了怎么写这题的Backtracking了，因为结果中的各个list长度都不一定相同，然后就在纸上手动演算了下过程，就明白了。

其实backtracking属于traverse的思想，**需要老大臣(backtracking方法)拿着小本子(各种传参的参数)来记录**。

subsets的Backtracking有以下特点:
(1)不需要达到特定的条件(比如长度需要和nums的长度一致)，所以在Backtracking的中不需要一开始指定条件就可以将当前
(2)需要利用一个currentIndex来知道当前traverse到能取哪些元素了。

其实backtrack最核心的思想就是有去一定要有回，所以在backtrack的方法中，对于像该题中的currentList，一定会是:
```java
//先加进去
currentList.add(nums[i]);
//再recursion
backtrackingHelper(results, currentList, i + 1, nums);
//然后再移除
currentList.remove(currentList.size() - 1);
```
这样的结构

leetcode上有一篇总结的很好的关于backtrack的模板：<https://discuss.leetcode.com/topic/46159/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning>

