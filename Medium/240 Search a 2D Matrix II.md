# 240 Search a 2D Matrix II

[문제](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## 풀이

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
            
        return False
```

```java
// 나중에 자바로 다시 풀기
```

## 설명


