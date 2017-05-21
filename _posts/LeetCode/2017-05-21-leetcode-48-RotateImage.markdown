---
layout: post
title:  "LeetCode 48 - Rotate Image"
date:   2017-05-21 00:15:02 -0400
categories: leetcode, Amazon
---

# Rotate Image

## 一刷

### 代码
转置矩阵+行反转：
```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void rotate(int[][] matrix) {
        // write your code here
        
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = i; j < matrix[0].length; j++){
                swap(matrix, i, j, j, i);
            }
            
            reverse(matrix[i]);
        }
        
    }
    
    private void swap(int[][] matrix, int rowA, int colA, int rowB, int colB){
        int temp = matrix[rowA][colA];
        matrix[rowA][colA] = matrix[rowB][colB];
        matrix[rowB][colB] = temp;
    }


    
    private void reverse(int[] array){
        int left = 0, right = array.length - 1;
        
        int temp;
        while(left < right){
            temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }
}
```

一步到位version：
```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void rotate(int[][] matrix) {
        // write your code here
        
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        for(int i = 0, j = matrix.length - 1; i < j; i++, j--){
            for(int m = i, n = j; m < j; m++, n--){
                int temp = matrix[i][m];
                matrix[i][m] = matrix[n][i];
                matrix[n][i] = matrix[j][n];
                matrix[j][n] = matrix[m][j];
                matrix[m][j] = temp;
            }
        }
        
    }
    
}
```

### 笔记
本题的多种解法中，最喜欢转置矩阵的解法。因为不仅巧妙而且代码相比于“对角线反转+上下翻转”的要少。更重要的是感觉掌握转置矩阵的写法更具有通用性，可能会在其他什么程序中用得上。

这题转置矩阵的写法很巧妙：
(1)首先要注意双层循环，第二层的起点不是0而是i。相当于swap只要应用于以左上到右下为对角线的上一半的三角便可以完成整个矩阵的转置。

(2)虽然对于某一行，只是转置从i到length[0] - 1。但是因为前面行的功劳，前面的0到i - 1已经是转置好了的。
所以在内层的for循环过后便可以很自信地进行：
reverse(matrix[i]);

转置矩阵的英语叫：transposed matrix

而另一种也很巧妙并且代码更少的一步到位法也很有意思，一开始光看程序似乎有点不太好理解，画个图(5x5的矩阵)然后走一遍就了然了。
感觉上有点像spiral matrix中的“削层”的过程：
(1)最内层中一个“连环”的swap操作每次是把四个点分别交换到最终正确的位置上。
(2)而内层的循环一次循环相当于“削一层”把最外层的所有点都交换到正确位置上。这样下一次就只用关心下一层。
(3)最外层的循环就相当于把所有层都“削”完。

代码虽然少，但是写起来并不容易并且但是很容易写错：
(1)首先，两个for循环里面是四个定位的变量，要注意。并且内层循环的起点是当前的外层。
(2)两层循环中的循环终止条件也都需要注意：
外层中，因为这题是正方形，所以其实最中间的一个格子不需要去处理，所以i < j就行了。
内层中更要注意，条件不是m < n而是m < j。具体为什么还是一画图就明白了。
(3)swap是四个点的swap所以看起来很眼花，但还是一边画图一边写就比较不容易出错。另一方面，即使是四个格子swap，还是遵循swap的“链式”原则：第一个肯定是赋给temp，然后就是前一项的右边就是后一项的左边直到形成一个环。

而其实本题的swap中的各个项之间如果硬要找规律的话，那就是：
matrix[a][x] = matrix[和x正好相对的那个变量][a]

---

## 二刷

### 代码

```java
public class Solution {
    public void rotate(int[][] matrix) {
        transposeMatrix(matrix);
        horizontalMirror(matrix);
    }
    
    private void transposeMatrix(int[][] matrix){
        int temp = 0;
        for(int i = 0; i < matrix.length; i++){
            for(int j = i + 1; j < matrix[i].length; j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
    
    private void horizontalMirror(int[][] matrix){
        int temp = 0;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[i].length / 2; j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix[i].length - 1 - j];
                matrix[i][matrix[i].length - 1 - j] = temp;
            }
        }
    }
    
}
```

Grandyang版本[http://www.cnblogs.com/grandyang/p/4389572.html]

```cpp
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                swap(matrix[i][j], matrix[j][i]);
            }
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

### 笔记

转置矩阵: **transposed matrix**

注意这题说明了是n x n的矩阵，否则要做到in place就很麻烦。

这题二刷的时候虽然修改了此处小地方才过，不过大体的思路还是很明确的，最后也是顺利就解出来了。

在纸上一画思路就明确了:**转置矩阵+垂直方向镜像反转**

所以可以将整个程序分成两步完成。

这题最需要注意的一点在于在处理垂直镜像的时候，第i行j列的镜像的位置是(matrix[i].length - 1 - j)而不是(matrix[i].length - j)

另外注意Grandyang的版本的精妙之处，因为转置矩阵的两层循环，外层循环每转置一次，被转置的那一行就相当于再也不会参与到转置的过程中了，所以利用这一点，可以把转置和垂直镜面反转的外层for循环合并。但是缺点是思路就不是那么清晰了，对于读代码的人不会那么一目了然。