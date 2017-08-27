---
layout: post
title:  "leetcode 170 - TwoSum3"
date:   2017-07-19 00:15:40.965473
categories: leetcode, Linkedin
---

# TwoSum3

## 一刷

### 代码

击败%99.15的版本，但是换成LinkedList却又超时
```java
public class TwoSum {

    private ArrayList<Integer> sortedList;
    
    /** Initialize your data structure here. */
    public TwoSum() {
        sortedList = new ArrayList<>();
    }
    
    private int findInsertPosition(int elem){
        int start = 0, end = sortedList.size() - 1;
        
        while(start + 1 < end){
            //mid写在循环里
            int mid = start + (end - start) / 2;
            int value = sortedList.get(mid);
            if(elem <= value){
                end = mid;
            }else{
                start = mid;
            }
        }
        
        if(start >= sortedList.size() || sortedList.get(start) >= elem){
            return start;
        }
        
        if(end >= sortedList.size() || sortedList.get(end) >= elem){
            return end;
        }
        
        return end + 1;
    }
    
    /** Add the number to an internal data structure.. */
    public void add(int number) {
        int insertIndex = findInsertPosition(number);
        sortedList.add(insertIndex, number);
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(int value) {
        
        int i = 0, j = sortedList.size() - 1;
        while(i < j){
            int sum = sortedList.get(i) + sortedList.get(j);
            if(sum == value){
                return true;
            }else if(sum > value){
                j--;
            }else{
                i++;
            }
        }
        
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */
```


```java
public class TwoSum {

    private HashMap<Integer, Integer> map;
    
    /** Initialize your data structure here. */
    public TwoSum() {
        map = new HashMap<>();
    }
    
    /** Add the number to an internal data structure.. */
    public void add(int number) {
        if(!map.containsKey(number)){
            map.put(number, 1);
        }else{
            map.put(number, map.get(number) + 1);
        }
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(int value) {
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int i = entry.getKey();
            int j = value - i;
            if((i == j && map.get(i) > 1) || (i != j && map.containsKey(j))){
                return true;
            }
            
        }
        
        return false;
    }
}

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */
```

### 笔记

2 sum非常适合用HashMap，即使是这种数据结构的follow up。但是3 sum一下就不能用了，所以自己写的版本很可能对于3 sum有较好的拓展性。

自己的思路是，使用类似插入排序的方式，使得无论怎么add(而且因为之前的都是有序的，所以插入可以选择二分搜索)，都维护一个有序的数组，然后使用双指针的方法来判断2 sum。

但是自己的这个版本的一个问题是，如果使用ArrayList，insert会有O(n)的操作，而如果选择LinkedList, 则insert虽然是O(1)的，但是双指针的时候，后面指针从后往前走则会每次get都需要O(n)时间。

试验的结果是使用ArrayList能击败99.15%的人，但是使用LinkedList则会超时，可能是因为get使用的远远大于add。

总之，如果使用ArrayList的版本，那么add是O(n)的时间(O(logn)搜索 + O(n)插入)，find是O(n)时间。

而且，自己的这种解法更有优势的一点在于，**如果find需要返回的是具体的两个数的index而不只是Boolean，那么HashMap的版本就做不了,自己的这个版本通过增加wrap类应该是可以做的**


该题还是可以使用HashMap的，但是要注意，因为此题只问有没有组合，而不需要具体的index。所以虽然仍然是HashMap<Integer, Integer>,
但是第二个Integer并不再是Index，而是某个num出现的次数。

add操作直接把数字放入HashMap中(注意这样的话，会失去具体加进来数字的index信息)

find操作遍历整个HashMap，确定其中一个数看另一个数是否在HashMap中(需要注意有可能会有两个数相等的情况，这时HashMap的value就能排上用处了，否则如果规定相加的两个数一定不相等的话，其实HashSet都能做)。

这种解法的时间复杂度是:add为近似O(1),find为近似O(n)

但是HashMap的操作都是近似O(1)，所以自己的版本虽然似乎在add上看Big O会慢一点，但实际速度却快过HashMap。
