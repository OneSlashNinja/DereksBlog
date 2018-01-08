---
layout: post
title:  "leetcode 210 - Course Schedule 2"
date:   2018-01-03 22:16:54.945028
categories: leetcode, Facebook, Bloomberg
---

# Course Schedule 2

## 一刷

### 代码

```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        if(prerequisites == null){
            return null;
        }
        
        //这回直接使用一个int[]来代替HashMap
        int[] indegree = new int[numCourses];
        Queue<Integer> queue = new LinkedList<Integer>();
        int[] result = new int[numCourses];
        
        //统计所有的indegree
        for(int i = 0; i < prerequisites.length; i++){
            int needToTake = prerequisites[i][0];
            indegree[needToTake]++;
        }
        
        //对于所有入度为0的情况，放到queue里面
        for(int i = 0; i < numCourses; i++){
            if(indegree[i] == 0){
                queue.offer(i);
            }
        }
        
        int index = 0;
        while(!queue.isEmpty()){
            int elem = queue.poll();
            result[index++] = elem;
            
            for(int i = 0; i < prerequisites.length; i++){
                if(prerequisites[i][1] == elem){
                    indegree[prerequisites[i][0]]--;

                    //在减去入度的同时进行入度为0的判断，这样就不用单独还需要检查一遍了
                    if(indegree[prerequisites[i][0]] == 0){
                        queue.offer(prerequisites[i][0]);
                    }
                }
            }
        }
        
        //本题因为返回的是int[]而不是ArrayList，所以需要判断最后是不是所有可能都能完成
        if(index != numCourses){
            return new int[0];
        }
        
        return result;
    }
}
```

### 笔记

基本和lintcode上的Topological Sorting写法是一样的，不过由于输入不一样，所以有些地方不太一样:
1. 因为知道输入的课程数，所以直接使用int[]来代替HashMap
2. 最后需要额外判断下是不是所有课程都能完成
