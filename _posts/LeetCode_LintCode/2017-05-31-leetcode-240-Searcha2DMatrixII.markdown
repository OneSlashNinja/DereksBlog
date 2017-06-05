---
layout: post
title:  "LeetCode 240 - Search a 2D Matrix II"
date:   2017-05-31 00:15:02 -0400
categories: leetcode, Amazon
---

# Search a 2D Matrix II

## 一刷

### 代码
一遍扫描(O(m+n))version:
```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param: A number you want to search in the matrix
     * @return: An integer indicate the occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        // write your code here
        if(matrix == null || matrix.length == 0){
            return 0;
        }
        int rowLength = matrix.length;
        int colLength = matrix[0].length;
        
        int rowIndex = 0, colIndex = colLength - 1;
        
        int count = 0;
        
        while(rowIndex < rowLength && colIndex >= 0){
            if(matrix[rowIndex][colIndex] > target){
                colIndex--;
            }else if(matrix[rowIndex][colIndex] < target){
                rowIndex++;
            }else{
                count++;
                rowIndex++;
                colIndex--;
            }
        }
        
        return count;
    }
}
```

### 笔记


> 这道题是经典题, 我在微软和YELP的onsite和电面的时候都遇到了. 
> 从右上角开始, 比较target 和 matrix[i][j]的值. 如果小于target, 则该行不可能有此数,  所以i++; 如果大于target, 则该列不可能有此数, 所以j--. 遇到边界则表明该矩阵不含target.


其实，这题的感觉就是，因为每一行自己和和每一列自己都是有序的，但是不像行和行之间互有关系(Search a 2D Matrix)或者列和列之间互有关系。
所以对于矩阵中的某个点来说，如果其上下左右都有元素，那么对于matrix[i][j]，如果其小于target，则有两个方向可以走：
上和左，如果其大于target，则另两个方向可以走：下和右。
所以，我们需要确定一个组合和一个点，使得在matrix[i][j]时，如果判断其<target。就只有某个方向可以走，而如果其>target，就只有另一个维度上的方向可以走。
所以，合理的选择只有两种：
(1)选择右上角的点。然后在matrix[i][j] > target时往左移动，<target时往下移动。
(2)选择左下角的点，然后再matrix[i][k] > target时往右，<target时往上移动。

为什么感觉有点和2d-tree的有共性的感觉？

这题的实现使用了第(1)种方案。

12.05更新，其实这题的矩阵就是注明的“杨氏矩阵”

---

## 二刷

### 代码

```java
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return false;
        }
        
        int row = 0, col = matrix[0].length - 1;
        
        while(row < matrix.length && col >= 0){
            if(matrix[row][col] == target){
                return true;
            }else if(target < matrix[row][col]){
                col--;
            }else{
                row++;
            }
        }
        
        return false;
    }
}
```


### 笔记

这题一遍AC，应该没什么问题了，思路也很明确，很容易记住。
注意leetcode和lintCode的题目稍微有点差别，leetcode中要求返回的是boolean，是否找到。而lintCode中要求返回的是target的个数。