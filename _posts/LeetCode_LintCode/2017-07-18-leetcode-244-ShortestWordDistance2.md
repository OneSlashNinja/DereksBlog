---
layout: post
title:  "leetcode 244 - Shortest Word Distance 2"
date:   2017-07-18 22:39:17.943128
categories: leetcode, Linkedin
---

# Shortest Word Distance 2

## 一刷

### 代码

```java
public class WordDistance {

    private HashMap<String, List<Integer>> map;
    
    public WordDistance(String[] words) {
        map = new HashMap<>();
        for(int i = 0; i < words.length; i++){
            if(!map.containsKey(words[i])){
                map.put(words[i], new ArrayList<>());
            }
            
            map.get(words[i]).add(i);
        }
    }
    
    public int shortest(String word1, String word2) {
        
        List<Integer> word1List = map.get(word1);
        List<Integer> word2List = map.get(word2);
        
        int shortest = Integer.MAX_VALUE;
        
        //这种表示下标的变量用i和j反而更利于理解
        int i = 0, j = 0;
        
        while(i < word1List.size() && j < word2List.size()){
            int word1Index = word1List.get(i);
            int word2Index = word2List.get(j);
            shortest = Math.min(shortest, Math.abs(word1Index - word2Index));
            
            if(word1Index <= word2Index){
                i++;
            }else{
                j++;
            }
            
        }
        
        return shortest;
        
    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(words);
 * int param_1 = obj.shortest(word1,word2);
 */
```

### 笔记

这题是Shortest Word Distance的follow up，而且是经典follow up的形式:

问如果把题1中的操作变成一个类，会经常执行同样的操作，怎么做？是不是能够优化？

从ShortestWordDistance的最优化解可以看出来，对于说直接的搜索，找word1和word2的最短距离的时间已经是O(n)的时间了，不可能再优化了，因为至少需要扫描一遍整个数组才能知道得到最短的距离。那么基本可以肯定，对于这种大量的计算的优化，肯定是**利用空间来换时间，进行预处理**。

那么具体怎么做？使用HashMap。

在类初始化的时候构建HashMap，key为word的string，而value则是该string所对应的所有index，类型是List<Integer>

这里有一个关键的隐含条件，是后面find Shortest的快速找到的关键点，那就是**list中的index都是有序的**

这样的话，在找word1和word2的Shortest的时候，就可以像merge sorted array那样，每次从两个list的头上拿出小的那个，并在这个过程中计算Shortest。


并且该种实现的另一个好处是易于拓展，如果又需要，完全可以再增加一个对外的method:

public void addString(String str){
    ...
}

只需要相应地插入到HashMap中去就可以了(不过需要额外再维护一个length变量)

