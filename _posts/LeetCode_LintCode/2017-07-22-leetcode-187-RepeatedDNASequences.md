---
layout: post
title:  "leetcode 187 - Repeated DNA Sequences"
date:   2017-07-22 23:48:26.928790
categories: leetcode, Linkedin
---

# Repeated DNA Sequences

## 一刷

### 代码

HashMap版
```java
public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {

        List<String> results = new ArrayList<>();

        if(s == null || s.length() <= 10){
            return results;
        }

        HashMap<String, Integer> map = new HashMap<>();

        for(int i = 0; i < s.length() - 10 + 1; i++){
            String subStr = s.substring(i, i + 10);
            if(!map.containsKey(subStr)){
                map.put(subStr, 1);
            }else{
                if(map.get(subStr) == 1){
                    results.add(subStr);
                }
                map.put(subStr, map.get(subStr) + 1);
            }
        }

        return results;
    }
}
```

HashSet代替HashMap简化版
```java
public List<String> findRepeatedDnaSequences(String s) {
    Set seen = new HashSet(), repeated = new HashSet();
    for (int i = 0; i + 9 < s.length(); i++) {
        String ten = s.substring(i, i + 10);
        if (!seen.add(ten))
            repeated.add(ten);
    }
    return new ArrayList(repeated);
}
```

Bit Manipulation
```java
public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        
        List<String> results = new ArrayList<>();
        
        if(s == null || s.length() == 0){
            return results;
        }
        
        int[] map = new int[26];
        map['A' - 'A'] = 0;
        map['C' - 'A'] = 1;
        map['G' - 'A'] = 2;
        map['T' - 'A'] = 3;
        
        HashSet<Integer> seen = new HashSet<>();
        HashSet<Integer> repeated = new HashSet<>();
        
        for(int i = 0; i + 9 < s.length(); i++){
            int hash = 0;
            
            for(int j = i; j < i + 10; j++){
                hash <<= 2; //hash = hash << 2
                //对于像0...1000 和 0...0011这里 += 和 |= 都是一样的效果
                hash += map[s.charAt(j) - 'A'];
            }
            
            if(!seen.add(hash) && repeated.add(hash)){
                results.add(s.substring(i, i + 10));
            }
            
        }
        
        return results;
    }
}
```

### 笔记

自己的思路很简单，每次截取10个字符的子字符串作为key存到到HashMap中，然后看之前是不是已经存在这样的key了，如果存在并且只存在了一次，那么说明是一个*还没有加入的*重复序列，所以将其加入到结果集中。

即使是最简单的实现中，其实也要注意几个地方：

for循环中，结束条件并不是i + 10 < s.length(),这是因为i自己其实就占了10个字符中的一个，所以应该是i + 10 - 1 < s.length().

同样的道理，虽然java的String中的substring(i,j)是取的[i,j)，但是由于取的应该是从i开始的10个数，所以应该是substring(i, i + 11 - 1)，也就是substring(i, i + 10)



然后看了leetcode中的类似的方案，发现其实对这个解法进行优化，使用两个HashSet来代替HashMap。
之所以使用HashMap，是因为需要记录该sequence出现了几次，要在正好之前出现了一次的时候将该sequence加入到结果集中，所以记录出现次数。但是你会发现其实出现次数会有冗余，两次以后不管出现多少次也都没啥用了其实。所以其实可以使用两个HashSet来代替表示这种信息:
第一个HashSet表示出现过的Sequence的集合，repeated表示出现过两次的sequence的集合。配合set.add()会返回Boolean，告诉是否add成功了，就可以最后直接将repeated转化为ArrayList返回(因为跟顺序也没有关系)


这道题还可以巧妙的使用Bit manipulation来做。核心思路是:

因为DNA只有4种可能性，所以可以使用2bit来表示一个DNA符号，那么10个DNA的序列只需要20bit。而Java中一个int是32bit，所以一个**int就足以唯一标识一个10位的DNA序列**。

一开始先把四种DNA分别对应到0...3上，然后对于每个10位的DNA序列，每次移动2bit后就加上新的2bit的DNA(也可以后移动)，计算出相对应的hash,然后再像前一种解法的那样，使用两个HashSet来标识那些重复过一次的sequence，加到results中去。
