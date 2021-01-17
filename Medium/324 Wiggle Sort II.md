# 324 Wiggle Sort II

[문제](https://leetcode.com/problems/wiggle-sort-ii/)

## 풀이

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums)%2 == 0:
            mid = len(nums)//2 - 1
        else:
            mid = len(nums)//2
            
        # nums[::2] = nums[mid::-1]
        # nums[1::2] = nums[:mid:-1]
            
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
```

```java
// 나중에 자바로 다시 풀기
```

## 설명


