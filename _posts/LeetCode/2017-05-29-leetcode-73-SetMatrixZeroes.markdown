---
layout: post
title:  "LeetCode 73 - Set Matrix Zeroes"
date:   2017-05-29 00:15:02 -0400
categories: leetcode, Amazon
---

# Set Matrix Zeroes

## 一刷

### 代码
O(m + n)版：
```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void setZeroes(int[][] matrix) {
        // write your code here
        
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        boolean[] rowZero = new boolean[matrix.length];
        boolean[] colZero = new boolean[matrix[0].length];
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    rowZero[i] = true;
                    colZero[j] = true;
                }
            }
        }
        
        for(int i = 0; i < matrix.length; i++){
            if(rowZero[i]){
                setRowZeros(matrix, i);
            }
        }
        
        for(int i = 0; i < matrix[0].length; i++){
            if(colZero[i]){
                setColZeros(matrix, i);
            }
        }
        
    }
    
    private void setRowZeros(int[][] matrix, int row){
        for(int j = 0; j < matrix[0].length; j++){
            matrix[row][j] = 0;
        }
    }
    
    private void setColZeros(int[][] matrix, int col){
        for(int j = 0; j < matrix.length; j++){
            matrix[j][col] = 0;
        }
    }
    
}
```

in place，将初始0炸过的位置设置为Integer.MIN_VALUE版：
```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void setZeroes(int[][] matrix) {
        // write your code here
        
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    setRowMin(matrix, i);
                    setColMin(matrix, j);
                    matrix[i][j] = Integer.MIN_VALUE;
                }
            }
        }
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == Integer.MIN_VALUE){
                    matrix[i][j] = 0;
                }
            }
            
        }
        
    }
    
    private void setRowMin(int[][] matrix, int row){
        for(int i = 0; i < matrix[0].length; i++){
            if(matrix[row][i] != 0){
                matrix[row][i] = Integer.MIN_VALUE;
            }
        }
    }
    
    private void setColMin(int[][] matrix, int col){
        for(int i = 0; i < matrix.length; i++){
            if(matrix[i][col] != 0){
                matrix[i][col] = Integer.MIN_VALUE;
            }
        }
    }
    
}
```

利用第一行和第一列的in place版本：
```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void setZeroes(int[][] matrix) {
        // write your code here
        
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        boolean firstRowZero = false;
        boolean firstColZero = false;
        
        //先标记是否第一排最后都是0
        for(int i = 0; i < matrix[0].length; i++){
            if(matrix[0][i] == 0){
                firstRowZero = true;
                break;
            }
        }
        
        //再标记是否第一列最后都是0
        for(int i = 0; i < matrix.length; i++){
            if(matrix[i][0] == 0){
                firstColZero = true;
                break;
            }
        }
        
        //开始利用第一排和第一列作为标志位进行标记
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1;j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        //利用刚才的标记位开始处理除第一行和第一列的所有位置
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1;j < matrix[0].length; j++){
                if(matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
        
        //回过头处理第一行
        if(firstRowZero){
            for(int i = 0; i < matrix[0].length; i++){
                matrix[0][i] = 0;
            }
        }
        
        //回过头处理第一列
        if(firstColZero){
            for(int i = 0; i < matrix.length; i++){
                matrix[i][0] = 0;
            }
        }
        
    }
    
}
```

### 笔记

刚看到这题时候和喜刷刷大神的感觉一样：

“
这题题意不是很清楚。很容易让人觉得置0是“连锁反应”，造成最后每个元素都为0。而实际题目的意思是，只有在原始矩阵中为0的数字才能将相应行列置0。而原本非0的数字，即使由于同行或同列的0元素而被置0了，也不能将它相关的行列置0。即这种置0的操作没有传递性，
”

