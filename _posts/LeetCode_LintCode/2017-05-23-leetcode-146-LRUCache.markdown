---
layout: post
title:  "LeetCode # - "
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
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

```java
public class LRUCache {

    //注意不是public class
    class DoubleListNode{
        //一开始以为只需要val的信息就够了
        //因为removeNodeFromHead方法需要通过node能够找到key，而map没有办法反推出key
        public int key;
        public int val;
        public DoubleListNode left;
        public DoubleListNode right;
        
        public DoubleListNode(int key, int val){
            this.key = key;
            this.val = val;
        }
    }

    private int capacity;
    private HashMap<Integer, DoubleListNode> map;
    private DoubleListNode head;
    private DoubleListNode tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<Integer, DoubleListNode>();
        //首先head和tail需要是指向两个实体的dummy node，
        //原因和设置dummy node是一样的，就是因为最头和最尾的两个元素也是可能被操作的
        //而且也不用担心这两个dummy node中的key会和真正的key为-1的情况冲突，因为这两个node是不会出现在map中的，所以不会被定位到
        this.head = new DoubleListNode(-1, -1);
        this.tail = new DoubleListNode(-1, -1);
        //并且要将他们连接起来
        //head<-->tail
        this.head.right = tail;
        this.tail.left = head;
    }
    
    //这种操作必须想象图形或者画出来
    private void moveNodeToTail(DoubleListNode target){
        tail.left.right = target;
        target.left = tail.left;
        tail.left = target;
        target.right = tail;
    }
    
    private void addNodeToTail(int key, int val){
        DoubleListNode newNode = new DoubleListNode(key, val);
        map.put(key, newNode);
        
        moveNodeToTail(newNode);
    }
    
    private void removeNodeFromHead(){
        DoubleListNode abandonedNode = head.right;
        map.remove(abandonedNode.key);
        
        head.right = abandonedNode.right;
        abandonedNode.right.left = head;
    }
    
    public int get(int key) {
        //if key not in the map, then return -1
        if(!map.containsKey(key)){
            return -1;
        }
        
        //or you need to move the element to the most front
        DoubleListNode target = map.get(key);
        
        //先把target从原来的位置"取出来"
        target.left.right = target.right;
        target.right.left = target.left;
        //然后粘到tail的位置
        moveNodeToTail(target);
        
        return target.val;
    }
    
    public void put(int key, int value) {
        //这个if也可以利用已经有的get方法，从而达到简化
        // if(map.containsKey(key)){
        //     //update the value
        //     map.get(key).val = value;
            
        //     //then move the node to most front
        //     DoubleListNode target = map.get(key);
        //     target.left.right = target.right;
        //     target.right.left = target.left;
        //     moveNodeToFront();
        if(get(key) != -1){ //如果不等于-1，那get方法会直接帮助移动到最前端
            map.get(key).val = value;
        }else{
            //以下这段代码可以简化
            // if(map.size() < capacity){
            //     //add the node to most front
            //     addNodeToFront(key, value);
            // }else{
            //     //remove the 
            //     removeNodeFromTail();
                
            //     //add the node to most front
            //     addNodeToFront(key, value);
            // }
            
            if(map.size() == capacity){
                removeNodeFromHead();
            }
            addNodeToTail(key, value);
            
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```


### 笔记

(1)感觉其实这题抽象出方法的层级很重要。一些可以复用的操作写成子方法，不仅可以是的代码更简洁，更易读，并且也更容易维护。

(2)DoubleListNode中需要key的信息，因为removeNodeFromHead方法需要通过node能够找到key，而map没有办法反推出key。

(3)head和tail到底谁在左谁在右，谁指向最新的谁指向最旧的，要在一开始就规定好。本题中，head在左tail在右，tail指向最新的，head指向最旧的。

(4)head和tail都需要在一开始指向一个辅助node，原因和使用dummy node一样，就是需要一个不会被程序挪动的"标杆"

(5)在put操作中，利用自定义的get操作来代替map.get()操作非常巧妙，这样就可以利用map.get()会帮助调整target到目标位置，从而省去很多重复的操作了。