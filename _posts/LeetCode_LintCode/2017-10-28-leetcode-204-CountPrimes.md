---
layout: post
title:  "leetcode 204 - Count Primes"
date:   2017-10-28 22:00:53.868624
categories: leetcode, Microsoft,
---

# CountPrimes

## 一刷

### 代码

coupling的暴力法，会TLE
```java
class Solution {
    public int countPrimes(int n) {
        
        int count = 0;
        
        for(int i = 2; i < n; i++){
            for(int j = 2; j <= i; j++){
                
                if(i == j){
                    count++;
                }
                
                if(i % j == 0){
                    break;
                }
                
            }
        }
        
        return count;
    }
}
```

解耦，将isPrime提取出来的方法，结构清晰，但是还是会TLE,卡在499979
```java
class Solution {
    public int countPrimes(int n) {
        int count = 0;
        
        if(n <= 1){
            return count;
        }
        
        for(int i = 2; i < n; i++){
            if(isPrime(i)){
                count++;
            }
        }
        
        return count;
    }
    
    private boolean isPrime(int num){
        
        for(int i = 2; i < num; i++){
            if(num % i == 0){
                return false;
            }
        }
        
        return true;
    }
}
```

稍微优化的剪枝，不过提升不大，仍然TLE,卡在499979
```java
class Solution {
    public int countPrimes(int n) {
        int count = 0;
        
        if(n <= 1){
            return count;
        }
        
        for(int i = 2; i < n; i++){
            if(isPrime(i)){
                count++;
            }
        }
        
        return count;
    }
    
    private boolean isPrime(int num){
        
        for(int i = 2; i <= num / 2; i++){
            if(num % i == 0){
                return false;
            }
        }
        
        return true;
    }
}
```

再进一步优化，可达到O(n^1.5),仍旧TLE，不过这回卡在1500000的版本
```java
class Solution {
    public int countPrimes(int n) {
        int count = 0;
        
        if(n <= 1){
            return count;
        }
        
        for(int i = 2; i < n; i++){
            if(isPrime(i)){
                count++;
            }
        }
        
        return count;
    }
    
    private boolean isPrime(int num){
        
        for(int i = 2; i * i<= num; i++){
            if(num % i == 0){
                return false;
            }
        }
        
        return true;
    }
}
```

埃拉托斯特尼筛法Sieve of Eratosthenes
```java
class Solution {
    public int countPrimes(int n) {
        
        //input validation
        if(n <= 1){
            return 0;
        }
        
        //题目中说的是小于n的数中，按理说应该new boolean[n - 1]。
        //但是抛除0,剩下的数刚好n - 1个，并且不用管和下标对应，更方便
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        
        //这两个值虽然计算中不会用，但是最后统计的时候会用到
        isPrime[0] = false;
        isPrime[1] = false;
        
        //起点是2, 终点是sqrt(n), 每次递增
        for(int i = 2; i * i < n; i++){
            //如果该数字本身就不是prime，就没必要检查了，肯定会被其他的某个case覆盖
            if(isPrime[i]){
                //注意j的起点是i * i, 每次递增i而不是i
                for(int j = i * i; j < n; j += i){
                    isPrime[j] = false;
                }
            }
        }
        
        int count = 0;
        for(int i = 0; i < isPrime.length; i++){
            if(isPrime[i]){
                count++;
            }
        }
        
        return count;
    }
}
```

### 笔记

这题也是一道有很多知识点或者说思考点的题目。总共写了5个版本，虽然每个版本都是正确的，但是明显可以看出一个进化的过程。

1. 
第一个版本耦合性比较大，只能适用于: 
    * 从1到n哪些数是prime?
    * 从1到n的prime有多少个?

而不能具体地测试某个数是不是prime。

2. 
版本2则将isPrime单独剥离出来作为一个函数，这样程序的可复用性，可读性，可维护性就大大增加了。
但是复杂度完全没有变

3. 
> As we know the number must not be divisible by any number > n / 2, we can immediately cut the total iterations half by dividing only up to n / 2. Could we still do better?

**对于一个数n，肯定是不会被从n / 2 ~ n这个范围的数整除的，所以对于isPrime这个方法也就没有必要检查这个区间了。**

这可以稍微优化一点版本2，但是基本不会有太大提升

4. 
对于一个非prime的数，比如16，除了4 * 4以外，一对除数中肯定会有一个大的，一个小的，比如 2 * 8， 那么检测2 * 8和检测8 * 2肯定是一样的，也就是说
**对于一个非prime的数n，以sqrt(n)为分界线，如果从2到sqrt(n)中都没有除数，那么从sqrt(n)到n肯定也不会有**，所以可以把上限再次变为`i * i<= num;`

这次算法时间复杂度从O(n^2)降低到了O(n^1.5)，不过仍然会TLE。

但如果只考虑isPrime这个方法本身，其实复杂度已经提升到极限了。下面的埃拉托斯特尼筛法Sieve of Eratosthenes则属于只针对要计算从1到n的prime个数的特殊情况，并且以牺牲空间作为代价的。

5. 
就像上面说的如果本题空间复杂度要求O(1)，那么上面的版本应该已经是最优了。埃拉托斯特尼筛法Sieve of Eratosthenes这种方法算是用空间换时间的版本。

其实思路很简单:

> 我们从2开始遍历到根号n，先找到第一个质数2，然后将其所有的倍数全部标记出来，然后到下一个质数3，标记其所有倍数，一次类推，直到根号n，此时数组中未被标记的数字就是质数。我们需要一个n-1长度的bool型数组来记录每个数字是否被标记，长度为n-1的原因是题目说是小于n的质数个数，并不包括n。

题目由两层循环来依次填充这个Boolean数组。**外层循环加上isPrime的判断是用来选定用来作为倍增的数字的，内层循环则是倍增并且mark非prime的过程**

注意外层循环的终止条件和内层循环的起始条件。外层循环终止条件是i * i < n, 而内层则是以j = i * i作为开始。

外层循环的终止条件是i * i < n的原因是:
**大于sqrt(n)的非prime，肯定会被小于sqrt(n)的情况覆盖**
比如找25内的prime，i的上限为5，那么7的情况呢？7自己本身在初始的时候就是prime，而2 * 7则会被2倍增的情况覆盖。

而内层循环终止的其实条件是i * i的原因是**i * i之前的情况会被i之前的数字所覆盖**，比如i为5时，i*i=25,那么是从25，30，35开始倍增。那么之前的5的倍数呢？4 * 5会被4的倍数的时候覆盖，3 * 5会被3的倍数的时候覆盖, 2 * 5会被2的倍增的时候覆盖。

### 参考
[Grandyang - [LeetCode] Count Primes 质数的个数](http://www.cnblogs.com/grandyang/p/4462810.html)
[Leetcode 8个循序渐进的提示](https://leetcode.com/problems/count-primes/hints/)