所以，其实这题就是“炸弹人”：每个原始数组里面有0的地方就是个“炸弹”，炸过的地方也是0，但是炸过后的0不再是炸弹。（如果具有“连锁反应”的话，那么可以想象，结果肯定会是：但凡整个matrix中出现一个0，那么最终结果肯定是整个matrix全部为0）
所以，是肯定需要额外的空间用来辅助buff到底哪些0是原始的0，哪些0是“炸”过后的0.

O(mn)的解法和O(m + n)的解法比较容易想到。但是O(1)的方法稍微不是那么直接。
一开始自己的灵感来自于"word search"那道题，想着可以用一个不会用到的字符来buff表示目标0。但问题在于这是int数组，所以就选了Integer.MIN_VALUE来表示。但是果然在某个大数据的阶段出错了，应该就是因为实际数据中本身就有了MIN_VALUE。

那么援引喜刷刷的总结：
“
1. O(mn)解法：克隆原来的matrix，然后扫描原来的matrix，遇到0，则在克隆版本中将对应的行列置0。
2. O(m+n)解法：用两个bool数组O(n)和O(m)，分别记录每行和每列的是否需要被置0。最后根据这两个数组来置0整个矩阵。
3. O(1)解法：用第0行和第0列来记录第1 ~ m-1行和第1 ~ n-1列是否需要置0。而用两个变量记录第0行和第0列是否需要置0。
”

其实可以发现，其实解法二就是解法一的升级，而解法三就是解法二的进一步升级：
解法1到解法2：
因为本来“一炸”就是一行和一列，所以，没必要保存二维matrix，只需要两个独立分别的array即可。
解法2到解法3：
其实这两个array可以直接使用原matrix中的某一行和某一列表示(其实可以是任意一行和一列，只不过是方便，所以选择了第0行和第0列)，而被“征用”的那一行和那一列可以“坍塌”成只用分别一个boolean表示即可。

所以，虽然解法3的代码很长，但是思路并不复杂，唯一需要注意的就是计算firstRowZero和firstColZero以及利用这两个flag来将第0行和第0列置0的顺序或者说位置(相当于最外层的大括号，一个在最前面，一个在最后面)。

感觉这道题除了这种“递归”进化的思想，其他似乎并没有什么意义。
---

## 二刷

### 代码

O(m + n)版
```java
public class Solution {
    public void setZeroes(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        boolean[] rowZeros = new boolean[matrix.length];
        boolean[] colZeros = new boolean[matrix[0].length];
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[i].length; j++){
                if(matrix[i][j] == 0){
                    rowZeros[i] = true;
                    colZeros[j] = true;
                }
            }
        }
        
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[i].length; j++){
                if(rowZeros[i] || colZeros[j]){
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
```

O(1) extra space版
```java
public class Solution {
    public void setZeroes(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }
        
        boolean firstRowHasZero = false;
        boolean firstColHasZero = false;
        
        for(int i = 0; i < matrix[0].length; i++){
            if(matrix[0][i] == 0){
                firstRowHasZero = true;
                break;
            }
        }
        
        for(int i = 0; i < matrix.length; i++){
            if(matrix[i][0] == 0){
                firstColHasZero = true;
                break;
            }
        }
        
        //注意下标是以1开始的，因为第一排最后处理
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1; j < matrix[i].length; j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        
        //注意下标是以1开始的，因为第一排最后处理
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1; j < matrix[i].length; j++){
                if(matrix[0][j] == 0 || matrix[i][0] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
        
        if(firstRowHasZero){
            for(int i = 0; i < matrix[0].length; i++){
                matrix[0][i] = 0;
            }
        }
        
        if(firstColHasZero){
            for(int i = 0; i < matrix.length; i++){
                matrix[i][0] = 0;
            }
        }
        
    }
}
```

### 笔记
关于具体的思路，一刷的时候已经写的非常详细和明确了。第二刷错误的地方要注意的就是在中间的两个两层for循环处，因为是利用第一层row和第一层col，所以下标需要时以1开始。