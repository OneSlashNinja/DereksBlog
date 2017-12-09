---
layout: post
title:  "leetcode 380 - Insert Delete Get Random O(1)"
date:   2017-12-05 00:06:02.028910
categories: leetcode, Google, Amazon, Facebook, Uber, Twitter, Yelp
---

# Insert Delete Get Random O(1)

## 一刷

### 代码

```java
class RandomizedSet {

    private static final int INI_CAPACITY = 8;
    
    private int[] arr;
    private int end;
    private HashMap<Integer, Integer> map;
    private Random rand;
    
    /** Initialize your data structure here. */
    public RandomizedSet() {
        this.arr = new int[INI_CAPACITY];
        this.end = 0;
        this.map = new HashMap<Integer, Integer>();
        this.rand = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(map.containsKey(val)){
            return false;
        }
        
        //数组如果满了，需要扩容
        if(end == arr.length){
            resizeArr(arr.length * 2);
        }
        
        arr[end] = val;
        map.put(val, end);
        end++;
        
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if(!map.containsKey(val)){//正好和insert相反
            return false;
        }
        
        //先调换位置，不仅要调换arr的位置，并且要把end的位置在map中也修改
        int currentIndex = map.get(val);
        int endVal = arr[end - 1];
        map.put(endVal, currentIndex);
        swap(currentIndex, end - 1);
        
        //然后arr中和map中都需要删除val
        map.remove(val);
        end--;
        
        //如果数组长度等于1 / 4了，则将长度缩为1 / 2
        if(end == arr.length / 4){
            resizeArr(arr.length / 2);
        }
        
        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        int randomIndex = rand.nextInt(end);
        return arr[randomIndex];
    }
    
    private void resizeArr(int capacity){
        int[] newArr = new int[capacity];
        for(int i = 0; i < end; i++){//注意end指向的是最后空白的位置，所以这里应该是 < end而不是 <= end
            newArr[i] = arr[i];
        }
        arr = newArr;
    }
    
    private void swap(int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

### 笔记

这题真是一道考察了非常多知识的题目。

首先，题目的要求是:
```
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
```

这三个操作都需要O(1)时间完成，前两个操作要O(1)其实没什么，但是getRandom则是这题的关键点。

* 如果只是要实现insert和remove并且要求O(1)时间完成，那么直接一个HashSet就行。但是getRandom要求**等概率**地输出一个元素，而HashSet是无序的，不能通过下标去获取一个元素，只能是暂存到一个额外的ArrayList中，这样的话，不仅需要额外空间，而且没有办法O(1)完成这个操作。

* 那么有了LRU和Register Class的经验，使用HashMap + DoubleLinkedList是否能够完成这项任务呢? 
还是不行，因为链表同样无法O(1)时间通过下标来找到某个元素，HashMap也帮不上忙。

* 所以，为了满足O(1)时间能够通过下标直接获取到相应元素这个性质，肯定是需要array，然后再加上需要insert和remove也能O(1)时间完成的要求，肯定同样需要配合HashMap。
但是问题在于，使用array的remove，如何使得被处理空出来的位置能够填补上，否则getRandom时，是有可能会定位到一个被删除了元素的下标的?并且如果不填充上空缺位置，如何知道该位置是空缺，即使使用有额外标志位的class，那么利用率也不高啊？

思考到这里就是本题的核心技巧了:
**首先，维护一个end指针，指向数组的末尾先一个要填充的位置，因为和Class Register中正好相反，本题中并不要求顺序，所以可以利用这里点，对于删除，直接将end-1位置的元素换到删除的位置上，然后end--就相当于删除了**

这样，最后getRandom就只需要生成一个范围是[0, end)的随机数，然后O(1)时间就能够获取到该元素。



解决了这个问题，还有一个问题需要解决。因为本题并没有提元素的多少有什么上限，所以我们需要一个有伸缩性质的存储。而这正是array的弊端，array必须制定固定的长度。
题解中"偷懒"的做法是使用ArrayList，但是个人感觉使用ArrayList并不地道，像上面提到的置换并end--就没法完美体现。

所以，自己动手，丰衣足食！直接使用array，配合resize。(这样的话还能顺便让面试官知道你了解resize的技巧)

这里resize的技巧是:
对于grow array，是**当数组满了的时候则倍增**，而对于shrink，**则是当元素减少到原来的1 / 4的时候，再将数组所谓原长度的1 / 2**。这是为了防止**thrashing**，也就是在临界点上增,删,增,删,增,删..., 这样数组的长度就会一直变化，而因为每次增加长度和减小长度都需要遍历并且copy，会浪费大量时间和空间。

具体参考**PrincetonAlgorithm part I的4 - 2章节: 4 - 2 - Resizing Arrays (9-56)**
