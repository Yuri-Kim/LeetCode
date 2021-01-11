# 8 String to Integer (atoi)

[문제](https://leetcode.com/problems/string-to-integer-atoi/)

## 풀이

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        only_num = re.compile(r'^ *([+\-]?\d+)')
        get = only_num.match(s)
        if not get:
            return 0
        else:
            num = int(get.group(1))
            if num >= 0:
                return min(num, 2**31 - 1)
            elif num < 0:
                return max(num, -2**31)
```

```java
// 나중에 자바로 다시 풀기
```

## 설명

부호와 숫자만 남긴후 범위 내에 있는지 확인

