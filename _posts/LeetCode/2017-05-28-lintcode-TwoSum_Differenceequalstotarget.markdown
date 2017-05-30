---
layout: post
title:  "LintCode - Two Sum - Difference equals to target"
date:   2017-05-28 00:23:02 -0400
categories: lintcode, Amazon
---

# Title

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

sort1
```java
public class Solution {
    /*
     * @param nums an array of Integer
     * @param target an integer
     * @return [index1 + 1, index2 + 1] (index1 < index2)
     */
     
    class NumberNode{
        public int value;
        public int index;
        
        public NumberNode(int value, int index){
            this.value = value;
            this.index = index;
        }
    }
     
    public int[] twoSum7(int[] nums, int target) {
        // write your code here
        
        int[] result = new int[]{-1, -1};
        
        if(nums == null || nums.length < 2){
            return result;
        }
        
        NumberNode[] nodeArr = new NumberNode[nums.length];
        for(int i = 0; i < nums.length; i++){
            nodeArr[i] = new NumberNode(nums[i], i);
        }
        
        Arrays.sort(nodeArr, new Comparator<NumberNode>(){
            public int compare(NumberNode n1, NumberNode n2){
                return n1.value - n2.value;
            }
        });
        
        int i = 0, j = i + 1;
        
        //因为某个difference和sum还不一样
        //加法两个加数调换位置不会影响结果，而减法则会影响结果
        //difference = minuend(减数) - subtractor(被减数)
        //或者-difference = subtractor(被减数) - minuend(减数)
        //所以在排好序后的数组，当target是负数时，则其实需要i和j调换顺序，但其实可以利用上面的交换来将target变换一下，使得依然target > 0, 这样依然能够遵循j > i的情况。
        if(target < 0){
            target = -target;
        }
        
        while(j < nodeArr.length){
            
            //这一个条件很重要，第一印象感觉应该循环中i < j， 如果i == j了就应该跳出或者说停止循环
            //但是如果考虑像排好序后[0, 3, 4], target = 1，那么当程序跑到i = j = 1，也就是都指向3的时候就会跳出循环
            //但其实我们知道结果是4 - 3 = 1,这是为什么呢
            //这是因为我们虽然排好了序，但是数字和数字之间的间隔是并没有排好序的，比如[0, 3, 4]
            //这样就使得我们虽然知道在当i指向0,j指向3的时候diff为3，应该向右移动i，但是我们没法肯定在后面的某个区间，i和j的diff不会更小
            //所以，当i == j的时候，我们不能直接就结束循环，而是应该让i把j顶向下一个位置，这样就能够使得i和j试到所有有可能的组合而不会忽略一种的一些
            if(i == j){
                j++;
            }
            
            int diff = nodeArr[j].value - nodeArr[i].value;
            if(diff == target){
                //+1是因为题目要求下标以1位底
                result[0] = Math.min(nodeArr[j].index, nodeArr[i].index) + 1;
                result[1] = Math.max(nodeArr[j].index, nodeArr[i].index) + 1;
                return result;
            }
            
            if(diff < target){
                j++;
            }else{
                i++;
            }
        }
        
        return result;
        
    }
}
```

