# 179. Largest Number

[문제](https://leetcode.com/problems/largest-number/)

## 풀이

```python
class compare(str):
    def __lt__(a, b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums = sorted(nums, key=compare)
        output = ''
        for num in nums:
            output += num
            
        if output[0] == '0':
            return '0'
        else:   
            return output
```

```java
// 나중에 자바로 다시 풀기
```

## 설명


