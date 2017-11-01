---
layout: post
title:  "lintcode 227 - Mock Hanoi Tower By Stacks"
date:   2017-10-29 00:59:17.970950
categories: lintcode, VMware
---

# Mock Hanoi Tower By Stacks

## 一刷

### 代码

```java
public class Tower {
    private Stack<Integer> disks;
    /*
    * @param i: An integer from 0 to 2
    */
    public Tower(int i) {
        // create three towers
        this.disks = new Stack<Integer>();
    }

    /*
     * @param d: An integer
     * @return: nothing
     */
    public void add(int d) {
        // Add a disk into this tower
        if (!disks.isEmpty() && disks.peek() <= d) {
            System.out.println("Error placing disk " + d);
        } else {
            disks.push(d);
        }
    }

    /*
     * @param t: a tower
     * @return: nothing
     */
    public void moveTopTo(Tower t) {
        // Write your code here
        if(t.disks.size() != 0 && t.disks.peek() < this.disks.peek()){
            System.out.println("Error Moving");
            return;
        }
        t.add(this.disks.pop());
    }

    /*
     * @param n: An integer
     * @param destination: a tower
     * @param buffer: a tower
     * @return: nothing
     */
    public void moveDisks(int n, Tower destination, Tower buffer) {
        // Move n Disks from this tower to destination by buffer tower
        
        //也能工作的版本
        // if(n == 1){
        //     moveTopTo(destination);
        //     //一定要注意触底的return
        //     return;
        // }

        if(n == 0){
            return;
        }
        
        moveDisks(n - 1, buffer, destination);
        moveTopTo(destination);
        buffer.moveDisks(n - 1, destination, this);
        
    }

    /*
     * @return: Disks
     */
    public Stack<Integer> getDisks() {
        // write your code here
        return disks;
    }
}

/**
 * Your Tower object will be instantiated and called as such:
 * Tower[] towers = new Tower[3];   
 * for (int i = 0; i < 3; i++) towers[i] = new Tower(i);
 * for (int i = n - 1; i >= 0; i--) towers[0].add(i);   
 * towers[0].moveDisks(n, towers[2], towers[1]);
 * print towers[0], towers[1], towers[2]
*/
```

### 笔记

蛮有意思的的一题，想起小时候在文曲星上玩的汉诺塔游戏了。经过自己的思考后，没看题解也写出来了。

其实本题本身给的基本结构就让人豁然开朗了不少，Tower的基础结构应该是Stack，能非常形象地体现先进后出的特点。
并且也明白了Tower应该有怎样的操作，Tower和Tower之间的互动是怎么样。


1. 注意构造函数中的参数`int i`似乎完全没什么用，就是迷惑性质的？

2. 最后的getDisks方法应该是为了OJ判断用的，对于我们自己没什么用。

3. moveTopTo方法就是稍微需要做点check，没什么亮点

所以，其实整个数据结构中，最精华的就是moveDisks这个方法了。
这个方法的参数也很巧妙，给了非常多的提示。

一开始还以为跟n的奇偶有关系，就像小时候自己玩的时候考虑的(说不定使用递推而不是递归会能做?)。

但是在纸上画了画就发现，其实肯定是递归的思想，也就是说整个过程肯定是，

**通过之前一系列的递归操作，能够将前n-1个disk先移动到buff区，然后再将最后一个disk移动到目的地，然后再通过一系列的递归将buff区的disk移动到目的地。**

**由于要把前n-1个先挪到buff区，所以递归调用的时候buff取和destination区会掉个个。**

一开始觉得整个递归的终止条件应该是当n==1的时候，就直接移动到目的地即可。其实也是可以work的。

但是看了别人题解后发现，其实只考虑n == 0的情况，进行返回后，n == 1的情况是会被覆盖的。
