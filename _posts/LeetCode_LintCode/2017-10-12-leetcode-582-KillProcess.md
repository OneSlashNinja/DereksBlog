---
layout: post
title:  "leetcode 582 - Kill Process"
date:   2017-10-12 23:03:13.410631
categories: leetcode, Bloomberg
---

# Kill Process

## 一刷

### 代码

理论正确，但超时的Set+Queue版本
```java
class Solution {
    
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        
        Set<Integer> resultSet = new HashSet<Integer>();
        
        Queue<Integer> queue = new LinkedList<Integer>();
        
        queue.offer(kill);
        
        while(queue.size() > 0){
            resultSet.add(queue.peek());
            int current = queue.poll();
            for(int i = 0; i < ppid.size(); i++){
                if(ppid.get(i) == current && !resultSet.contains(pid.get(i))){
                    resultSet.add(pid.get(i));
                    queue.offer(pid.get(i));
                }
            }
        }
        
        return new ArrayList<Integer>(resultSet);
        
    }
}
```

看了leetcode题解后，利用HashMap进行预处理后的优化BFS版本(还是使用Queue)
```java
class Solution {
    
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        
        //构建HashMap
        for(int i = 0; i < pid.size(); i++){
            
            if(ppid.get(i) == 0){
                continue;
            }
            
            if(!map.containsKey(ppid.get(i))){
                map.put(ppid.get(i), new ArrayList<Integer>());
            }
            
            map.get(ppid.get(i)).add(pid.get(i));
        }
        
        //使用Queue,配合HashMap进行BFS
        
        List<Integer> results = new ArrayList<Integer>();
        
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(kill);
        
        while(!queue.isEmpty()){
            int current = queue.poll();
            results.add(current);
            if(!map.containsKey(current)){//It is the leaf node
                continue;
            }
            
            for(int childId : map.get(current)){
                queue.offer(childId);
            }
            
        }
        
        return results;
    }
    
}
```

DFS的版本
```java
class Solution {
    
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        
        //和BFS的预处理完全一样，构建HashMap
        for(int i = 0; i < pid.size(); i++){
            
            if(ppid.get(i) == 0){
                continue;
            }
            
            if(!map.containsKey(ppid.get(i))){
                map.put(ppid.get(i), new ArrayList<Integer>());
            }
            
            map.get(ppid.get(i)).add(pid.get(i));
        }
        
        //使用Queue,配合HashMap进行BFS
        
        List<Integer> results = new ArrayList<Integer>();
        
        dfsHelper(map, results, kill);
        
        return results;
    }
    
    private void dfsHelper(HashMap<Integer, List<Integer>> map, List<Integer> results, int kill){
        
        results.add(kill);
        
        //触底
        if(!map.containsKey(kill)){
            return;
        }
        
        List<Integer> children = map.get(kill);
        for(int id : children){
            dfsHelper(map, results, id);
        }
    }
    
}
```

### 笔记

自己一开始的思路其实就是经典的BFS套路: HashSet + Queue

但是很致命的一点缺陷就是有大量的冗余重复查找，每次想要看一个node的所有children时，都需要整个再遍历搜一遍ppid这个list。

而正确的做法就是用空间换时间(其实在这题中都并没有真正增加空间复杂度，因为即使不用预处理，本身也需要用一个HashSet), **进行预处理**。而这里的预处理的办法就是将父与子的对应关系使用HashMap<Integer, List<Integer>>表示出来。

这样每次在寻找某个node的所有children时，就能通过HashMap的优势，通过O(1)时间找到。

---

本题另一个之所以是好题的原因就是其多种解法，参考[LeetCode - Kill Process](https://leetcode.com/articles/kill-process/): 
不仅可以通过构建树来解，还可以很好地比较DFS(利用recursion)和BFS(利用Queue)两种不同的解法。

相比于BFS，DFS的特点就很明显了:
    * 因为要对某块代码进行recursion，所以需要额外创建一个helper方法。
    * 返回类型是void，因为结果通过一个传参在方法中进行添加。
    * 参数中还需要map来作为超找的字典，kill作为当前处理id的参照
