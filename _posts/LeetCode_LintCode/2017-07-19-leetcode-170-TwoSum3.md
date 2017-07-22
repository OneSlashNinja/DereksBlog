---
layout: post
title:  "leetcode 170 - TwoSum3"
date:   2017-07-19 00:15:40.965473
categories: leetcode, Linkedin
---

# TwoSum3

## 一刷

### 代码

击败%99.15的版本，但是换成LinkedList却有超时
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

### 笔记

2 sum非常适合用HashMap，即使是这种数据结构的follow up。但是3 sum一下就不能用了，所以自己写的版本很可能对于3 sum有较好的拓展性。