sort2
```java
public class Solution {
    /*
     * @param nums an array of Integer
     * @param target an integer
     * @return [index1 + 1, index2 + 1] (index1 < index2)
     */
     
    class NumberNode{
        public int value;
        public int index;
        
        public NumberNode(int value, int index){
            this.value = value;
            this.index = index;
        }
    }
     
    public int[] twoSum7(int[] nums, int target) {
        // write your code here
        
        int[] result = new int[]{-1, -1};
        
        if(nums == null || nums.length < 2){
            return result;
        }
        
        NumberNode[] nodeArr = new NumberNode[nums.length];
        for(int i = 0; i < nums.length; i++){
            nodeArr[i] = new NumberNode(nums[i], i);
        }
        
        Arrays.sort(nodeArr, new Comparator<NumberNode>(){
            public int compare(NumberNode n1, NumberNode n2){
                return n1.value - n2.value;
            }
        });
        
        int i = 0, j = 0;
        
        while(j < nodeArr.length && i < nodeArr.length){
            
            int diff = nodeArr[j].value - nodeArr[i].value;
            if(diff == target){
                //i和j在比较的过程中可能会重合，这对于i和j在竞赛的过程来说是必要的
                //但是对于diff == target的情况，i和j则不可以是同一个元素(这种情况下只可能有两个相同的元素出现)，所以在这种情况下，需要使用j++来把两个数碰开
                if(i == j){
                    j++;
                    continue;
                }
                //+1是因为题目要求下标以1位底
                result[0] = Math.min(nodeArr[j].index, nodeArr[i].index) + 1;
                result[1] = Math.max(nodeArr[j].index, nodeArr[i].index) + 1;
                return result;
            }
            
            if(diff < target){
                j++;
            }else{
                i++;
            }
        }
        
        return result;
        
    }
}
```

```java
public class Solution {
    /*
     * @param nums an array of Integer
     * @param target an integer
     * @return [index1 + 1, index2 + 1] (index1 < index2)
     */
     
     
    public int[] twoSum7(int[] nums, int target) {
        // write your code here
        
        int[] result = helper(nums, target);
        if(result[0] == -1 && result[1] == -1){
            result = helper(nums, -target);
        }
        
        return result;
    }
    
    private int[] helper(int[] nums, int target) {
        // write your code here
        
        int[] result = new int[]{-1, -1};
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++){
            //注意 a - b = target => a - target = b
            //所以这里是nums[i] - target而不是target - nums[i]
            //另外注意这里也可以换成
            //if(map.containsKey(nums[i])){
            //    result[0] = map.get(nums[i]) + 1;
            //    result[1] = i + 1;
            //    return result;
            //}
            //map.put(nums[i] - target, i);
            //这是因为当target变成-target时，效果是一样的
            if(map.containsKey(nums[i] - target)){
                result[0] = map.get(nums[i] - target) + 1;
                result[1] = i + 1;
                return result;
            }
            
            map.put(nums[i], i);
        }
        
        return result;
    }
}
```

### 笔记

这题的解题方法的最基本的思路和基础的two sum是基本一样的，也可以用sort后双指针或者是HashMap的方法，但是因为减法中减数和被减数的顺序不可调换，所以细节上会有蛮多不同:

1. 对于sort+双指针的方法要注意:
(1)和two sum一样，因为sort时候会丢失原始的下标，所以需要创建一个额外的数据结构来存储这种对应关系。注意comparator的写法。
(2)因为是减法的顺序，我们要确定到底谁是减数，谁是被减数，所以我们可以假设target肯定为 >= 0, 因为如果a - b = target < 0, 我们可以设法找出b - a = target >= 0
(3)在普通的two sum的双指针方法中，一头一尾两个指针，< target了就向右移动在头的指针， > target了就向左移动在尾的指针，方向很明确。但是在two diff中，如果我们也用一头一尾两个指针，基于(1)中给出的假设(target >= 0)，我们把被减数i放在头上，把被减数j放在尾上，那么j - i < target其实就可以有两种移动方法，既可以向左移动i，也可以向右移动j，所以是没法控制的。因此我们需要将两个指针都设置在头上，这样一来，当j - i < target时就右移j，当j - i > target时就左移i。

关于sort1和sort2的其他注意的地方具体solution

sort1和sort2的区别在于:
(1)第一种解法相当于规定,当a - b = target < 0的情况，则直接把它变成b - a = target > 0的情况，因为结果要求返回的顺序是这样有助于我们确定减数肯定大于等于被减数。

sort2来说更易懂，并且如果题目要求返回的不是基于大小顺序，而是[减数,被减数]或者[被减数,减数]的关系，则sort2更直接，而sort1还要根据原始的target是否>0来判断最后两个数的返回顺序。

2. 这题也可以使用HashMap的方法，不过同样因为到底谁作为减数，谁作为被减数的问题，所以需要试两边，一遍以target作为target，一遍以-target作为target。