# 29 Divide Two Integers

[문제](https://leetcode.com/problems/string-to-integer-atoi/)

## 풀이

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        output = 0
        label = 1

        if dividend * divisor < 0:
            label = -1

        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend - divisor >= 0:
            x = 0
            while dividend - (divisor << 1 << x) > 0:
                x += 1
            dividend -= (divisor << x)
            output += (2 ** x)

        output *= label

        return output
```

```java
// 나중에 자바로 다시 풀기
```

## 설명


